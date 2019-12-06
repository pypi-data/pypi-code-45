def write_dataframe_to_csv_on_s3(dataframe, filename, **kwarg):
    """ Write a dataframe to a CSV on S3 """
    print("Writing {} records to {}".format(len(dataframe), filename))
    path = 'tmp/out.csv'
    dataframe.to_csv(path, sep=";", index=False, decimal = ',', encoding='ISO-8859-1', **kwarg)
    s3_resource = boto3.resource("s3")
    s3_resource.Object('krotonanalytics', filename).upload_file(path)
    print('Done')

def write_dataframe_on_s3(dataframe, filename, parquet=False, **kwarg):
    """ Write a dataframe to a CSV on S3 """
    print("Writing {} records to {}".format(len(dataframe), filename))
    path = 'tmp/out.csv'
    if parquet:
        dataframe.to_parquet(path, index=False, **kwarg)
    else:
        dataframe.to_csv(path, sep=";", index=False, decimal = ',', encoding='ISO-8859-1', **kwarg)
    s3_resource = boto3.resource("s3")
    s3_resource.Object('krotonanalytics', filename).upload_file(path)
    print('Done')
    
def save_partitions(df, filter_dict):
    filter_acumulator = pd.Series(data=False, index=df.index)
    filter_counter = 0
    for file, data_filter in filter_dict.items():

        filter_acumulator = filter_acumulator | data_filter
        filter_counter += data_filter.sum()

    dataframe_list = []
    if filter_acumulator.all() and (filter_counter == df.shape[0]):
        for file, data_filter in filter_dict.items():
            df_output = df[data_filter].copy()
            write_dataframe_to_csv_on_s3(df_output, file)
            dataframe_list.append(df_output)
        return dataframe_list
    else:
        display(filter_acumulator)
        print(filter_counter)
        print(df.shape[0])
        raise Exception('Filters are not a perfect partition')