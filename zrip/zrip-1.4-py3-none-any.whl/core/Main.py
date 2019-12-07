# -*- coding: utf-8 -*-

import tkinter
import os

from core import Tools, Gui
from core.Router import ROOT_ROUTER_PATH


def main():
    # 日志根目录
    LOG_PATH = os.getcwd() + '/LOG'
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)

    if not os.path.exists(ROOT_ROUTER_PATH):
        os.mkdir(ROOT_ROUTER_PATH)
    gui = tkinter.Tk()
    # 窗口标题
    gui.title('RIP协议模拟系统')
    # 主窗口大小SocketRIP
    gui.geometry('1280x800')
    # 禁止改变窗口大小
    gui.resizable(width=False, height=False)

    # 新建一个日志文件
    log_file_path = Tools.create_log(LOG_PATH)
    # 窗口添加组件
    app = Gui.Gui(gui, log_file_path)
    # 进入消息循环
    gui.mainloop()


main()
