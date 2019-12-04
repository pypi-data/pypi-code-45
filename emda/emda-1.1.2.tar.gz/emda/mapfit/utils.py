"""
Author: "Rangana Warshamanage, Garib N. Murshudov"
MRC Laboratory of Molecular Biology
    
This software is released under the
Mozilla Public License, version 2.0; see LICENSE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import fcodes_fast
from emda.plotter import plot_nlines,plot_nlines_log
from timeit import default_timer as timer
from emda.config import *

#debug_mode = 0 # 0: no debug info, 1: debug

def get_FRS(uc,RM,E2):
    # scipy interpolation  
    #ERS = interpolate_scipy(E2,RM) 
    #ERS = np.expand_dims(ERS, axis=3) 
    # end
    if len(E2.shape) == 3:
        E2 = np.expand_dims(E2, axis=3)
    ERS = get_interp(uc,RM,E2)
    return ERS

def get_interp(uc,RM,data):
    import fcodes_fast
    assert len(data.shape) == 4
    ih,ik,il,n = data.shape
    interp3d = fcodes_fast.tricubic(RM,data,debug_mode,n,ih,ik,il)
    return interp3d

def create_xyz_grid(uc,nxyz):
    x = np.fft.fftfreq(nxyz[0]) * uc[0]
    y = np.fft.fftfreq(nxyz[1]) * uc[1]
    z = np.fft.fftfreq(nxyz[2]) * uc[2]
    xv, yv, zv = np.meshgrid(x,y,z)
    xyz = [yv,xv,zv]
    for i in range(3):
        xyz[i] = np.fft.ifftshift(xyz[i])
    return xyz

def get_xyz_sum(xyz):
    xyz_sum = np.zeros(shape=(6),dtype='float')
    n = -1
    for i in range(3):  
        for j in range(3):
            if i == 0:
                sumxyz = np.sum(xyz[i] * xyz[j])
            elif i > 0 and j >= i:
                sumxyz = np.sum(xyz[i] * xyz[j])
            else:
                continue
            n = n + 1
            xyz_sum[n] = sumxyz   
    print(xyz_sum)
    return xyz_sum

def avg_and_diffmaps(maps2avg,uc,nbin,sgnl_var,totl_var,covar,fsc12,hffsc,bin_idx,s_grid,res_arr,Bf_arr):
    # average and difference map calculation
    import numpy as np
    import numpy.ma as ma
    import fcodes_fast
    nx,ny,nz = maps2avg[0].shape
    nmaps = len(maps2avg)
    unit_cell = uc
    all_maps = np.zeros(shape=(nx,ny,nz,nmaps),dtype='complex')
    for i in range(nmaps):
        all_maps[:,:,:,i] = maps2avg[i]
    print(all_maps.shape)
    #
    S_mat = np.zeros(shape=(nmaps,nmaps,nbin),dtype='float')
    T_mat = np.zeros(shape=(nmaps,nmaps,nbin),dtype='float')
    F_mat = np.zeros(shape=(nmaps,nmaps,nbin),dtype='float')
    # Populate Sigma matrix
    start = timer()
    for i in range(nmaps):
        for j in range(nmaps):
            if i == j:
                print('i,j=',i,j)
                # Diagonals
                S_mat[i,i,:] = 1.0
                T_mat[i,i,:] = 1.0
                F_mat[i,i,:] = np.sqrt(ma.masked_less_equal(hffsc[i],0.0).filled(0.0))
            elif j > i:
                # Off diagonals
                print('i,j=',i,j)
                plot_nlines_log(res_arr,[covar[j-1],sgnl_var[i],sgnl_var[j]],
                                ["S12","S11","S22"],'log_variance_signal.eps')
                Sigma_ij_ma = ma.masked_less_equal(covar[j-1],0.0)
                sgnl_var_ij_ma = ma.masked_where(ma.getmask(Sigma_ij_ma), sgnl_var[i] * sgnl_var[j])
                S_mat[i,j,:] = (Sigma_ij_ma / np.sqrt(sgnl_var_ij_ma)).filled(0.0)
                Totalv_ij_ma = ma.masked_where(ma.getmask(Sigma_ij_ma), totl_var[i] * totl_var[j])
                T_mat[i,j,:] = (Sigma_ij_ma / np.sqrt(Totalv_ij_ma)).filled(0.0)
                plot_nlines_log(res_arr,
                                [covar[j-1],totl_var[i],totl_var[j]],
                                ["S12","T11","T22"],'log_variance_totalv.eps')
            else:
                print('i,j=',i,j)
                S_mat[i,j,:] = S_mat[j,i,:]
                T_mat[i,j,:] = T_mat[j,i,:]
    # Plotting
    plot_nlines(res_arr,[S_mat[0,0,:],S_mat[0,1,:],S_mat[1,0,:],S_mat[1,1,:]],
                        'S_mat_fsc_ij.eps',
                        ["FSC11","FSC12","FSC21","FSC22"])
    plot_nlines(res_arr,[F_mat[0,0,:],F_mat[1,1,:]],
                        'F_mat_fsc_ij.eps',
                        ["sqrt(FSC11)","sqrt(FSC22)"])
    plot_nlines(res_arr,[T_mat[0,0,:],T_mat[0,1,:],T_mat[1,0,:],T_mat[1,1,:]],
                        'T_mat_fsc_ij.eps',
                        ["FSC11","FSC12","FSC21","FSC22"])
    end = timer()
    print('Time for sigma matrix population: ', end-start)
    start = timer()
    # Variance weighted matrices calculation
    Wgt = np.zeros(shape=(nmaps,nmaps,nbin))
    for ibin in range(nbin):
        T_mat_inv = np.linalg.pinv(T_mat[:,:,ibin]) # Moore-Penrose psedo-inversion
        tmp = np.dot(F_mat[:,:,ibin],T_mat_inv)
        Wgt[:,:,ibin] = np.dot(S_mat[:,:,ibin],tmp)
    plot_nlines(res_arr,[Wgt[0,0,:],Wgt[0,1,:],Wgt[1,0,:],Wgt[1,1,:]],
                        'Wgt_map_ij.eps',
                        ["W11","W12","W21","W22"])
    end = timer()
    print('time for pinv  ',end-start)
    # Average map calculation
    nbf = len(Bf_arr)
    assert all_maps.shape[:3] == bin_idx.shape
    assert all_maps.shape[3] == nmaps
    AVG_Maps = fcodes_fast.calc_avg_maps(all_maps,
                                         bin_idx,
                                         s_grid,
                                         Wgt,
                                         Bf_arr,
                                         unit_cell,
                                         debug_mode,
                                         nbin,
                                         nmaps,
                                         nbf,
                                         nx,ny,nz)
    return AVG_Maps

def output_maps(averagemaps,com,unit_cell,map_origin,bf_arr):
    import emda.iotools as iotools
    start = timer()
    nx, ny, nz = averagemaps.shape[:3]
    center = (nx/2, ny/2, nz/2)
    for ibf in range(averagemaps.shape[4]):
        if bf_arr[ibf] < 0.0:
            Bcode = '_blur'+str(abs(bf_arr[ibf]))
        elif bf_arr[ibf] > 0.0:
            Bcode = '_sharp'+str(abs(bf_arr[ibf]))
        elif bf_arr[ibf] == 0.0:
            Bcode = '_unsharpened'
        for imap in range(averagemaps.shape[3]):
            filename_mrc = 'avgmap_'+str(imap)+Bcode+'.mrc'
            data2write = apply_shift(averagemaps[:,:,:,imap,ibf],com,center) # center not given
            iotools.write_mrc(data2write,
                              filename_mrc,
                              unit_cell,
                              map_origin)
            # Writing to .mtz file
            '''filename_mtz = 'avgmap_'+str(imap)+Bcode+'.mtz'
            write_3d2mtz_fortran(unit_cell,average_maps[:,:,:,imap,ibf],filename_mtz)'''
        
        # Difference and Biase removed map calculation
        nmaps = averagemaps.shape[3]
        for m in range(nmaps-1):
            for n in range(m+1,nmaps):
                fname_diff1 = 'diffmap_m'+str(n)+'-m'+str(m)+Bcode
                dm1 = apply_shift(averagemaps[:,:,:,n,ibf] - averagemaps[:,:,:,m,ibf],com,center)
                iotools.write_mrc(dm1,
                                  fname_diff1+'.mrc',
                                  unit_cell,map_origin)
                '''write_3d2mtz_fortran(unit_cell,dm1,fname_diff1+'.mtz')'''
                dm2 = apply_shift(averagemaps[:,:,:,m,ibf] - averagemaps[:,:,:,n,ibf],com,center)
                fname_diff2 = 'diffmap_m'+str(m)+'-m'+str(n)+Bcode
                iotools.write_mrc(dm2,
                                  fname_diff2+'.mrc',
                                  unit_cell,map_origin)
                '''write_3d2mtz_fortran(unit_cell,dm2,fname_diff2+'.mtz')'''
                # 2Fo-Fc type maps
                twom2m1 = apply_shift(averagemaps[:,:,:,n,ibf] + dm1, com, center)
                fname1_2FoFc = '2m'+str(n)+'-m'+str(m)
                iotools.write_mrc(twom2m1,
                                  fname1_2FoFc+'.mrc',
                                  unit_cell,map_origin)
                '''write_3d2mtz_fortran(unit_cell,twom2m1,fname1_2FoFc+'.mtz')'''
                twom1m2 = apply_shift(averagemaps[:,:,:,m,ibf] + dm2, com, center)
                fname2_2FoFc = '2m'+str(m)+'-m'+str(n)
                iotools.write_mrc(twom1m2,
                                  fname2_2FoFc+'.mrc',
                                  unit_cell,map_origin)
                '''write_3d2mtz_fortran(unit_cell,twom1m2,fname2_2FoFc+'.mtz')'''
    end = timer()
    print('Map output time: ',end-start)

def apply_shift(f_map, com, center):
    import numpy as np
    from scipy.ndimage.interpolation import shift
    shifted_data = np.real(np.fft.ifftshift(
                         np.fft.ifftn(
                         np.fft.ifftshift(f_map))))
    shifted_data = shift(shifted_data, np.subtract(com, center))
    return shifted_data

def remove_unwanted_corners(uc,target_dim):
    from emda.restools import get_resArr,remove_edge
    nx,ny,nz = target_dim
    fResArr = get_resArr(uc,nx)

    cut_mask = remove_edge(fResArr,fResArr[-1])
    cc_mask = np.zeros(shape=(nx,ny,nz),dtype='int')
    cx, cy, cz = cut_mask.shape
    dx = (nx - cx)//2
    dy = (ny - cy)//2
    dz = (nz - cz)//2
    print(dx,dy,dz)
    cc_mask[dx:dx+cx, dy:dy+cy, dz:dz+cz] = cut_mask
    return cc_mask

def double_the_axes(arr1):
    nx, ny, nz = arr1.shape
    big_arr1 = np.zeros((2*nx, 2*ny, 2*nz), dtype='float')
    dx = int(nx/2); dy = int(ny/2); dz = int(nz/2)
    big_arr1[dx:dx+nx, dy:dy+ny, dz:dz+nz] = arr1
    return big_arr1

def get_minimum_bounding_dims(arr1):
    # box dim check begin
    indices = np.indices(arr1.shape)
    from scipy import ndimage
    map_sum = np.sum(arr1)/1000
    arr1 = arr1 * (arr1 > map_sum)
    com = ndimage.measurements.center_of_mass(arr1)
    dist2 = ((indices[0,:,:] - com[0]) ** 2 + 
             (indices[1,:,:] - com[1]) ** 2 + 
             (indices[2,:,:] - com[2]) ** 2)
    #np.max(dist2[mask > 0.5])
    min_dim = int(np.sqrt(np.max(dist2)) * 2) + 1
    print(com,min_dim)
    # box dim check end
    return com, min_dim

def realsp_map_interpolation(arr1,RM):
    from scipy import ndimage
    com = ndimage.measurements.center_of_mass(arr1)
    print(com)
    com = (120, 120, 120)
    nx, ny, nz = arr1.shape
    print(nx, ny, nz)
    rotated_map = fcodes_fast.trilinear_map(RM,com,arr1,nx,ny,nz)
    return rotated_map

def calc_averagemaps_simple(maps2avg,uc,nbin,sgnl_var,totl_var,covar,fsc12,hffsc,bin_idx,res_arr,Bf_arr):
    # average and difference map calculation
    import numpy as np
    import numpy.ma as ma
    import fcodes_fast
    nx,ny,nz = maps2avg[0].shape
    nmaps = len(maps2avg)
    unit_cell = uc
    all_maps = np.zeros(shape=(nx,ny,nz,nmaps),dtype='complex')
    for i in range(nmaps):
        all_maps[:,:,:,i] = maps2avg[i]
    print(all_maps.shape)
    #
    S_mat = np.zeros(shape=(nmaps,nmaps,nbin),dtype='float') # signal variance
    T_mat = np.zeros(shape=(nmaps,nmaps,nbin),dtype='float') # total variance
    # Populate Sigma matrix
    start = timer()
    for i in range(nmaps):
        for j in range(nmaps):
            if i == j:
                print('i,j=',i,j)
                # Diagonals
                S_mat[i,i,:] = sgnl_var[i]
                T_mat[i,i,:] = totl_var[i]               
            elif j > i:
                # Off diagonals
                print('i,j=',i,j)
                S_mat[i,j,:] = covar[j-1]
                T_mat[i,j,:] = covar[j-1]
            else:
                print('i,j=',i,j)
                S_mat[i,j,:] = S_mat[j,i,:]
                T_mat[i,j,:] = T_mat[j,i,:]
    # Plotting
    plot_nlines_log(res_arr,[S_mat[0,0,:],S_mat[0,1,:],S_mat[1,0,:],S_mat[1,1,:]],
                            ["S11","S12","S21","S22"],'S_mat_fsc_ij.eps')
    plot_nlines_log(res_arr,[T_mat[0,0,:],T_mat[0,1,:],T_mat[1,0,:],T_mat[1,1,:]],
                            ["T11","T12","TC21","T22"],'T_mat_fsc_ij.eps')

    end = timer()
    print('Time for sigma matrix population: ', end-start)
    start = timer()
    # Variance weighted matrices calculation
    Wgt = np.zeros(shape=(nmaps,nmaps,nbin))
    for ibin in range(nbin):
        T_mat_inv = np.linalg.pinv(T_mat[:,:,ibin]) # Moore-Penrose psedo-inversion
        Wgt[:,:,ibin] = np.dot(S_mat[:,:,ibin],T_mat_inv)
    plot_nlines(res_arr,[Wgt[0,0,:],Wgt[0,1,:],Wgt[1,0,:],Wgt[1,1,:]],
                        'Wgt_map_ij.eps',["W11","W12","W21","W22"])
    end = timer()
    print('time for pinv  ',end-start)
    # Average map calculation
    nbf = len(Bf_arr)
    assert all_maps.shape[:3] == bin_idx.shape
    assert all_maps.shape[3] == nmaps
    AVG_Maps = fcodes_fast.calc_avg_maps(all_maps,
                                    bin_idx,
                                    Wgt,
                                    Bf_arr,
                                    unit_cell,
                                    debug_mode,
                                    nbin,
                                    nmaps,
                                    nbf,
                                    nx,ny,nz)
    return AVG_Maps