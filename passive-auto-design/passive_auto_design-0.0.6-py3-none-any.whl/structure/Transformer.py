# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:10:47 2019

@author: mpoterea
"""
import numpy as np
from scipy.optimize import minimize_scalar
from ..special import u0, eps0

class Transformer:
    """
        Create a transformator object with the specified geometry _primary & _secondary
        (which are dict defined as :
            {'di':_di,'n_turn':_n_turn, 'width':_width, 'gap':_gap, 'height':height})
        and calculate the associated electrical model
    """
    def __init__(self, _primary, _secondary, _eps_r=4.2, _dist=9, _dist_sub=1e9, _freq=1e9):
        self.prim = _primary
        self.second = _secondary
        self.dist = _dist
        self.dist_sub = _dist_sub
        self.freq = _freq
        self.eps_r = _eps_r
        self.model = {'lp':self.l_geo(True),
                      'rp':self.r_geo(True, 17e-9),
                      'ls':self.l_geo(False),
                      'rs':self.r_geo(False, 17e-9),
                      'cg':self.cc_geo(False),
                      'cm':self.cc_geo(True),
                      }
    def set_primary(self, _primary):
        """
            modify the top inductor and refresh the related model parameters
        """
        self.prim = _primary
        self.model['lp'] = self.l_geo(True)
        self.model['rp'] = self.r_geo(True, 17e-9)
        self.model['cg'] = self.cc_geo(False)
        self.model['cm'] = self.cc_geo(True)
    def set_secondary(self, _secondary):
        """
            modify the bottom inductor and refresh the related model parameters
        """
        self.second = _secondary
        self.model['ls'] = self.l_geo(False)
        self.model['rs'] = self.r_geo(False, 17e-9)
        self.model['cg'] = self.cc_geo(False)
        self.model['cm'] = self.cc_geo(True)
    def l_geo(self, _of_primary=True):
        """
            return the value of the distributed inductance of the described transformer
            if _of_primary, return the value of the top inductor
            else, return the value of the bottom inductor
        """
        k_1 = 1.265   #constante1 empirique pour inductance
        k_2 = 2.093   #constante2 empirique pour inductance
        if _of_primary:
            geo = self.prim
        else:
            geo = self.second
        outer_diam = geo['di']+2*geo['n_turn']*geo['width']+2*(geo['n_turn']-1)*geo['gap']
        rho = (geo['di']+outer_diam)/2
        density = (outer_diam-geo['di'])/(outer_diam+geo['di'])
        return k_1*u0*geo['n_turn']**2*rho/(1+k_2*density)
    def cc_geo(self, _mutual=True):
        """
            return the value of the distributed capacitance of the described transformer
            if _mutual, return the capacitance between primary and secondary
            else, return the capacitance to the ground plane
        """
        if _mutual:
            dist = self.dist
        else:
            dist = self.dist_sub
        c_1 = 8.275   #constante1 empirique pour capacité
        c_2 = 5.250   #constante2 empirique pour capacité
        n_t = self.prim['n_turn']
        return self.prim['width']*eps0*self.eps_r*(c_1+c_2*(n_t-1))*self.prim['di']/dist
    def r_geo(self, _of_primary=True, rho=17e-10):
        """
            return the value of the resistance of the described transformer
        """
        if _of_primary:
            geo = self.prim
        else:
            geo = self.second
        n_t = geo['n_turn']
        height = geo['height']
        l_tot = 8*np.tan(np.pi/8)*n_t*(geo['di']+geo['width']+(n_t-1)*(geo['width']+geo['gap']))
        r_dc = rho*l_tot/(geo['width']*height)
        skin_d = np.sqrt(rho/(u0*self.freq*np.pi))
        r_ac = rho*l_tot/((1+height/geo['width'])*skin_d*(1-np.exp(-height/skin_d)))
        return r_dc + r_ac
    def generate_spice_model(self, k_ind):
        """
            Generate a equivalent circuit of a transformer with the given values
        """
        return f'Transformer Model\n\n\
L1		IN	1	{self.model["lp"]*1e12:.1f}p\n\
R1		1	OUT	{self.model["rp"]*1e3:.1f}m\n\
L2		CPL	2	{self.model["ls"]*1e12:.1f}p\n\
R2		2	ISO	{self.model["rs"]*1e3:.1f}m\n\
K		L1	L2	{k_ind:.3n}\n\
CG1		IN	0	{self.model["cg"]*1e15/4:.1f}f\n\
CG2		OUT	0	{self.model["cg"]*1e15/4:.1f}f\n\
CG3		ISO	0	{self.model["cg"]*1e15/4:.1f}f\n\
CG4		CPL	0	{self.model["cg"]*1e15/4:.1f}f\n\
CM1		IN	CPL	{self.model["cm"]*1e15/2:.1f}f\n\
CM2		ISO	OUT	{self.model["cm"]*1e15/2:.1f}f\n\n'
