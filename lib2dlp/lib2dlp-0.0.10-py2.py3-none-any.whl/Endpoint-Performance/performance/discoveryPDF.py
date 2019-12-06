#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块

from PIL import ImageGrab
from PIL import Image
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph,Frame
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Image as platImage
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
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

    def CreatePdfNum(self,s,num):
        o = office()
        x = 0
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        #pdfmetrics.registerFont(TTFont('hei', 'hei.TTF'))
        #import testSubFun
        #testSubFun.testSubFunc('first')
        #设置页面大小

        #discoverysrc,pdfdir = o.getpath()
        #o.mkdir(pdfdir)
        #pdfdir = "D:\\performance2\\Result\\pdf"

        c = canvas.Canvas('D:\\performance2\\Result\\pdf\\dlp%s.pdf' % num,pagesize=A4)
        #c = canvas.Canvas('%s\\dlp%s.pdf' % (pdfdir,num),pagesize=A4)
        xlength,ylength = A4
        #print('width:%d high:%d'%(xlength,ylength))
        #c.line(1,1,ylength/2,ylength)
        #设置文字类型及字号
        #c.setFont('hei',20)
        #生成一个table表格
        atable = [[1,2,3,4,5,6,7,8],[11,12,13,14,15,16,17,18]]
        t = Table(atable,50,20)
        t.setStyle(TableStyle([('ALIGN',(0,0),(3,1),'CENTER'),
                               ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
                               ('BOX',(0,0),(-1,-1),0.25,colors.black)]))
        textOb = c.beginText(1,ylength-10)
        indexVlaue = 0
        while(indexVlaue < ylength):
            #textStr = u'''wo shi tupian---wo shi tupian--wo shi tupian--wo shi tupian%d'''%indexVlaue + salt
            textStr = u"wo shi tupian---wo shi tupian--wo shi tupian--wo shi tupian--参考资料%d"% indexVlaue + salt
            #print('nextline,nextline%d'%indexVlaue)
            textOb.textLine(textStr)
            indexVlaue = indexVlaue + 1
            break
        c.drawText(textOb)

        #discoverysrc = "D:\\performance2\\data"
        #简单的图片载入
        imageValue = 'D:\\performance2\\data\\dlp.png'
        #imageValue = '%s\\dlp.png' % discoverysrc
        c.drawImage(imageValue,97,97,650,650)
        #c.drawImage('file\\dlp.png',50,50,50,50)
        t.split(0,0)
        t.drawOn(c,100,1)
        c.showPage()
        #换页的方式不同的showPage
        while x < s:
            imageValue = 'D:\\performance2\\data\\dlp.png'
            #imageValue = '%s\\dlp.png' % discoverysrc
            c.drawImage(imageValue,97,97,650,650)
            c.drawString(0,0,'tupian%s' % x)
            c.showPage()
            x = x + 1
        c.save()
    def CreatePdfE(self,n):
        m = 0
        o = office()
        while m < n:
            s = random.randint(500,1000)
            o.CreatePdfNum(s,m)
            m = m + 1
        return True

    def getpath(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('D:\\performance2\\perfconf.ini'))
            discoverysrc = config.get("data", "discoverysrc")
            pdfdir = config.get("discovery", "pdf")
            return discoverysrc,pdfdir
        except Exception as e:
            print e

    def getdislogpath(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('D:\\performance2\\perfconf.ini'))
            discoverylog = config.get("logdir", "dislog")
            return discoverylog
        except Exception as e:
            print e
    
    def get_desktop(self):
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return _winreg.QueryValueEx(key, "Desktop")[0]


    def logtodis(self,text):
        #o = office()
        #discoverylog = o.getdislogpath()
        #discoverylog = "D:\\performance2\\log"
        logpath = 'D:\\performance2\\log\\rundiscovery.txt'
        f = open(logpath,'a+')
        f.write(text)
        f.write('---rundiscovery:\t%s\r\n' %datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.close()

    def rundiscovery(self):
        o = office()
        pdfdir = "D:\\performance2\\Result\\pdf"
        #discoverysrc,pdfdir = o.getpath()
        isExists = os.path.exists(pdfdir)
        if not isExists:
            o.mkdir(pdfdir)
        else:
            shutil.rmtree(pdfdir)
            time.sleep(3)
            o.mkdir(pdfdir)
        
        print "START------>" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        o.CreatePdfE(40)
        time.sleep(5)
        o.logtodis("PDF")
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
                f = timeget()
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