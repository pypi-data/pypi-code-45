evil = '/usr/local/lib/python2.7/site-packages/GDAL-2.0.0-py2.7-linux-x86_64.egg'
import sys

if evil in sys.path:
    del sys.path[sys.path.index(evil)]

import os
from pyroSAR import identify
from pyroSAR.gamma import geocode
from pyroSAR.gamma.srtm import dem_autocreate

# filename = '/home/john/Desktop/S1_proc_test/S1A_IW_GRDH_1SDV_20150426T190111_20150426T190136_005659_00741C_FFB7.zip'
filename = '/geonfs01_vol3/swos/data/sentinel1/GRD/S1A_IW_GRDH_1SDV_20150426T190111_20150426T190136_005659_00741C_FFB7.zip'

outdir = '/geonfs01_vol1/ve39vem/test/dem_test'

id = identify(filename)

demfiles = {}
for demType in ['AW3D30', 'SRTM 1Sec HGT', 'SRTM 3Sec']:
    dem_id = demType.replace(' ', '-')
    dem_base = 'demfile_gamma_{}'.format(dem_id)
    dem = os.path.join(outdir, dem_base)
    print(demType)
    with id.bbox() as bbox:
        dem_autocreate(geometry=bbox, demType=demType, outfile=dem)
    demfiles[dem_id] = dem

os.environ['OMP_NUM_THREADS'] = '6'

for dem_id, dem_file in demfiles.items():
    scenedir = os.path.join(outdir, '{}_{}'.format(id.outname_base(), dem_id))
    geocode(scene=id, dem=dem,
            tempdir=os.path.join(scenedir, 'process'), outdir=scenedir,
            targetres=90, scaling='db')



from pyroSAR.snap import geocode

geocode(infile=id, outdir=os.path.join(outdir, 'snap'), test=True)
