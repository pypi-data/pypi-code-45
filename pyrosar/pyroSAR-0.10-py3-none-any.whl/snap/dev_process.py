import os
from pyroSAR import identify
from pyroSAR.snap import geocode
from pyroSAR.auxdata import dem_autoload

indir = '/home/john/Desktop/S1_proc_test'
outdir = '/home/john/Desktop/S1_proc_test'

# indir = '/geonfs01_vol3/swos/data/sentinel1/GRD'
# outdir = '/geonfs01_vol1/ve39vem/test/proc_snap'

scene = os.path.join(indir, 'S1A_IW_GRDH_1SDV_20150426T190111_20150426T190136_005659_00741C_FFB7.zip')

id = identify(scene)

dem_autoload([id.bbox()], demType='SRTM 1Sec HGT', buffer=0.5)

geocode(infile=scene,
        outdir=outdir,
        polarizations='VV',
        test=False,
        cleanup=False,
        removeS1BorderNoise=False,
        tr=90)
