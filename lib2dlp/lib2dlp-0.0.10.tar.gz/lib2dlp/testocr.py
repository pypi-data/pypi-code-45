#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser
import socket
import win32gui,win32ui,win32api,win32con
import time
from PIL import Image
from PIL import ImageGrab
import os


def GetVol():
      vol = "D"
      valuesC = []
      valuesD = []
      cf = ConfigParser.ConfigParser()
      cf.read("conf/endpoint.ini")
      hostname = socket.getfqdn(socket.gethostname())
      ipaddr = socket.gethostbyname(hostname)
      opts_ipC = cf.options("ipC")
      kvs_ipC = cf.items("ipC")
      opts_ipD = cf.options("ipD")
      kvs_ipD = cf.items("ipD")

      for opts in opts_ipC:
         value = cf.get("ipC", opts)
         valuesC.insert(1,value)
      #print valuesC

      for opts in opts_ipD:
         value = cf.get("ipD", opts)
         valuesD.insert(1,value)
      #print valuesD

      if ipaddr in valuesC:
         vol = "C"
         return vol
      elif ipaddr in valuesD:
         vol = "D"
         return vol
      else:
         print(u"error")
         vol = "D"
         return vol
         #sys.exit(2)
      return vol

def window_capture():
      hwnd = 0
      dpath = GetVol() + ':\\DLP\\Result\\'
      hwndDC = win32gui.GetWindowDC(hwnd)
      mfcDC=win32ui.CreateDCFromHandle(hwndDC)
      saveDC=mfcDC.CreateCompatibleDC()
      saveBitMap = win32ui.CreateBitmap()
      MoniterDev=win32api.EnumDisplayMonitors(None,None)
      w = MoniterDev[0][2][2]
      h = MoniterDev[0][2][3]
      #print w,h　　　＃图片大小
      saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
      saveDC.SelectObject(saveBitMap)
      saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
      cc=time.gmtime()
      bmpname=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'_WindowsCapture'+'.bmp'
      saveBitMap.SaveBitmapFile(saveDC, bmpname)
      Image.open(bmpname).save(bmpname[:-4]+".jpg")
      os.remove(bmpname)
      jpgname=bmpname[:-4]+'.jpg'
      djpgname=dpath+jpgname  
      copy_command = "move %s %s" % (jpgname, djpgname)
      os.popen(copy_command)
      return True

def run():
      while True:
            window_capture()
            time.sleep(60)

if __name__ == "__main__":
      run()