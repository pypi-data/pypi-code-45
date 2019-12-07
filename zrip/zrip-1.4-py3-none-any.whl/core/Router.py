# -*- coding: utf-8 -*-

import UDP.Sever
import UDP.Client
import os


# 路由器根目录
from core import RouterList

ROOT_ROUTER_PATH = os.getcwd()+'/ROUTER'


class Router(object):
    # 路由器类
    def __init__(self, **params):
        # ip地址
        self.ip_address = params['ip_address']
        # 路由器名
        self.router_name = params['name']

        if not os.path.exists(ROOT_ROUTER_PATH):
            os.mkdir(ROOT_ROUTER_PATH)
        # 如果路由器不存在，则创建
        if not os.path.exists(os.path.join(ROOT_ROUTER_PATH,self.ip_address.split(':')[0]+' '+self.ip_address.split(':')[1])):
            os.mkdir(os.path.join(ROOT_ROUTER_PATH,self.ip_address.split(':')[0]+' '+self.ip_address.split(':')[1]))
        # 路由表
        self.router_list = RouterList.RouterList(os.path.join(ROOT_ROUTER_PATH,
                                                           self.ip_address.split(':')[0] + ' ' +
                                                           self.ip_address.split(':')[1]
                                                           ,self.router_name+'.rl'))
        # 路由器路径
        self.path = os.path.join(ROOT_ROUTER_PATH,self.ip_address.split(':')[0]+' '+self.ip_address.split(':')[1])





    def get_router_name(self):
        # 获取路由器名
        return self.router_name

    def get_router_path(self):
        # 获取路由器路径
        return self.path

    def get_router_ip_address(self):
        # 获取路由器ip地址
        ip_port = (self.ip_address.split(':')[0], int(self.ip_address.split(':')[1]))
        return ip_port

    def get_router_list(self):
        # 获取路由表
        return self.router_list

    def get_near_router(self, all_near_router):
        # 获取相邻路由器列表
        return all_near_router[self.router_name]

    def send_router_list(self, **params):
        # 发送路由表
        '''
        param params: sever-服务端连接  host-服务端ip  port-服务端端口　 path-上传文件保存路径 
        '''
        send_client = UDP.Client.Client(host=params['host'],
                                        port=params['port'], buf_size=1024)
        data = [router_info['target']+'  '+router_info['distance']+'  '+router_info['next']
                for router_info in self.router_list.set_send_router_info()]
        try:
            if send_client.upload_data('\n'.join(data), params['path']):
                send_client.close()
        except Exception as e:
            print("端口："+params['port'])
            print(e)

        params['sever'].handle_request()

    def getDistance(self,router_list,target):
        #根据name获得ip:port
        for router in router_list:
            if router['target']==target:
                return router['distance']
        pass
    def update_router_list(self):
        # 更新路由表
        for other_router_list in [RouterList.RouterList(os.path.join(self.path,router_list))
                                  for router_list in os.listdir(self.path)
                                  if not os.path.basename(router_list).split('.')[0] == self.router_name]:
            for other_router_info in other_router_list.get_router_info():
                for self_router_info in self.router_list.get_router_info():
                    sign = 0  # 标志位
                    # 目的网络相同
                    if other_router_info['target'] == self_router_info['target']:
                        # 下一跳相同
                        if other_router_info['next'] == self_router_info['next']:
                            # 更新
                            self_router_info['distance'] = other_router_info['distance']
                            sign = 1
                            break
                        # 下一跳不同
                        else:
                            # 距离小于原表
                            if int(other_router_info['distance']) < int(self_router_info['distance']):
                                # 更新
                                self_router_info['distance'] = int(other_router_info['distance'])
                                self_router_info['next'] = other_router_info['next']
                                sign = 1
                                break
                            # 距离不小于原表
                            else:
                                # 不变
                                sign = 1
                                break
                    else:
                        pass
                # 原表中没有此目的网络
                if sign == 0:
                    # 添加
                    self.router_list.add_router_info(other_router_info)
            # 删除其他路由表
            os.remove(other_router_list.get_router_list_path())
        # 保存路由表
        self.router_list.save_router_list()

def remove_route_file(path):
    # path=ROOT_ROUTER_PATH
    if os.path.exists(path):
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                remove_route_file(path_file)
