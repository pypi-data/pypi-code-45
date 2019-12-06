#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser
import socket
import win32gui,win32ui,win32api,win32con
import time
import win32serviceutil
import win32service
import win32event
import os
import logging
import inspect
import sys
import servicemanager
from PIL import Image
from PIL import ImageGrab

class PythonServiceOCR(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonServiceOCR"
    _svc_display_name_ = "Python OCR Test"
    _svc_description_ = "This is a python OCR test code"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True

    def _getLogger(self):
        logger = logging.getLogger('[PythonServiceOCR]')

        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger
    
    def SvcDoRun(self):
        import ConfigParser
        import socket
        import win32gui,win32ui,win32api,win32con
        import time
        import os
        import logging
        import inspect
        import sys
        import servicemanager
        from PIL import Image
        from PIL import ImageGrab
        import servicemanager
        self.logger.info("service is run.... START")
        while self.run:
            os.system("C:\\Windows\\notepad.exe")
            time.sleep(5)
            self.logger.info("service is run.... END")
        
        '''
        f = open('test.dat', 'w+')  
        rc = None  
          
        # if the stop event hasn't been fired keep looping  
        while rc != win32event.WAIT_OBJECT_0:  
            f.write('TEST DATA\n')  
            f.flush()  
            # block for 5 seconds and listen for a stop event  
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)  
              
        f.write('SHUTTING DOWN\n')  
        f.close()
        self.logger.info("service is run.... END")
        '''

        '''
        while self.run:
            self.logger.info("I am runing....")
            #self._doRun(test())
            test1()
            #self.logger.info("到底能不能运行")
            time.sleep(5)'''
        # win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False

    def test1():
        self.logger.info("test1到底能不能运行")
          
    def test(self):
        hwnd = 0
        #dpath = 'C:\\DLP\\Result\\'
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　＃图片大小
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        cc = time.gmtime()
        bmpname = str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8) + \
            str(cc[4])+str(cc[5])+'_WindowsCapture'+'.bmp'
        saveBitMap.SaveBitmapFile(saveDC, bmpname)
        Image.open(bmpname).save(bmpname[:-4]+".jpg")
        os.remove(bmpname)
        jpgname = bmpname[:-4]+'.jpg'
        #djpgname = dpath+jpgname
        #copy_command = "move %s %s" % (jpgname, djpgname)
        #os.popen(copy_command)
        return True


if __name__ == "__main__":
      win32serviceutil.HandleCommandLine(PythonServiceOCR)