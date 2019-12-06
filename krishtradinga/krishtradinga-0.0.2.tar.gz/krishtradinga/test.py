import agrud

agrud_1 = agrud.agrud("9c2aa0-a680c6-d3d6c8-7fe643-2","5b94ef-d576cf-5615a9-b2f09b-9b5b55-1a",base_url="https://www.agrud.org/")

df1 = agrud_1.download_data("NASDAQ:AAPL","01/01/2012","01/01/2019","Price","EOD")

print(df1)