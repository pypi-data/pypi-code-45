import copy
from astropy.io import fits
import numpy as np
import re

class GrismMeta:
    def __init__(self,files):
        self.files = copy.deepcopy(files)
        self.meta = {}
        for i,ii in enumerate(files):
            self.meta[i] = {}
            self.meta[i]['ID'] = i
            self.meta[i]['FILE'] = ii
        self.make_meta()
        self.make_grismNdirect()
    def make_grismNdirect(self):
        keys = {
            'DIRECT': ['F.+'],
            'GRISM': ['G.+']
        }
        gid,did,nid = [],[],[]
        for i in self.meta:
            nchip = self.meta[i]['NCHIP']
            y = 'NONE'
            ext = None
            for j in np.arange(nchip):
                if y!='NONE':
                    continue
                string = 'FILTER'+str(j+1) if nchip > 1 else 'FILTER'
                filt = self.meta[i][string]
                for k in keys:
                    if y!='NONE':
                        continue
                    for l in keys[k]:
                        if y!='NONE':
                            continue
                        if re.search(l,filt):
                            y = k
                            ext = j
            if y=='DIRECT':
                did.append(i)
            elif y=='GRISM':
                gid.append(i)
            else:
                nid.append(i)
            self.meta[i]['EXT'] = ('SCI',ext+1)
        self.gid = copy.deepcopy(gid)
        self.did = copy.deepcopy(did)
        self.nid = copy.deepcopy(nid)
    def make_meta(self):
        keys1 = {'PRIMARY': ['TELESCOP','INSTRUME','DETECTOR'
                             ,'TARGNAME','RA_TARG','DEC_TARG'
                             ,'EXPSTART','EXPTIME','POSTARG1','POSTARG2'
                             ,'SUBARRAY'
                            ]
                }        
        keys2 = {
            ('HST','ACS','WFC'): {
                'NCHIP': 2,
                'PRIMARY': ['FILTER1','FILTER2'],
                'SCI': ['CCDCHIP','IDCSCALE','BUNIT']
            },
            ('HST','WFC3','IR'): {
                'NCHIP': 1,
                'PRIMARY': ['FILTER'],
                'SCI': ['IDCSCALE','BUNIT']
            }
        }                 
        for i in self.meta:
            x = fits.open(self.files[i])
            for j in keys1:
                for k in keys1[j]:
                    self.meta[i][k] = x[j].header[k]
            xx = (self.meta[i]['TELESCOP'],self.meta[i]['INSTRUME'],self.meta[i]['DETECTOR'])
            xxx = keys2[xx]
            nchip = xxx['NCHIP']
            self.meta[i]['NCHIP'] = copy.deepcopy(nchip)
            for j in xxx:
                if j=='NCHIP':
                    continue
                elif j=='PRIMARY':
                    for k in xxx[j]:
                        self.meta[i][k] = x[j].header[k]
                elif j=='SCI':
                    for k in xxx[j]:
                        for l in np.arange(nchip):
                            string = k+str(l+1) if nchip > 1 else k
                            self.meta[i][string] = x[j,l+1].header[k]
