"""
Author: "Rangana Warshamanage, Garib N. Murshudov"
MRC Laboratory of Molecular Biology
    
This software is released under the
Mozilla Public License, version 2.0; see LICENSE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
from timeit import default_timer as timer
import numpy as np
import fcodes_fast
from emda.iotools import read_map,write_mrc,resample2staticmap
from emda.mapfit.utils import remove_unwanted_corners
import emda.plotter
from emda.config import *

#debug_mode = 1 # 0: no debug info, 1: debug

class EmmapOverlay:
    
    def __init__(self,hfmap_list, mask_list=None):
        self.hfmap_list         = hfmap_list
        self.mask_list          = mask_list
        self.map_unit_cell      = None
        self.map_origin         = None
        self.map_dim            = None
        #
        self.ceo_lst            = None
        self.cbin_idx           = None
        self.cdim               = None
        self.cbin               = None

    def load_maps(self):
        from scipy import ndimage
        from scipy.ndimage.interpolation import shift
        #import fcodes_fast
        # read mask and map
        fhf_lst = []
        if self.mask_list is not None:
            if len(self.hfmap_list) != len(self.mask_list):
                print('map_list and mask_list must have the same size!')
                print('exiting program...')
                exit()
            for i in range(len(self.mask_list)):
                _,mask,_ = read_map(self.mask_list[i])
                uc,arr,origin = read_map(self.hfmap_list[i])
                if i == 0: 
                    com1 = ndimage.measurements.center_of_mass(arr * mask)
                    print('COM: ', com1)
                    nx, ny, nz = arr.shape
                    box_centr = (nx//2, ny//2, nz//2)
                    print(box_centr)
                    self.com1 = com1
                    self.box_centr = box_centr
                    map_origin = origin
                    uc_target = uc
                    target_dim = arr.shape
                    target_pix_size = uc_target[0]/target_dim[0]
                    corner_mask = remove_unwanted_corners(uc,target_dim)
                    arr_mask = shift(arr * mask, np.subtract(box_centr,com1))
                    fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_mask * corner_mask))))
                else:
                    mask = resample2staticmap(target_pix_size,target_dim,uc,mask)
                    arr = resample2staticmap(target_pix_size,target_dim,uc,arr)                
                    com1 = ndimage.measurements.center_of_mass(arr * mask) 
                    print('COM: ', com1)            
                    arr_mask = shift(arr * mask, np.subtract(box_centr,com1))                  
                    fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_mask * corner_mask))))

            # free memory
            del arr, arr_mask, mask
            del corner_mask
            #
            self.map_origin     = map_origin
            self.map_unit_cell  = uc_target
            self.map_dim        = target_dim 
            self.fhf_lst        = fhf_lst 

        if self.mask_list is None: 
            for i in range(len(self.hfmap_list)):
                uc,arr,origin = read_map(self.hfmap_list[i])
                if i == 0:
                    com1 = ndimage.measurements.center_of_mass(arr)
                    print('COM: ', com1)
                    nx, ny, nz = arr.shape
                    box_centr = (nx//2, ny//2, nz//2)
                    print(box_centr)
                    self.com1 = com1
                    self.box_centr = box_centr
                    map_origin = origin
                    uc_target = uc
                    target_dim = arr.shape
                    target_pix_size = uc_target[0]/target_dim[0]
                    arr = shift(arr, np.subtract(box_centr,com1)) 
                    #print('COM after centering: ', ndimage.measurements.center_of_mass(arr))
                    fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr))))
                else:
                    arr = resample2staticmap(target_pix_size,target_dim,uc,arr)
                    com1 = ndimage.measurements.center_of_mass(arr)
                    print('COM: ', com1)
                    arr = shift(arr, np.subtract(box_centr,com1)) 
                    #print('COM after centering: ', ndimage.measurements.center_of_mass(arr))
                    fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr))))
                
            # free memory
            del arr
            #            
            self.map_origin     = map_origin
            self.map_unit_cell  = uc_target
            self.map_dim        = target_dim 
            self.fhf_lst        = fhf_lst 

    def calc_fsc_from_maps(self):  
        # function for only two maps fitting
        import fcodes_fast
        nmaps = len(self.fhf_lst) 
        fFo_lst = []
        fEo_lst = []
        fBTV_lst = []
        #
        nx,ny,nz = self.fhf_lst[0].shape
        maxbin = np.amax(np.array([nx//2,ny//2,nz//2]))
        self.nbin,res_arr,self.bin_idx = fcodes_fast.resolution_grid(
            self.map_unit_cell,debug_mode,maxbin,nx,ny,nz)
        self.res_arr = res_arr[:self.nbin]
        #
        for i in range(nmaps): 
            fo,eo,_,_,totalvar,_ = fcodes_fast.calc_fsc_using_halfmaps(
                self.fhf_lst[i],self.fhf_lst[i],self.bin_idx,self.nbin,debug_mode,nx,ny,nz)  
            fFo_lst.append(fo)
            fEo_lst.append(eo)
            fBTV_lst.append(totalvar)
        #
        self.fo_lst            = fFo_lst
        self.eo_lst            = fEo_lst
        self.totalvar_lst      = fBTV_lst



class EmmapAverage:
    
    def __init__(self,hfmap_list, mask_list=None):
        self.hfmap_list         = hfmap_list
        self.mask_list          = mask_list
        self.map_unit_cell      = None
        self.map_origin         = None
        self.map_dim            = None
        self.resol_rand         = 10.0 # resolution (A) for phase randomisation
        #
        self.ceo_lst            = None
        self.cbin_idx           = None
        self.cdim               = None
        self.cbin               = None

    def load_maps(self):
        from scipy import ndimage
        from scipy.ndimage.interpolation import shift
        from emda.fsc_true_from_phase_randomize import get_randomized_sf
        import fcodes_fast
        # read masks
        fhf_lst = []
        unmask_fhf_lst = []
        phrand_fhf_lst = []
        if self.mask_list is not None:
            if len(self.hfmap_list) != len(self.mask_list):
                print('hfmap_list and mask_list must have the same size!')
                print('exiting program...')
                exit()
            mask_lst = []
            for i in range(0,len(self.mask_list),2):
                _,mask,_ = read_map(self.mask_list[i])
                mask_lst.append(mask) # for hfmap1 & hfmap2

            for i in range(0,len(self.hfmap_list),2):
                uc,arr1,origin = read_map(self.hfmap_list[i])
                uc,arr2,origin = read_map(self.hfmap_list[i+1])
                if i == 0: 
                    com1 = ndimage.measurements.center_of_mass(arr1 * mask_lst[0])
                    nx, ny, nz = arr1.shape
                    box_centr = (nx//2, ny//2, nz//2)
                    print(box_centr)
                    self.com1 = com1
                    self.box_centr = box_centr
                    map_origin = origin
                    uc_target = uc
                    target_dim = arr1.shape
                    target_pix_size = uc_target[0]/target_dim[0]
                    corner_mask = remove_unwanted_corners(uc,target_dim)
                    # get resolution grid
                    maxbin = np.amax(np.array([nx//2,ny//2,nz//2]))
                    resol_grid, self.s_grid, _ = fcodes_fast.resolution_grid_full(uc,0.0,1,maxbin,nx,ny,nz)
                    #
                    for arr in [arr1, arr2]:
                        arr_unmask = arr
                        fhf1_randomized = get_randomized_sf(resol_grid,arr_unmask,self.resol_rand)
                        arr_rand = np.real(np.fft.ifftn(np.fft.ifftshift(fhf1_randomized))) * mask_lst[0]
                        arr_mask = shift(arr * mask_lst[0], np.subtract(box_centr,com1))
                        arr_unmask = shift(arr_unmask, np.subtract(box_centr,com1)) 
                        arr_rand = shift(arr_rand, np.subtract(box_centr,com1))
                        fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_mask * corner_mask))))
                        unmask_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_unmask * 
                                                                                          corner_mask))))
                        phrand_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_rand * 
                                                                                          corner_mask))))
                else:
                    run_once = True
                    for arr in [arr1, arr2]:
                        mask = resample2staticmap(target_pix_size,target_dim,uc,mask_lst[i//2])
                        arr = resample2staticmap(target_pix_size,target_dim,uc,arr)
                        arr_unmask = arr
                        fhf1_randomized = get_randomized_sf(resol_grid,arr_unmask,self.resol_rand)
                        arr_rand = np.real(np.fft.ifftn(np.fft.ifftshift(fhf1_randomized))) * mask
                        if run_once: com1 = ndimage.measurements.center_of_mass(arr * mask)
                        run_once = False
                        arr_mask = shift(arr * mask, np.subtract(box_centr,com1))
                        arr_unmask = shift(arr_unmask, np.subtract(box_centr,com1)) 
                        arr_rand = shift(arr_rand, np.subtract(box_centr,com1))
                        fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_mask * corner_mask))))
                        unmask_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_unmask * 
                                                                                          corner_mask))))
                        phrand_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_rand * 
                                                                                          corner_mask))))

            # free memory
            del mask_lst
            del arr, arr1, arr2
            del corner_mask
            #
            self.map_origin     = map_origin
            self.map_unit_cell  = uc_target
            self.map_dim        = target_dim 
            self.fhf_lst       = fhf_lst 
            self.unmask_fhf_lst = unmask_fhf_lst
            self.phrand_fhf_lst = phrand_fhf_lst

        if self.mask_list is None: 
            print('Correlation based masks will be generated and used for fitting!')
            from emda import maskmap_class
            obj_maskmap = maskmap_class.MaskedMaps()
            for i in range(0,len(self.hfmap_list),2):
                uc,arr1,origin = read_map(self.hfmap_list[i])
                uc,arr2,origin = read_map(self.hfmap_list[i+1])
                # calculate the mask
                obj_maskmap.generate_mask(arr1, arr2)
                mask = obj_maskmap.mask
                write_mrc(mask,"{0}_{1}.{2}".format('mask',str(i),'mrc'),uc,origin)
                if i == 0:
                    com1 = ndimage.measurements.center_of_mass(arr1 * mask)
                    nx, ny, nz = arr1.shape
                    box_centr = (nx//2, ny//2, nz//2)
                    print(box_centr)
                    self.com1 = com1
                    self.box_centr = box_centr
                    map_origin = origin
                    uc_target = uc
                    target_dim = arr1.shape
                    target_pix_size = uc_target[0]/target_dim[0]
                    # get resolution grid
                    maxbin = np.amax(np.array([nx//2,ny//2,nz//2]))
                    resol_grid, self.s_grid, _ = fcodes_fast.resolution_grid_full(uc,0.0,1,maxbin,nx,ny,nz)
                    #
                    for arr in [arr1, arr2]:
                        arr_unmask = arr
                        fhf1_randomized = get_randomized_sf(resol_grid,arr_unmask,self.resol_rand)
                        arr_rand = np.real(np.fft.ifftn(np.fft.ifftshift(fhf1_randomized))) * mask
                        arr_mask = shift(arr * mask, np.subtract(box_centr,com1))
                        arr_unmask = shift(arr_unmask, np.subtract(box_centr,com1)) 
                        arr_rand = shift(arr_rand, np.subtract(box_centr,com1))
                        fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_mask))))
                        unmask_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_unmask))))
                        phrand_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_rand))))
                else:
                    run_once = True
                    for arr in [arr1, arr2]:
                        mask = resample2staticmap(target_pix_size,target_dim,uc,mask)
                        arr = resample2staticmap(target_pix_size,target_dim,uc,arr)
                        arr_unmask = arr
                        fhf1_randomized = get_randomized_sf(resol_grid,arr_unmask,self.resol_rand)
                        arr_rand = np.real(np.fft.ifftn(np.fft.ifftshift(fhf1_randomized))) * mask
                        if run_once: com1 = ndimage.measurements.center_of_mass(arr * mask)
                        run_once = False
                        arr_mask = shift(arr * mask, np.subtract(box_centr,com1))
                        arr_unmask = shift(arr_unmask, np.subtract(box_centr,com1)) 
                        arr_rand = shift(arr_rand, np.subtract(box_centr,com1))
                        fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_mask))))
                        unmask_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_unmask))))
                        phrand_fhf_lst.append(np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr_rand))))
                
            # free memory
            del arr, arr1, arr2
            #            
            self.map_origin     = map_origin
            self.map_unit_cell  = uc_target
            self.map_dim        = target_dim 
            self.fhf_lst        = fhf_lst 
            self.unmask_fhf_lst = unmask_fhf_lst 
            self.phrand_fhf_lst = phrand_fhf_lst

    def calc_fsc_variance_from_halfdata(self): 
        import fcodes_fast 
        nmaps = len(self.fhf_lst) 
        fFo_lst = []
        fEo_lst = []
        fBNV_lst = []
        fBSV_lst = []
        fBTV_lst = []
        fBFsc_lst = []
        umfFo_lst = []
        umfEo_lst = []
        umfBNV_lst = []
        umfBSV_lst = []
        umfBTV_lst = []
        umfBFsc_lst = []
        #
        nx,ny,nz = self.fhf_lst[0].shape
        maxbin = np.amax(np.array([nx//2,ny//2,nz//2]))
        self.nbin,res_arr,self.bin_idx = fcodes_fast.resolution_grid(
            self.map_unit_cell,debug_mode,maxbin,nx,ny,nz)
        self.res_arr = res_arr[:self.nbin]
        idx = np.argmin((self.res_arr - self.resol_rand)**2)
        #
        for i in range(0,nmaps,2): 
            # masked data
            fo,eo,noisevar,signalvar,totalvar,bin_fsc = fcodes_fast.calc_fsc_using_halfmaps(
                self.fhf_lst[i],self.fhf_lst[i+1],self.bin_idx,self.nbin,debug_mode,nx,ny,nz) 
            full_fsc_total = 2.0 * bin_fsc / (1.0 + bin_fsc)
            # unmasked data
            umfo,umeo,umnoisevar,umsignalvar,umtotalvar,umbin_fsc = fcodes_fast.calc_fsc_using_halfmaps(
                self.unmask_fhf_lst[i],self.unmask_fhf_lst[i+1],self.bin_idx,self.nbin,debug_mode,nx,ny,nz)
            full_fsc_unmasked = 2.0 * umbin_fsc / (1.0 + umbin_fsc)
            # randomised data
            _,_,_,_,_,rbin_fsc = fcodes_fast.calc_fsc_using_halfmaps(
                self.phrand_fhf_lst[i],self.phrand_fhf_lst[i+1],self.bin_idx,self.nbin,debug_mode,nx,ny,nz)
            full_fsc_noise = 2.0 * rbin_fsc / (1.0 + rbin_fsc)

            # fsc_true from Richard's formular
            fsc_true = (full_fsc_total - full_fsc_noise) / (1 - full_fsc_noise)
            # replace fsc_true with fsc_masked_full upto resol_rand_idx + 2 (RELION uses 2)
            fsc_true[:idx+2] = full_fsc_total[:idx+2] 

            # plot various FSCs
            emda.plotter.plot_nlines(self.res_arr,
                                [full_fsc_unmasked,full_fsc_total,full_fsc_noise,fsc_true],
                                "{0}_{1}.{2}".format('fsc',str(i),'eps'),
                                ["unmasked","fsc_t","fsc_n","fsc_true"])
            
            fFo_lst.append(fo)
            fEo_lst.append(eo)
            fBNV_lst.append(noisevar)
            fBSV_lst.append(signalvar)
            fBTV_lst.append(totalvar)
            fBFsc_lst.append(fsc_true)
            #umfFo_lst.append(umfo)
            #umfEo_lst.append(umeo)
            #umfBNV_lst.append(umnoisevar)
            #umfBSV_lst.append(umsignalvar)
            #umfBTV_lst.append(umtotalvar)
            #umfBFsc_lst.append(umbin_fsc)
        #
        self.fo_lst            = fFo_lst
        self.eo_lst            = fEo_lst
        self.signalvar_lst     = fBSV_lst
        self.totalvar_lst      = fBTV_lst
        self.hffsc_lst         = fBFsc_lst
        #self.umfo_lst            = umfFo_lst
        #self.umeo_lst            = umfEo_lst
        #self.umsignalvar_lst     = umfBSV_lst
        #self.umtotalvar_lst      = umfBTV_lst
        #self.umhffsc_lst         = umfBFsc_lst
