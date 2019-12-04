"""
Author: "Rangana Warshamanage, Garib N. Murshudov"
MRC Laboratory of Molecular Biology
    
This software is released under the
Mozilla Public License, version 2.0; see LICENSE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
from timeit import default_timer as timer
from emda.plotter import plot_nlines
from emda.quaternions import get_RM
from emda.mapfit.utils import get_FRS,create_xyz_grid,get_xyz_sum
import fcodes_fast
from emda.restools import cut_resolution_for_linefit
from emda.mapfit.derivatives_newmethod2 import derivatives
from emda.config import *

np.set_printoptions(suppress=True) # Suppress insignificant values for clarity

#debug_mode = 0 # 0: no debug info, 1: debug

class EmFit:
    def __init__(self,mapobj):
        self.mapobj         = mapobj
        self.cut_dim        = mapobj.cdim
        self.ful_dim        = mapobj.map_dim
        self.cell           = mapobj.map_unit_cell
        self.origin         = mapobj.map_origin
        self.w_grid         = None
        self.fsc            = None 
        self.sv             = None
        self.t              = None
        self.st             = None
        self.step           = None
        self.rotmat         = None

    def get_wght(self,e0,ert):
        cx,cy,cz = e0.shape
        start = timer()
        f1f2_covar,fsc = fcodes_fast.calc_covar_and_fsc_betwn_anytwomaps(e0,
                                ert,
                                self.mapobj.cbin_idx,
                                self.mapobj.cbin,
                                debug_mode,
                                cx,cy,cz)
        fsc = np.array(fsc, dtype=np.float64, copy=False)

        w_grid = fcodes_fast.read_into_grid(self.mapobj.cbin_idx,
                                fsc/(1-fsc**2),
                                self.mapobj.cbin,
                                cx,cy,cz)
        w_grid = np.array(w_grid, dtype=np.float64, copy=False)

        fsc_sqd = fsc**2
        fsc_combi = fsc_sqd/(1 - fsc_sqd)
        w2_grid = fcodes_fast.read_into_grid(self.mapobj.cbin_idx,
                                fsc_combi,
                                self.mapobj.cbin,cx,cy,cz)
        end = timer()
        #print('weight calc time: ', end-start)
        return w_grid,w2_grid,fsc

    def functional(self,e0,e1):
        start = timer()
        cx,cy,cz = e0.shape
        self.st,s1,s2,s3 = fcodes_fast.get_st(cx,cy,cz,self.t)
        #self.st = np.transpose(st_transpose)
        self.sv = np.array([s1,s2,s3])
        self.ert = get_FRS(self.cell,self.rotmat,e1 * self.st)[:,:,:,0]
        self.w_grid,self.w2_grid,self.fsc = self.get_wght(e0, self.ert) # translate and then rotate
        fval = np.sum(self.w_grid * e0 * np.conjugate(self.ert))
        end = timer()
        #print('functional calc time: ', end-start)
        return fval.real

    def f(self,k):
        # w = 1.0 for line search
        nx,ny,nz = self.e0_lf.shape
        t = self.step[:3]*k[0]
        st,_,_,_ = fcodes_fast.get_st(nx,ny,nz,t)
        q_init = np.array([1.0, 0.0, 0.0, 0.0])
        tmp = np.insert(self.step[3:]*k[1], 0, 0.0)
        tmp = tmp + q_init
        q = tmp/np.sqrt(np.dot(tmp, tmp))
        rotmat = get_RM(q)
        ers = get_FRS(self.cell,rotmat,self.e1_lf * st)
        fval = np.sum(self.e0_lf * np.conjugate(ers[:,:,:,0]))
        return -fval.real

    def calc_fval_for_different_kvalues_at_this_step(self,step,e0,e1):
        from scipy import optimize
        nx,ny,nz = e0.shape
        w = 1.0
        start = timer()
        smax = 15 # cut resolution in Angstrom
        self.e0_lf = cut_resolution_for_linefit(self.e0,self.mapobj.cbin_idx,self.mapobj.res_arr,smax)
        self.e1_lf = cut_resolution_for_linefit(self.e1,self.mapobj.cbin_idx,self.mapobj.res_arr,smax)
        init_guess = [1.0,1.0]
        minimum = optimize.minimize(self.f, init_guess, method='Powell')
        end = timer()
        #print('time for line search: ', end-start)
        return minimum.x

    def minimizer(self,ncycles,t_init,rotmat):
        from emda.mapfit import rotmat2quart

        fsc_lst         = []
        fval_lst        = []
        theta2_lst      = []
        trans_lst       = []

        nfit = len(self.mapobj.ceo_lst) - 1
        self.e0 = self.mapobj.ceo_lst[0] # Static map e-data for fit
        xyz = create_xyz_grid(self.cell, self.cut_dim)
        vol = self.cell[0] * self.cell[1] * self.cell[2]
        xyz_sum = get_xyz_sum(xyz)
        q_init = np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float64)
        self.trans_para = []
        self.rot_para   = []

        print('Cycle#   ', 'Func. value  ', 'Rotation(degrees)  ', 'Translation(A)  ')
        for ifit in range(nfit):
            self.e1 = self.mapobj.ceo_lst[ifit + 1]
            for i in range(ncycles):
                start = timer()
                if i == 0:
                    self.t = np.asarray(t_init)
                    t_accum = self.t
                    t_accum_angstrom = t_accum * self.cell[:3]
                    translation_vec = np.sqrt(np.sum(t_accum_angstrom * t_accum_angstrom))
                    # passing rotmat instead of theta_init
                    self.rotmat = rotmat
                    q = rotmat2quart.rot2quart(self.rotmat)
                    self.q = q
                    q_accum = self.q
                    theta2 = np.arccos((np.trace(self.rotmat) - 1)/2) * 180./np.pi
                else:
                    self.rotmat = get_RM(self.q)
                    rm_accum = get_RM(q_accum)
                    theta2 = np.arccos((np.trace(rm_accum) - 1)/2) * 180./np.pi

                #print(self.rotmat)
                fval = self.functional(self.e0, self.e1)
                fval_lst.append(fval) 
                theta2_lst.append(theta2)
                trans_lst.append(translation_vec)
                #print(i,fval,theta2,translation_vec,q,self.t)
                print(i,fval,theta2,translation_vec)

                if i == 0 or i == ncycles-1: 
                    fsc_lst.append(self.fsc)

                if i == ncycles-1:
                    rotmat = get_RM(q_accum)
                    self.rotmat = rotmat
                    self.t_accum = t_accum
                    self.fsc_lst = fsc_lst

                self.step,self.grad,self.e1 = derivatives(self.e0,
                            self.ert,self.w_grid,self.w2_grid,q,self.sv,xyz,xyz_sum,vol)
                alpha = self.calc_fval_for_different_kvalues_at_this_step(self.step,self.e0,self.e1)
                self.t = self.step[:3]*alpha[0]
                #self.t = np.asarray([0.0, 0.0, 0.0]) # for no translation test
                t_accum = t_accum + self.t
                t_accum_angstrom = t_accum * self.cell[:3]
                translation_vec = np.sqrt(np.sum(t_accum_angstrom * t_accum_angstrom))
                tmp = np.insert(self.step[3:]*alpha[1],0,0.0)
                q_accum = q_accum + tmp
                q_accum = q_accum/np.sqrt(np.dot(q_accum, q_accum))
                tmp = tmp + q_init
                #tmp = q_init  # for no-rotation test
                q = tmp/np.sqrt(np.dot(tmp, tmp))
                self.q = q
                end = timer()
                #print('time for one cycle:', end-start)
            #plot_nlines(self.mapobj.cres_arr,fsc_lst,'before_and_after_fit.eps',["Start","End"])
            

