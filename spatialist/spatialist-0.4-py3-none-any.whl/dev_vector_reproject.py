
from pyroSAR import identify

id = identify('/home/john/Desktop/S1A_IW_GRDH_1SDV_20180101T170648_20180101T170713_019964_021FFD_DA78.zip')


with id.bbox()as vec:
    print(vec)
    vec.reproject(4326)
    print(vec.convert2wkt()[0])
