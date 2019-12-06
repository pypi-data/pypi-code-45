#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块


from datetime import datetime
from faker import Factory
from faker import Faker
import xlwt
import xlrd
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

    def CreateExcelNum(self,text,s,num,r,c):
        path = "D:\\performance2\\Result\\excel"
        o.mkdir(path)
        try:
            i = 0
            z = 3
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.name = 'Times New Roman'
            font.bold = True
            style.font = font
            filename = xlwt.Workbook(encoding = 'UTF-8')
            while i < s:
                t = 0
                wa =0
                qc = 0
                x = random.randint(0, 10)
                #y = random.randint(0, 10)
                sheet = filename.add_sheet("test %s" % i)
                #while t < 100:
                while t < 100:
                    while wa < r:                       # r 代表行
                        for qc in xrange(0,c):            #c 代表列
                            sheet.write(wa,qc,text,style)
                            qc = qc + 1
                        wa = wa + 1
                    t = t + 1
                i = i + 1
            sheet = filename.add_sheet("test %s" % s)
            while z < 10:
                salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
                sheet.write(2,z - 3,"参考资料" + salt,style)
                z = z + 1
            filename.save("D:\\performance2\\Result\\excel\\dlp%s.xls" % num)
            return True
        except Exception,e:
            print(str(e))
            return False
    def CreateExcelE(self,text,s,n,r,c):
        m = 0
        o = office()
        while m < n:
            o.CreateExcelNum(text,s,m,r,c)
            m = m + 1
        return True

    def CreateExcelE1(self,n):
        o = office()
        m = 0
        faker = Faker("zh_CN")
        text = faker.text(max_nb_chars=255)

        while m < n:
            s = random.randint(50,100)
            o.CreateExcelNum(text,s,m,100,50)
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
        path = "D:\\performance2\\Result\\excel"
        isExists = os.path.exists(path)
        if not isExists:
            o.mkdir(path)
        else:
            shutil.rmtree(path)
            time.sleep(3)
            o.mkdir(path)
        
        print "START------>" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        o.CreateExcelE1(9)#之前是9
        time.sleep(5)
        o.logtodis("WORD")
        
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