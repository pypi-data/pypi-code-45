# -*- coding: utf-8 -*-
import networkx as nx

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os
import tkinter
from tkinter import messagebox

from core import Router, Event, Tools


class Gui(object):

    def __init__(self, master, log):
        self.master = master

        self.log = log
        # 全界面
        self.maxFrame = tkinter.Frame(master)
        self.maxFrame.pack(fill=tkinter.BOTH, expand=1, padx=1, pady=1)
        # 左侧控制区域

        # self.LFrame = tkinter.LabelFrame(self.maxFrame, font=18, padx=1, pady=1)
        # self.LFrame.pack(side=tkinter.LEFT)
        # 左侧控制区域
        self.fm1 = tkinter.Frame(self.maxFrame)
        self.fm1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)

        self.leftFrame = tkinter.LabelFrame(self.fm1, font=18, padx=1, pady=1)
        self.leftFrame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=tkinter.YES)

        # 图像
        # self.imageFrame=tkinter.Frame(self.fm1)
        self.imageFrame = tkinter.LabelFrame(self.fm1, font=18, padx=1, pady=1)
        self.imageFrame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)

        # 路由创建区域

        self.image_lable = tkinter.Label(self.imageFrame)
        self.image_lable.pack()
        if os.path.exists("ba.png"):
            self.tk_image = tkinter.PhotoImage(file="ba.png")
            self.image_lable.config(image=self.tk_image)

        self.routerGenerate = tkinter.Button(self.leftFrame, text='生成拓扑网络', font=18, padx=20, pady=5)
        self.routerGenerate.grid(row=6, column=0, pady=5, columnspan=2)

        tkinter.Label(self.leftFrame, text='更新路由表', font=18).grid(row=7, column=0, sticky='W', pady=5)
        self.routerUpdate = tkinter.Button(self.leftFrame, text='更新全部路由', font=18, padx=20, pady=5)
        self.routerUpdate.grid(row=8, column=0, pady=5, columnspan=2)
        self.routerUpdateStep = tkinter.Button(self.leftFrame, text='更新下一路由', font=18, padx=20, pady=5)
        self.routerUpdateStep.grid(row=8, column=2, pady=5, columnspan=2)
        # 故障模拟区域
        tkinter.Label(self.leftFrame, text='模拟网络故障', font=18).grid(row=9, column=0, sticky='W', pady=5)
        tkinter.Label(self.leftFrame, text='故障网络名称：', font=16).grid(row=10, column=0, sticky='W', pady=5)
        self.routerFault = tkinter.Entry(self.leftFrame, justify=tkinter.CENTER)
        self.routerFault.grid(row=10, column=1)
        self.faultStart = tkinter.Button(self.leftFrame, text='故障', font=18, padx=20, pady=5)
        self.faultStart.grid(row=11, column=0, pady=5, columnspan=2)
        tkinter.Label(self.leftFrame, text='', font=18).grid(row=12, column=0, sticky='W', pady=5)
        tkinter.Label(self.leftFrame, text='', font=18).grid(row=13, column=0, sticky='W', pady=5)

        # 路由信息显示界面
        self.routeInfoFrame = tkinter.LabelFrame(self.maxFrame, font=18, padx=1, pady=1)
        self.routeInfoFrame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)
        tkinter.Label(self.routeInfoFrame, text='路由表信息', font=16).pack()
        self.routeShowArea = tkinter.Scrollbar(self.routeInfoFrame)
        self.routeShowArea.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.routeData = tkinter.Text(self.routeInfoFrame, width=60, height=18, font=16, state=tkinter.DISABLED,
                                      yscrollcommand=self.routeShowArea.set)
        self.routeData.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.routeShowArea.config(command=self.routeData.yview)

        # 日志信息显示界面
        self.logFrame = tkinter.LabelFrame(self.maxFrame, padx=1, pady=1)
        self.logFrame.pack()
        tkinter.Label(self.logFrame, text='操作日志', font=16).pack()
        self.logShowArea = tkinter.Scrollbar(self.logFrame)
        self.logShowArea.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.logData = tkinter.Text(self.logFrame, width=60, height=13, font=16, state=tkinter.DISABLED,
                                    yscrollcommand=self.logShowArea.set)
        self.logData.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.logShowArea.config(command=self.logData.yview)
        # 按钮功能绑定
        self.event_bound()

    def event_bound(self):
        # 添加路由按钮
        # self.routerAdd.bind('<ButtonRelease-1>', self.add_button)
        self.routerGenerate.bind('<ButtonRelease-1>', self.generate_network)
        # 更新路由表按钮
        self.routerUpdate.bind('<ButtonRelease-1>', self.update_button)

        self.routerUpdateStep.bind('<ButtonRelease-1>', self.update_step_button)
        # 设置故障按钮
        self.faultStart.bind('<ButtonRelease-1>', self.fault_button)
        # 距离下拉框
        # self.routerDistance.bind("<<ComboboxSelected>>", self.set_router_next)
        # 退出时保存日志
        self.master.protocol('WM_DELETE_WINDOW', self.save_log_event)

    def set_router_next(self, event):
        # 距离下拉框选择1时，设置下一跳为*
        if self.routerDistance.get() == '1':
            self.EntryData = tkinter.StringVar()
            self.routerNext = tkinter.Entry(self.leftFrame, justify=tkinter.CENTER,
                                            textvariable=self.EntryData, state='readonly')
            self.EntryData.set('*')
            self.routerNext.grid(row=5, column=1)
        else:
            self.routerNext = tkinter.Entry(self.leftFrame, justify=tkinter.CENTER)
            self.routerNext.grid(row=5, column=1)

    def update_button(self, event):
        # 发送按钮功能绑定
        # 如果没有路由表
        if len(os.listdir(Router.ROOT_ROUTER_PATH)) == 0:
            messagebox.showinfo('警告', '不存在路由表，无法发送!')
            return
        Event.update_router(log_show=self.logData, router_show=self.routeData)

    def update_step_button(self, event):
        # 发送按钮功能绑定
        # 如果没有路由表
        if len(os.listdir(Router.ROOT_ROUTER_PATH)) == 0:
            messagebox.showinfo('警告', '不存在路由表，无法发送!')
            return
        Event.update_step_router(log_show=self.logData, router_show=self.routeData)

    def add_button(self, event):
        # 添加按钮功能绑定
        # 输入为空
        if (self.routerName.get().strip() == '') or \
                (self.routerTarget.get().strip() == '') or \
                (self.routerTarget.get().strip() == '') or \
                (self.routerNext.get().strip() == ''):
            return
        Event.add_router(log_show=self.logData, router_show=self.routeData,
                         name=self.routerName.get(), ip=self.routerIp.get(),
                         target=self.routerTarget.get(), distance=self.routerDistance.get(),
                         next=self.routerNext.get())

    def fault_button(self, event):
        # 故障按钮功能绑定
        # 如果没有路由表
        if len(os.listdir(Router.ROOT_ROUTER_PATH)) == 0:
            messagebox.showinfo('警告', '不存在路由表，无法发送!')
            return
        # 判断网络是否存在
        sign = 0  # 标志位
        for router_list in Tools.get_all_router_list(Router.ROOT_ROUTER_PATH):
            if self.routerFault.get() in [router_info['target'] for router_info
                                          in router_list.get_router_info()]:
                sign = 1
                break
        if sign == 0:
            messagebox.showinfo('警告', '此网络不存在，无法进行故障测试!')
            return
        Event.fault_test(log_show=self.logData, router_show=self.routeData,
                         fault=self.routerFault.get())

    def save_log_event(self):
        # 保存日志
        Tools.save_log(log_data=self.routeData, log=self.log)
        # 关闭窗口
        self.master.destroy()

    def generate_network(self, event):

        # clf()  # 清图。
        # cla()  # 清坐标轴。
        # close()  # 关窗口
        plt.cla()

        # G = fat_tree_topo()
        # nx.draw(G,pos = nx.random_layout(G),node_color = 'b',edge_color = 'r',with_labels = False,font_size =18,node_size =20)
        # nx.draw(G,pos = nx.spring_layout(G),node_color = 'b',edge_color = 'r',with_labels = False,font_size =18,node_size =20)
        # nx.draw(G,pos = nx.circular_layout(G),node_color = 'b',edge_color = 'r',with_labels = False,font_size =18,node_size =20)
        # nx.draw(G,pos = nx.shell_layout(G),node_color = 'b',edge_color = 'r',with_labels = False,font_size =18,node_size =20)
        # nx.draw(topo, with_labels=True)

        # G = nx.petersen_graph()
        # G = nx.tutte_graph()
        G = nx.erdos_renyi_graph(16, 0.15)
        # G = nx.watts_strogatz_graph(30, 3, 0.1)
        # G = nx.barabasi_albert_graph(17, 1)
        # G = nx.random_lobster(17, 0.9, 0.9)
        from networkx.drawing.nx_agraph import write_dot, graphviz_layout

        pos = graphviz_layout(G, prog='dot')
        # nx.draw(G, pos=pos, node_color='b', edge_color='r', with_labels=True, font_size=18, node_size=20)

        ip = "127.0.0.1"
        start_port = 8080
        labels = {}
        # letter = 97
        letter = "R"
        # 设置节点信息
        for i in range(list(G.nodes).__len__()):
            port = start_port + i
            # name = chr(letter + i).upper()
            name = letter + str(i)
            ip_address = ip + ":" + str(port)
            labels[i] = name + "/" + str(port)
            G.add_node(1)
            G.nodes[i]['ip_address'] = ip + ":" + str(port)
            G.nodes[i]['router_name'] = name
            print(G.nodes[i])
            # print(G.neighbors(G.nodes[i]))
            print(G[i])
        Router.remove_route_file(Router.ROOT_ROUTER_PATH)
        for i in range(list(G.nodes).__len__()):
            port = start_port + i
            # name = chr(letter + i).upper()
            name = letter + str(i)
            ip_address = ip + ":" + str(port)
            # 获取所有节点的边，并生成路由表
            # 删除路由器

            # 创建一个路由器实例
            router = Router.Router(name=name, ip_address=ip_address)
            # 添加自己
            router.get_router_list().add_router_info(data={'target': ip_address,
                                                           'distance': str(0),
                                                           'next': "*"})
            for k in G[i].keys():
                # 向此路由表添加一条新路由信息
                router.get_router_list().add_router_info(data={'target': G.nodes[k]["ip_address"],
                                                               'distance': str(1),
                                                               'next': G.nodes[k]["router_name"]})
            # 保存此路由表
            router.get_router_list().save_router_list()

        # labels=dict((i, chr(97+i).upper()) for i in  range(list(G.nodes).__len__()))
        # nx.draw(G, pos=nx.shell_layout(G), node_color='b', edge_color='r', labels=labels,with_labels=False, font_size=18, node_size=40)

        nx.draw(G, pos=pos, node_color='b', edge_color='r', labels=labels, with_labels=True, font_size=10, node_size=18)
        # plt.figure(figsize=fs, dpi=dpi_set)
        # plt.rcParams['figure.figsize'] = (8.0, 4.0)
        plt.savefig("ba.png")
        # plt.show()
        # self.image_lable.config(image=self.tk_image)
        # self.image_lable.image=self.tk_image
        # self.tk_image = tkinter.PhotoImage(file="ba.png")
        self.show_image()

    def show_image(self):
        w_box = 600
        h_box = 400
        try:
            # pil_image = Image.open("/Users/zengcd/Desktop/SocketRIP/ba.png")
            # w, h = pil_image.size
            # pil_image_resized = self.resize(w, h, w_box, h_box, pil_image)
            # tk_image = ImageTk.PhotoImage(pil_image)
            # tk_image = tkinter.PhotoImage(file="ba.png")
            # image_lable = tkinter.Label(self.imageFrame, image=self.tk_image, text="Inside the LabelFrame")
            # image_lable.pack()

            self.tk_image = tkinter.PhotoImage(file="ba.png")
            self.image_lable.config(image=self.tk_image)
            # self.maxFrame.update()
            # self.image_lable.config(image=self.tk_image)
            # image_lable.grid(row=2, sticky='W', pady=0)  # 把图片整合到标签类中
        except Exception as e:
            print(e)

    def resize(self, w, h, w_box, h_box, pil_image):
        '''
        resize a pil_image object so it will fit into
        a box of size w_box times h_box, but retain aspect ratio
        对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
        '''
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)
