from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
from emda.iotools import write_mrc,read_map
from emda.quaternions import get_quaternion,get_RM
from emda.mapfit.utils import double_the_axes, get_FRS
from emda.config import *

def write_mrc2(mapdata,filename,unit_cell,map_origin):
    import mrcfile as mrc
    import numpy as np
    data2write = np.real(np.fft.ifftshift(np.fft.ifftn(np.fft.ifftshift(mapdata))))
    # removing outer regions
    nx, ny, nz = data2write.shape
    assert nx == ny == nz
    dx = int(nx/4); xx = int(nx/2)
    newdata = data2write[dx:dx+xx,dx:dx+xx,dx:dx+xx]
    file = mrc.new(name=filename, data=np.float32(newdata), compression=None, overwrite=True)
    file.header.cella.x = unit_cell[0]
    file.header.cella.y = unit_cell[1]
    file.header.cella.z = unit_cell[2]
    file.header.nxstart = map_origin[0]
    file.header.nystart = map_origin[1]
    file.header.nzstart = map_origin[2]
    file.close()

def map_transform(mapname,t,r,ax,outname='translformed.mrc'):
    import emda.iotools
    import numpy as np
    from emda.quaternions import get_quaternion,get_RM
    import fcodes_fast
    uc, arr, origin = emda.iotools.read_map(mapname)
    theta = [ax,r]
    q = get_quaternion(theta)
    q = q/np.sqrt(np.dot(q,q))
    rotmat = get_RM(q)
    hf = np.fft.fftshift(np.fft.fftn(arr))
    cx,cy,cz = hf.shape
    t = (np.asarray(t)) / uc[:3]
    st,_,_,_ = fcodes_fast.get_st(cx,cy,cz,t)
    transformed_map = np.real(
                              np.fft.ifftn(
                              np.fft.ifftshift(
                              get_FRS(uc,rotmat,hf*st)[:,:,:,0])))
    emda.iotools.write_mrc(transformed_map,outname,uc,origin)
    return transformed_map

if (__name__ == "__main__"):
    mapname = '/Users/ranganaw/MRC/REFMAC/Bianka/fit/com_at_box_center/using_normalised_sf/shifted_to/static_map.mrc'
    uc,arr,origin = read_map(mapname)
    theta_init=[(0,0,1),180.0]
    q = get_quaternion(theta_init)
    q = q/np.sqrt(np.dot(q,q))
    rotmat = get_RM(q)
    arr = double_the_axes(arr)
    hf = np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr)))
    frt_full = get_FRS(uc,rotmat,hf)[:,:,:,0]
    write_mrc2(frt_full,'staticmap_z_180deg.mrc',uc,origin)