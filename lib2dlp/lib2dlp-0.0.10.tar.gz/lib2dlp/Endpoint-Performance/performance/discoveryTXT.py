#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块

from datetime import datetime
from faker import Factory
from faker import Faker
import time
import random
import sys
import os
import shutil
import ConfigParser
import string


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

    def toText(self,f):
        faker = Faker("zh_CN")
        f.writelines("王宝强")
        f.writelines("\n")
        f.writelines("苏绍辉")
        f.writelines("\n")
        f.writelines("姓名: ")
        f.writelines(faker.name())
        f.writelines("\n")
        f.writelines("电话号码: ")
        f.writelines(faker.phone_number())
        f.writelines("\n")
        f.writelines("18位身份证号: ")
        f.writelines(faker.ssn())
        f.writelines("\n")
        f.writelines("信用卡卡号: ")
        f.writelines(faker.credit_card_number(card_type=None))
        f.writelines("\n")
        f.writelines("参考资料")
        f.writelines("\n")
        f.writelines("地址: ")
        f.writelines(faker.address())

    def genContent(self,num):
        o = office()
        fix = o.timeget()
        spath = "D:\\performance2\\Result\\txt\\%s" % fix
        path = o.mkdir(spath)
        size = random.randint(1,100)

        faker = Faker("zh_CN")
        file = '%s\\content_%s.txt' % (path,num)
        s = faker.text(max_nb_chars=2048)
        if os.path.exists(file):
            os.remove(file)
            pass
        f = open(file,'a')
        i = 0
        #while(i < 185*size):#循环185次刚好是1M大小文件,循环2次刚好是12K大小
        while(i < 20*size):#循环185次刚好是1M大小文件,循环2次刚好是12K大小
            f.write(s)
            i = i + 1
        o.toText(f)
        f.close()
        return True

    def CreateContent(self,n):
        m = 0
        o = office()
        while m < n:
            o.genContent(m)
            m = m + 1
        return True
    
    def get_desktop(self):
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return _winreg.QueryValueEx(key, "Desktop")[0]

    def logtodis(self,text):
        logpath = 'D:\\performance2\\log\\rundiscovery.txt'
        f = open(logpath,'a+')
        f.write(text)
        f.write('---rundiscovery:\t%s\r\n' %datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.close()

    def rundiscovery(self):
        o = office()
        path = "D:\\performance2\\Result\\txt"
        isExists = os.path.exists(path)
        if not isExists:
            o.mkdir(path)
        else:
            shutil.rmtree(path,ignore_errors=True)
            time.sleep(3)
            o.mkdir(path)
        
        print "START------>" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        o.CreateContent(200)
        time.sleep(5)
        o.logtodis("TXT")
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