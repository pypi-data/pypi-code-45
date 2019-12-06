#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image
from PIL import ImageGrab
import win32gui
import win32ui
import win32api
import win32con
import time
import os
import random
import shutil

def genStr(num):
   H = '0123456789ABCDEFGHIJKLMNOPQISTUVWXYZabcdefghijklmnopqistuvwxyz'
   salt = ''
   for i in range(num):
      salt += random.choice(H)
   return salt

def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def window_capture(dpath):
   hwnd = 0
   #dpath = 'data/capture/%s' % path
   hwndDC = win32gui.GetWindowDC(hwnd)
   mfcDC = win32ui.CreateDCFromHandle(hwndDC)
   saveDC = mfcDC.CreateCompatibleDC()
   saveBitMap = win32ui.CreateBitmap()
   MoniterDev = win32api.EnumDisplayMonitors(None,None)
   w = MoniterDev[0][2][2]
   h = MoniterDev[0][2][3]
   time.sleep(1)
   #print w,h　　　＃图片大小
   saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
   saveDC.SelectObject(saveBitMap)
   saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
   cc = time.gmtime()
   bmpname = str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'_WindowsCapture'+'.bmp'
   saveBitMap.SaveBitmapFile(saveDC, bmpname)
   Image.open(bmpname).save(bmpname[:-4]+".jpg")
   os.remove(bmpname)
   jpgname = bmpname[:-4]+'.jpg'
   djpgname = dpath + "/" + jpgname
   copy_command = "move %s %s" % (jpgname, djpgname)
   os.popen(copy_command)
   mfcDC.DeleteDC()
   saveDC.DeleteDC()
   win32gui.ReleaseDC(hwnd,hwndDC)
   win32gui.DeleteObject(saveBitMap.GetHandle())
   return True

if __name__ == "__main__":
   while 1:
      hpath = 'data/capture/'
      dpath = 'data/capture/%s' % genStr(8)
      if os.path.exists(hpath):
         shutil.rmtree(hpath,ignore_errors=True)
         time.sleep(1)
         os.makedirs(dpath)
         print u"%s——>先删除后创建目录%s" % (timeget(),dpath)
      else:
         os.makedirs(dpath)
         print u"%s——>直接创建目录%s" % (timeget(),dpath)
      x = 0
      while x < 100:
         window_capture(dpath)
         time.sleep(3)
         x += 1