import datacube

dc = datacube.Datacube()

print(dc.list_products())

# overview of all measurements (e.g. VV, VH) and their product associations
print(dc.list_measurements())

# the number of stored tiles
print(dc.index.datasets.count())

uuid = '8eb9ee0e-fbfb-4783-aa8c-4b21ca808568'

# check if dataset has already been indexed
print(dc.index.datasets.has(uuid))

# get the location of the indexing YML for this dataset
print(dc.index.datasets.get_locations(uuid))

# get all possible search keys for a product
print(dc.index.datasets.get_field_names('S1_GRD_ingest'))
