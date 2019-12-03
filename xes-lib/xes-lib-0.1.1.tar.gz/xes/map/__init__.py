from xes.map import map

'''
名 称: get_routes
功 能: 获取公交线路
参数1: 起点地址, 类型: string
参数2: 终点地址, 类型: string
返回值：线路列表, 类型: list
'''
get_routes = map.get_routes


'''
名 称: get_sites
功 能: 获取公交线路站点
参数1: 线路列表, 类型: list
参数2: 索引值, 类型: int
返回值：站点列表, 类型: list
'''
get_sites = map.get_sites