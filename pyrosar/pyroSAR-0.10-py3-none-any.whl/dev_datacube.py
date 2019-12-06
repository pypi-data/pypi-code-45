import os
from pyroSAR.datacube_util import Product, Dataset
from pyroSAR.ancillary import groupby, find_datasets

# define a directory containing processed SAR scenes
dir = '/home/john/Desktop/sites/Spain_Donana/proc_out'

maindir = '/home/john/Desktop/odc_test'

# define a name for the product YML; this is used for creating a new product in the datacube
yml_product = os.path.join(maindir, 'product_def.yml')

# define a directory for storing the indexing YMLs; these are used to index the dataset in the datacube
yml_index_outdir = os.path.join(maindir, 'yml_indexing')

# define a name for the ingestion YML; this is used to ingest the indexed datasets into the datacube
yml_ingest = os.path.join(maindir, 'ingestion.yml')

# product description
product_name_indexed = 'S1_GRD_index'
product_name_ingested = 'S1_GRD_ingest'
product_type = 'gamma0'
description = 'this is just some test'

# define the units of the dataset measurements (i.e. polarizations)
units = 'backscatter'
# alternatively this could be a dictionary:
# units = {'VV': 'backscatter VV', 'VH': 'backscatter VH'}

ingest_location = os.path.join(maindir, 'ingest')

# find pyroSAR files by metadata attributes
files = find_datasets(dir, recursive=True, sensor=('S1A', 'S1B'), acquisition_mode='IW')

# group the found files by their file basenames
# files with the same basename are considered to belong to the same dataset
grouped = groupby(files, 'outname_base')

print(len(files))
print(len(grouped))

# create a new product and add the collected datasets to it
# alternatively, an existing product can be used by providing the corresponding product YML file
with Product(name=product_name_indexed,
             product_type=product_type,
             description=description) as prod:
    for dataset in grouped:
        with Dataset(dataset, units=units) as ds:
            # add the datasets to the product
            # this will generalize the metadata from those datasets to measurement descriptions,
            # which define the product definition
            prod.add(ds)

            # parse datacube indexing YMLs from product and dataset metadata
            prod.export_indexing_yml(ds, yml_index_outdir)

    # write the product YML
    prod.write(yml_product)

    # print the product metadata, which is written to the product YML
    print(prod)

with Product(yml_product) as prod:
    prod.export_ingestion_yml(yml_ingest, product_name_ingested, ingest_location)


# datacube product add product_def.yml
# datacube dataset add yml_indexing/*

# note: the following failed at first with the message "Failed to load requested storage driver: NetCDF CF"
# a list of available drivers can be queried by datacube.drivers.writer_drivers()
# this issue was solved by first uninstalling datacube,
# installing gdal (which was installed together with datacube as its dependency and thus removed during uninstallation)
# and then installing datacube again

# datacube ingest -c ingestion.yml
