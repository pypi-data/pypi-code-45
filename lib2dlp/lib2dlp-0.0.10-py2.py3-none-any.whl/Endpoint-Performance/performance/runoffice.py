#coding:gbk

import os
import win32com,win32api
from win32com.client import Dispatch, DispatchEx
import time
import ctypes
import ConfigParser

Winmm = ctypes.WinDLL('Winmm.dll')

def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def openword(wordpath):
    word = Dispatch('Word.Application')  # ´ò¿ªwordÓ¦ÓÃ³ÌÐò
    # word = DispatchEx('Word.Application') #Æô¶¯¶ÀÁ¢µÄ½ø³Ì
    word.Visible = 1  # ºóÌ¨ÔËÐÐ,²»ÏÔÊ¾
    word.DisplayAlerts = 0  # ²»¾¯¸æ

    b_t = Winmm.timeGetTime()
    doc = word.Documents.Open(FileName=wordpath, Encoding='gbk')
    ret = Winmm.timeGetTime() - b_t
    print(ret)
    time.sleep(1)
    word.Quit()
    return ret

def openexcel(xlspath):
    excel = Dispatch('Excel.Application')
    excel.Visible =1
    excel.DisplayAlerts = 0  # ²»¾¯¸æ
    b_t = Winmm.timeGetTime()
    ret = excel.Workbooks.Open(xlspath)
    ret = Winmm.timeGetTime() - b_t
    print(ret)
    time.sleep(1)
    excel.quit()
    return ret

def openppt(pptpath):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = 1
    ppt.DisplayAlerts = 0  # ²»¾¯¸æ
    #path = r'D:\ÆóÒµ°æ\·À²¡¶¾\Ö÷¶¯·ÀÓù½éÉÜ.ppt'  # wordÎÄ¼þÂ·¾¶
    b_t = Winmm.timeGetTime()
    ret = ppt.Presentations.Open(pptpath)
    ret = Winmm.timeGetTime() - b_t
    print(ret)
    time.sleep(1)
    ppt.quit()
    return ret

def getfile():
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open('perfconf.ini'))
        office_folder = config.get("office", "folder")
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
    #Winmm = ctypes.WinDLL('Winmm.dll')
    folder = getfile()
    print folder
    #totaltime = 0
    for boot,dirs,files in os.walk(folder):
        for file in files:
            totaltime = 0
            ext = file.split('.')[-1]
            if('ppt' in ext):
                coasttime = openppt(os.path.join(boot,file))
                time.sleep(5)
                os.system('taskkill /IM POWERPNT.EXE /F')
                totaltime = totaltime + coasttime
            elif('doc' in ext):
                coasttime = openword(os.path.join(boot,file))
                time.sleep(5)
                os.system('taskkill /IM WINWORD.EXE /F')
                totaltime = totaltime + coasttime
            elif('xls' in ext):
                coasttime = openexcel(os.path.join(boot, file))
                time.sleep(5)
                os.system('taskkill /IM EXCEL.EXE /F')
                totaltime = totaltime + coasttime
            time.sleep(5)
            loginfo(file,totaltime)
    #print(totaltime)