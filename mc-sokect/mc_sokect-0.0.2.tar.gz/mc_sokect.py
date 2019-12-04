import socket
import sys
import random
import _thread
import time
import struct
import json
import subprocess
import datetime
from urllib.request import urlopen
class server:
    '''
        初始化服务端
        Args:
            port:端口号，范围从1025~65534，不写默认随机端口,类型int
            max_coon_num:最大连接数，表示此服务端最大可以连接的人数，不写默认最大连接数为：8  类型int
    '''
    def __init__(self, port: int = -1, max_conn_num: int = 8):
        print("服务端准备中，请等待。。。")
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.port = port
        self.max = max_conn_num
        self.obj = []
        self.objaddr = {}
        self.objdata = {}
        if port == -1:
            self.port = random.randint(1025, 65535)
            while self.net_is_used(self.port):
                self.port = random.randint(1025, 65535)
        if type(self.port) == int and 1024 < self.port <65535:
            if not self.net_is_used(self.port):
                self.server.bind(('',self.port)) #绑定要监听的端口
            else:
                print("端口被占用。。。。")
                sys.exit(1)
        else:
            print("端口错误。。。。")
            sys.exit(1)
        print("欢迎使用魔扣少儿编程Python网络服务端，服务端创建完成。")
    def net_is_used(self, port, ip='127.0.0.1'):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((ip,port))
            s.shutdown(2)
            return True
        except:
            return False
    #获取外网IP
    def GetOuterIP(self):
        return json.load(urlopen('https://api.ipify.org/?format=json'))['ip']
        pass
    def start(self):
        '''
        开启服务器
        '''
        print("服务端开始启动。。。")
        self.Connect()
        _thread.start_new_thread(self.Accept,())
        time.sleep(1)
        print("服务端启动成功。。。")
        print("服务端信息如下：\n   内网ip:",socket.gethostbyname(socket.getfqdn(socket.gethostname()))+'\n   外网ip: '+self.GetOuterIP(),"\n   端口:",self.port)
        print("把你的ip和端口告诉你的魔扣小伙伴就可以连接了哦！")
        pass
    def Connect(self):
        self.server.listen(self.max)
        print("开始监听客户端。。。")
        pass
    def Accept(self):
        print("开始等待客户端连接。。。")
        while True:
            onn,addr = self.server.accept()
            #self.obj.append(onn)
            self.objaddr[onn] = addr
            _thread.start_new_thread(self.Updata,(onn,))
            #_thread.start_new_thread(self.Updata,(onn,))
            print("客户端已连接,ip:", onn.getsockname()[0])
    def Updata(self, coon: socket.socket):
        while True:
            try:
                cmd = coon.recv(1024).decode("utf-8")
                #self.objdata[temp[0]] = temp[1]
                temp = json.loads(cmd)
                self.objdata[temp[0]] = temp[1]
                #p = subprocess.Popen(cmd,shell=False,stdout=-1,stderr=-1)
                
                # data与err_data都是采用的系统编码，windows是GBK
                #---------------------------
                #data = p.stdout.read()
                #print('aaa:',data)
                #----------------------------
                #err_data = p.stderr.read()
                #print(err_data)
                # 计算真实数据长度
                length = len(self.objdata)


                # 在发送数据之前发送额外的信息
                #t = "{执行时间:%s 真实数据长度:%s" % (datetime.datetime.now(),length)
                # 把要发送的数据先存到字典中
                t = {}
                t["time"] = str(datetime.datetime.now())
                t["size"] = length
                t["filename"] = "Hugn"

                t_json = json.dumps(t) # 得到json格式字符串
                t_data = t_json.encode("utf-8") # 将json转成了字节
                t_length = struct.pack("i",len(t_data))

                # 1.先发送额外信息的长度
                coon.send(t_length)
                # 2.发送额外信息
                coon.send(t_data)
                # 3.发送真实数据
                cmd = json.dumps(self.objdata)
                coon.send(cmd.encode('utf-8'))
                #coon.send(err_data)
            except:
                print("客户端ip:",coon.getsockname()[0]," 以断开连接")
                #self.obj.remove(coon)
                break
            

class client:
    '''
    初始化客户端
    Args:
        server_ip:所连接的服务端ip，类型str
        server_port:所连接的服务端端口，类型int
        my_name:网络ID，客户端名称，用于区分用户
    '''
    def __init__(self, server_ip, server_port, my_name: str):
        print("客户端准备中，请等待。。。")
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_ip = server_ip
        self.server_port = server_port
        self.my_name = my_name
        self.msg=None
        self.obj = None
        self.dT = 0
        print("欢迎使用魔扣少儿编程Python网络客户端，客户端创建完成。")
    def start(self):
        
            self.client.connect((self.server_ip,self.server_port))
            print("客户端已连接到ip:",self.server_ip,"  端口:",self.server_port)
            _thread.start_new_thread(self.receive,())
        
    def send(self, msg):
        '''
        向服务器发送数据
        Args:
            msg:想要发送的数据(任意类型)
        '''
        self.msg = msg
        pass
    def GetMsg(self):
        '''
        获取服务器发送的信息
        '''
        return self.obj
        pass
    def receive(self):
        while True:
            if self.msg != None:
                temp = json.dumps([self.my_name,self.msg])
                self.client.send(temp.encode('utf-8'))
                self.msg = None
                # 1.接收的是额外信息的长度
                length = self.client.recv(4)
                len_data = struct.unpack("i",length)[0] # 转换为整型

                # 2.接收额外信息
                t_data = self.client.recv(len_data)
                #print(t_data.decode("utf-8"))

                json_dic = json.loads(t_data.decode("utf-8"))
                #print("执行时间:%s" % json_dic["time"])

                data_size = json_dic["size"] # 得到数据长度
                self.dT = json_dic["time"]
                #data_len = json_dic["datalen"]
                all_data = b'' # 存储已接收数据
                rcv_size = 0 # 已接收长度
                # 接收真实数据
                # 循环接收 直到 接收到的长度等于总长度
                while  rcv_size < data_size:
                    data = self.client.recv(1024)
                    rcv_size += len(data)
                    all_data += data

                #print("接收长度%s" % rcv_size)
                all_data = json.loads(all_data.decode("gbk"))
                self.obj = all_data