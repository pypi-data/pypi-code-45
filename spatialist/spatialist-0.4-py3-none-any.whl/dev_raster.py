from spatialist import Raster

filename = '/home/john/Desktop/dem_test/S1A__IW___A_20150426T190111_VV_grd_mli_norm_geo_db.tif'
# filename = '/geonfs01_vol1/ve39vem/test/Nesrin/S1A__IW___A_20150426T190111_VV_grd_mli_norm_geo_db.tif'

with Raster(filename) as ras:
    print(ras.projection)

