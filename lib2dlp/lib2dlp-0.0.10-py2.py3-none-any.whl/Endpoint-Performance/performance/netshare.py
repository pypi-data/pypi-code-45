#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import getopt
import time
import shutil
from ctypes import *
#_DEBUG=True

def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L

def copyfile(source_files,target_files):
    try:         
        file = file_name(source_files)
        for f in file:    
            shutil.copy(f,target_files)
        return 1
    except Exception,e:
        print e
        #print "netLogon False"
        return 0

def myFmtCallback(command, modifier, arg):
    #print(command)
    return 1    # TRUE

def format_drive(Drive, Format, Title):
    try:
        fm = windll.LoadLibrary('fmifs.dll')
        FMT_CB_FUNC = WINFUNCTYPE(c_int, c_int, c_int, c_void_p)
        FMIFS_HARDDISK = 0
    finally:
    
        ret = fm.FormatEx(c_wchar_p(Drive), FMIFS_HARDDISK, c_wchar_p(Format),
                c_wchar_p(Title), True, c_int(0), FMT_CB_FUNC(myFmtCallback))
        if ret == 0:
            return 1
        else:
            return 0
def format_usb():
    if format_drive('G:\\', 'NTFS', 'USBDrive') == 1:
        print u"格式化成功%s" % timeget()
    else:
        print u"格式化失败%s" % timeget()
def netshare_test():
    src = "data\\usb"
    dst = "G:\\"
    if copyfile(src,dst) == 1:
        return 1
    else:
        return 0

#end--------------------------------------------------------
if __name__ == "__main__":
    while 1:
        time.sleep(30)
        if netshare_test() == 1:
            print u"拷贝完成%s" % timeget()
        else:
            print u"拷贝失败%s" % timeget()
            format_usb()
        time.sleep(10)
        
    '''
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -t:测试HTTP上传文件\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "htpclTv", ["help", "output="])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        if cmd in ("-t", ""):
            http_test()
        elif cmd in ("-v", "--version"):
            print("version 1.0")
    '''