#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块
from datetime import datetime
import time
import random
import sys
import os
import shutil
import ConfigParser
import string
import zipfile


reload(sys)
sys.setdefaultencoding('utf8')

class office:

    def hello(self):
        print('hello')

    def timeget(self):
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y%m%d%H%M%S", timeArray) 
        return otherStyleTime

    def mkdir(self,path):
        path=path.strip()
        path=path.rstrip("\\")
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path.decode('utf-8'))
            print path + u' 创建成功'
            return path
        else:
            print path + u' 目录已存在'
            return path

    def enzip(self):
        target_dir = 'D:\\performance2\\Result\\archive\\'
        target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
        f = zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED)
        startdir = "D:\\performance2\\Result"
        for dirpath, dirnames, filenames in os.walk(startdir):
            for filename in filenames:
                f.write(os.path.join(dirpath,filename))
        print 'Sucessful backup to', target
        f.close()

    def file_name(self,file_dir):
        L=[]
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                L.append(os.path.join(root, file))
        return L

    def copyfile(self,source_files,target_files):
        o = office()
        try:         
            file = o.file_name(source_files)
            for f in file:    
                shutil.copy(f,target_files)
            return True
        except Exception,e:
            print e
            print "netLogon False"
            return False
        return

    def prerar(self):
        o = office()
        path = "D:\\performance2\\data\\Result"
        isExists = os.path.exists(path)
        if not isExists:
            o.mkdir(path)
        else:
            shutil.rmtree(path)
            time.sleep(3)
            o.mkdir(path)

        src = "D:\\performance2\\Result"
        dst = "D:\\performance2\\data\\Result"

        o.copyfile(src,dst)

    def enrar(self):
        o = office()
        o.prerar()

        source = ['D:\\performance2\\data\\Result']
        target_dir = 'D:\\performance2\\Result\\archive\\'
        target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'
        zip_command = "D:\\performance2\\tool\\WinRAR\\Rar.exe a %s %s" % (target, ' '.join(source))
        if os.system(zip_command) == 0:
            print 'Sucessful backup to', target
            shutil.rmtree("D:\\performance2\\data\\Result")
        else:
            print 'Backup Failed'

    def logtodis(self,text):
        logpath = 'D:\\performance2\\log\\rundiscovery.txt'
        f = open(logpath,'a+')
        f.write(text)
        f.write('---rundiscovery:\t%s\r\n' %datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.close()

    def rundiscovery(self):
        o = office()
        path = "D:\\performance2\\Result\\archive"
        isExists = os.path.exists(path)
        if not isExists:
            o.mkdir(path)
        else:
            shutil.rmtree(path)
            time.sleep(3)
            o.mkdir(path)
        
        print "START------>" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        o.enzip()
        o.logtodis("ZIP")

        time.sleep(5)
        o.enrar()
        o.logtodis("RAR")
        print "STOP------>" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def test(self):
        i = 0
        path = os.getcwd()+ '\\'
        time.sleep(3)
        starttime = time.time()
        for y in range(18):
            try:
                o = office()
                o.rundiscovery()
                time.sleep(3)
                f = o.timeget()
                print 'rundiscovery' + '  '+ str(i)+ '  ' + f

                i = i + 1
            except Exception,ex:
                print ex
            if y == 17:
                break
            time.sleep(3600)
        print 'over'
        win32api.keybd_event(win32con.VK_LWIN,0,0,0)
        win32api.keybd_event(68,0,0,0)
        win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(win32con.VK_LWIN,0,win32con.KEYEVENTF_KEYUP,0)          
        subprocess.Popen('taskmgr')
        time.sleep(4)
        im = ImageGrab.grab()
        im.save('c:\\12.png')      
        time.sleep(120)
        try:
            os.system('taskkill /IM 360tray.exe /F')
            os.system('taskkill /IM 360EntClient.exe /F')
            os.system('taskkill /IM DLPMain.exe /F')
            os.system('taskkill /IM DlpCenter.exe /F')
            os.system('taskkill /IM dlpmain32.exe /F')
            os.system('taskkill /IM DriverControler.exe /F')
            os.system('taskkill /IM DriverControler.exe /F')
        except Exception,ex:
            print ex
    
#end--------------------------------------------------------

if __name__ == "__main__":
    o = office()
    #o.test()
    o.rundiscovery()