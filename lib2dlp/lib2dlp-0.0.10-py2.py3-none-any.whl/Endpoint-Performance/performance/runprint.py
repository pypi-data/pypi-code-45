#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import time
import win32com,win32api,win32print
from win32com.client import Dispatch, DispatchEx
import win32gui
import ctypes
import ConfigParser
import psutil
Winmm = ctypes.WinDLL('Winmm.dll')

def KillProcess(process):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == process:
            os.system('taskkill /IM %s /F' % process)
            return 1
        else:
            return 0

def get_child_windows(parent):
    if not parent:
      return
    hwndChildList = []
    win32gui.EnumChildWindows(parent,lambda hwnd,param:param.append(hwnd),hwndChildList)
    return hwndChildList

def FindEX(classname,titlename):
    #classname = "OpusApp"
    #titlename = "%s - Microsoft Word" % name
    #hh = get_child_windows(hwnd1)
    #for h in hh:
      #title = win32gui.GetWindowText(h)
      #print title
      #clsname = win32gui.GetClassName(h)
      #print clsname
    #win32print.ClosePrinter(hPrinter)
    #time.sleep(30)
    #win32gui.FindWindow(classname, titlename)
    #print hwnd2
    #print get_child_windows(hwnd2)
    if get_child_windows(win32gui.FindWindow(classname, titlename)) == None:
      #b_t3 = Winmm.timeGetTime()
      #print "b_t3------%s" % b_t3
        return 0
    else:
        return 1

def openword(wordpath,name):
    printer_name = win32print.GetDefaultPrinter()
    #hPrinter = win32print.OpenPrinter(printer_name)

    word = Dispatch('Word.Application')
    word.Visible = 1
    word.DisplayAlerts = 0

    b_t1 = Winmm.timeGetTime()
    #doc = word.Documents.Open(FileName=wordpath, Encoding='gbk')
    doc = word.Documents.Open(FileName=wordpath)
    b_t2 = Winmm.timeGetTime()
    print "b_t2------%s" % b_t2
    try:
        win32api.ShellExecute(
         0,
         "print",
         wordpath,
         '/d:"%s"' % printer_name,
         ".",
         0
        )
        print u"打印%s" % wordpath
    finally:
        #win32print.ClosePrinter(hPrinter)
        classname = "OpusApp"
        titlename = "%s - Microsoft Word" % name
        print "classname:%s,titlename:%s" % (classname,titlename)
        while FindEX(classname,titlename) == 1:
            FindEX(classname,titlename)

        b_t3 = Winmm.timeGetTime()
        print "b_t3------%s" % b_t3
        time.sleep(30)
        word.Quit()
        ret = b_t3 - b_t2
        print(ret)
    try:
        while KillProcess("WINWORD.EXE") == 1:
            KillProcess("WINWORD.EXE")
        time.sleep(10)
        os.system('net stop spooler')
        time.sleep(10)
        os.system('del /f/s/q C:\\Windows\\System32\\spool\\PRINTERS\\*.*')
        time.sleep(10)
        os.system('net start spooler')
        time.sleep(10)
        #os.system('taskkill /IM python.exe /F')
    except Exception,ex:
        print ex
    return ret

def openexcel(xlspath,name):
    printer_name = win32print.GetDefaultPrinter()
    #hPrinter = win32print.OpenPrinter(printer_name)

    excel = Dispatch('Excel.Application')
    excel.Visible =1
    excel.DisplayAlerts = 0

    b_t1 = Winmm.timeGetTime()
    xls = excel.Workbooks.Open(xlspath)
    b_t2 = Winmm.timeGetTime()
    print "b_t2------%s" % b_t2
    try:
        win32api.ShellExecute(
        0,
        "print",
        xlspath,
        '/d:"%s"' % printer_name,
        ".",
        0
        )
        print u"打印%s" % xlspath
    finally:
        #win32print.ClosePrinter(hPrinter)
        classname = "XLMAIN"
        titlename = "Microsoft Excel - %s" % name
        print "classname:%s,titlename:%s" % (classname,titlename)
        while FindEX(classname,titlename) == 1:
            FindEX(classname,titlename)

        b_t3 = Winmm.timeGetTime()
        print "b_t3------%s" % b_t3
        time.sleep(30)
        excel.quit()
        ret = b_t3 - b_t2
        print(ret)
    try:
        while KillProcess("EXCEL.EXE") == 1:
            KillProcess("EXCEL.EXE")
        time.sleep(10)
        os.system('net stop spooler')
        time.sleep(10)
        os.system('del /f/s/q C:\\Windows\\System32\\spool\\PRINTERS\\*.*')
        time.sleep(10)
        os.system('net start spooler')
        time.sleep(10)
        #os.system('taskkill /IM python.exe /F')
    except Exception,ex:
        print ex
    return ret

def openppt(pptpath,name):
    printer_name = win32print.GetDefaultPrinter()
    #hPrinter = win32print.OpenPrinter(printer_name)

    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = 1
    ppt.DisplayAlerts = 0

    b_t1 = Winmm.timeGetTime()
    power = ppt.Presentations.Open(pptpath)
    b_t2 = Winmm.timeGetTime()
    print "b_t2------%s" % b_t2
    try:
        win32api.ShellExecute(
         0,
         "print",
         pptpath,
         '/d:"%s"' % printer_name,
         ".",
         0
        )
        print u"打印%s" % pptpath
    finally:
        #win32print.ClosePrinter(hPrinter)
        classname = "PPTFrameClass"
        titlename = "%s - Microsoft PowerPoint" % name
        print "classname:%s,titlename:%s" % (classname,titlename)
        while FindEX(classname,titlename) == 1:
            FindEX(classname,titlename)

        b_t3 = Winmm.timeGetTime()
        print "b_t3------%s" % b_t3
        time.sleep(30)
        ppt.quit()
        ret = b_t3 - b_t2
        print(ret)
    try:
        while KillProcess("POWERPNT.EXE") == 1:
            KillProcess("POWERPNT.EXE")
        time.sleep(10)
        os.system('net stop spooler')
        time.sleep(10)
        os.system('del /f/s/q C:\\Windows\\System32\\spool\\PRINTERS\\*.*')
        time.sleep(10)
        os.system('net start spooler')
        time.sleep(10)
        #os.system('taskkill /IM python.exe /F')
    except Exception,ex:
        print ex
    return ret

def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def getfile():
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open('perfconf.ini'))
        office_folder = config.get("print", "folder")
        return office_folder
    except Exception as e:
        print e

def getFileSize(file):
    fsize = 0
    ext = file.split('.')[-1]
    if('ppt' in ext):
        filePath = getfile() + "\\ppt\\" + file
    elif('doc' in ext):
        filePath = getfile() + "\\word\\" + file
    elif('xls' in ext):
        filePath = getfile() + "\\excel\\" + file
    fsize = os.path.getsize(filePath)
    #fsize = fsize/float(1024 * 1024)
    fsize = fsize/float(1024)
    return round(fsize, 2)

def loginfo(file,totaltime):
    logpath = 'log\\runoffice.txt'
    f = open(logpath,'a+')
    f.write('%s\t%s\t\t runoffice_time:%sms\t\t%sKB\r\n' % (timeget(),file,totaltime,getFileSize(file)))
    f.close()

if __name__ == '__main__':
    folder = getfile()
    print folder
    #totaltime = 0
    for boot,dirs,files in os.walk(folder):
        for file in files:
            totaltime = 0
            ext = file.split('.')[-1]
            if('ppt' in ext):
                coasttime = openppt(os.path.join(boot,file),file)
                
                time.sleep(15)
                totaltime = totaltime + coasttime
                #print totaltime
            elif('doc' in ext):
                coasttime = openword(os.path.join(boot,file),file)

                time.sleep(15)
                totaltime = totaltime + coasttime
                #print totaltime
            elif('xls' in ext):
                coasttime = openexcel(os.path.join(boot, file),file)
                
                time.sleep(15)
                totaltime = totaltime + coasttime
                #print totaltime
            time.sleep(15)
            loginfo(file,totaltime)