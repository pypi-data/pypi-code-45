#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import time
import subprocess
import multiprocessing
import threading
import win32api
import win32con
from PIL import ImageGrab
from datetime import datetime
from datetime import date
from apscheduler.scheduler import Scheduler


def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def test():
    i = 0
    path = os.getcwd()+ '\\'
    time.sleep(60)
    starttime = time.time()
    for y in range(18):
        try:
            
            os.system(path + 'copy_time.exe')
            time.sleep(120)
            a = timeget()
            print 'copy_time.exe' + '  '+ str(i) + '  ' + a

            os.system(path + 'runoffice.exe')
            time.sleep(120)
            b = timeget()
            print 'runoffice.exe' + '  '+ str(i)+ '  ' + b

            os.system(path + 'unzip_time.exe')
            time.sleep(120)
            c = timeget()
            print 'unzip_time.exe' + '  '+ str(i)+ '  ' + c

            os.system(path + 'IEOpen.exe')
            time.sleep(120)
            d = timeget()
            print 'IEOpen.exe' + '  '+ str(i)+ '  ' + d

            os.system('python ' + path + 'http_test.py')
            time.sleep(300)
            e = timeget()
            print 'https_test' + '  '+ str(i)+ '  ' + e

            os.system('python ' + path + 'https_test.py')
            time.sleep(300)
            f = timeget()
            print 'netshare' + '  '+ str(i)+ '  ' + f

            os.system('python ' + path + 'netshare.py')
            time.sleep(300)
            g = timeget()
            print 'smtp' + '  '+ str(i)+ '  ' + g

            os.system('python ' + path + 'smtp.py')
            time.sleep(300)
            h = timeget()
            print 'smtp' + '  '+ str(i)+ '  ' + h
            
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

def discovery():
    i = 0
    path = os.getcwd()+ '\\'
    time.sleep(10)
    starttime = time.time()
    try:
        os.system('python ' + path + 'discoveryTXT.py')
        time.sleep(10)
        discoveryTXT = timeget()
        print 'discoveryTXT' + '  '+ str(i)+ '  ' + discoveryTXT

        os.system('python ' + path + 'discoveryWORD.py')
        time.sleep(10)
        discoveryWORD = timeget()
        print 'discoveryWORD' + '  '+ str(i)+ '  ' + discoveryWORD

        os.system('python ' + path + 'discoveryEXCEL.py')
        time.sleep(10)
        discoveryEXCEL = timeget()
        print 'discoveryEXCEL' + '  '+ str(i)+ '  ' + discoveryEXCEL

        os.system('python ' + path + 'discoveryPPT.py')
        time.sleep(10)
        discoveryPPT = timeget()
        print 'discoveryPPT' + '  '+ str(i)+ '  ' + discoveryPPT

        os.system('python ' + path + 'discoveryRAR.py')
        time.sleep(10)
        discoveryRAR = timeget()
        print 'discoveryRAR' + '  '+ str(i)+ '  ' + discoveryRAR

        i = i + 1

    except Exception,ex:
        print ex

def runAll_test():
    i = 0
    t = 1
    path = os.getcwd()+ '\\'
    time.sleep(10)
    starttime = time.time()
    try:
        while t < 11:
            os.system('python ' + path + 'smtp.py')
            time.sleep(3)
            smtp = timeget()
            print 'smtp' + '  '+ str(i)+ '  ' + smtp

            os.system('python ' + path + 'IEOpen.py')
            time.sleep(3)
            IEOpen = timeget()
            print 'IEOpen' + '  '+ str(i)+ '  ' + IEOpen

            os.system('python ' + path + 'writeWord.py')
            time.sleep(3)
            writeWord = timeget()
            print 'writeWord' + '  '+ str(i)+ '  ' + writeWord

            os.system(path + 'UsbDriver.exe')
            time.sleep(3)
            UsbDriver = timeget()
            print 'UsbDriver' + '  '+ str(i)+ '  ' + UsbDriver

            os.system(path + 'Printer.exe')
            time.sleep(3)
            Printer = timeget()
            print 'Printer' + '  '+ str(i)+ '  ' + Printer

            os.system('python ' + path + 'capture.py')
            time.sleep(3)
            capture = timeget()
            print 'capture' + '  '+ str(i)+ '  ' + capture

            os.system('python ' + path + 'mouse.py')
            time.sleep(3)
            mouse = timeget()
            print 'mouse' + '  '+ str(i)+ '  ' + mouse

            time.sleep(60)
            t = t + 1      

        i = i + 1

    except Exception,ex:
        print ex

def runALLAsThread():
    threads = []
    i1 = threading.Thread(target=runAll_test(),name='runAll_test')
    threads.append(i1)
    for t in threads:
        t.start()
        t.join()

def job_func():
    print "start discovery %s" % timeget()
    runAll_test()
    print "stop discovery %s" % timeget()

def job_func1():
    scheduler = Scheduler()
    scheduler.start()
    job = scheduler.add_interval_job(job_func, hours=1) # hours,minutes,seconds

    runAll_test()

def runjob(x,y,z):
    scheduler = Scheduler()
    scheduler.start()

    #scheduler.add_job(job_func, 'date', run_date=datetime(2019, 06, 05, 11, 20, 0), args=[]) #python 3.6
    #scheduler.add_interval_job(job_func, hours=2, start_date='2010-10-10 09:30')   #python 2.7
    job = scheduler.add_date_job(job_func1, datetime(2019, 9, x, y, z, 0), [])
    #job = scheduler.add_interval_job(job_func, seconds=5)
 
    time.sleep(7*24*60*60)

    scheduler.shutdown(wait=False)

if __name__ == '__main__':
    #test()
    x,y,z = 26,20,00 # %d %H %M
    runjob(x,y,z)