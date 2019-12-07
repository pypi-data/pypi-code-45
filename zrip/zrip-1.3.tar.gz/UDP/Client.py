# -*- coding: utf-8 -*-
import socket
import json


class Client(object):
    # 客户端类
    def __init__(self, **params):
        # ip地址
        self.address = (params['host'], int(params['port']))
        # 缓冲区大小
        self.buf_size = params['buf_size']
        # 创建连接
        self.udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_client.connect(self.address)

    def upload_data(self, data, save_path):
        # 上传文件
        io_list = (save_path, data)
        json_list = json.dumps(io_list)
        # self.udp_client.sendto(json_list.encode(), self.address)
        self.udp_client.send(json_list.encode())
        return True

    def close(self):
        # 关闭连接
        self.udp_client.close()

