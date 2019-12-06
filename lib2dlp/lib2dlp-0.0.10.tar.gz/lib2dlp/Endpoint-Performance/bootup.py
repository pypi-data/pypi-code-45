import os
import time
import subprocess
from PIL import ImageGrab
import win32api
import win32con
import psutil
import sys

def startup():
    try:
        os.system(r'C:\Windows\System32\cmd.exe cmd /c ""C:\logman_skylar - 6.6.bat" "')
        os.system(r'C:\Windows\System32\cmd.exe cmd /c ""C:\start.bat" "')
        time.sleep(30)
        f = open(r'c:\\count.txt', 'a+')
        f.writelines('a' + '\n')
        f.close()            
        win32api.keybd_event(win32con.VK_LWIN,0,0,0)
        win32api.keybd_event(68,0,0,0)
        win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(win32con.VK_LWIN,0,win32con.KEYEVENTF_KEYUP,0)          
        subprocess.Popen('taskmgr')
        time.sleep(2)
        im = ImageGrab.grab()
        im.save('c:\\%s.png' %time.time()) 
	os.system(r'C:\Procmon.exe /Terminate')
	if os.path.exists(r"C:\test.pml"):
	    os.rename(r"C:\test.pml",r"C:\%s.pml" %time.time())
	pids = processinfo()
	for i in pids:
	    os.system(r'"C:\Program Files (x86)\Debugging Tools for Windows\adplus.vbs" -hang -p %s -fullonfirst -quiet -o c:\dumps' %i)
        os.system('taskkill /IM 360tray.exe /F')
        os.system('taskkill /IM 360EntClient.exe /F')                          
        os.system("shutdown -r -t 5")
    except Exception,ex:
        print ex

def test():
    if os.path.exists(r'c:\\count.txt'):
        f = open(r'c:\\count.txt', 'r')
        count = f.readlines()
        f.close()
        print len(count)
        if len(count) == 3:
            os.remove(r'c:\\count.txt')
        else:
            startup()
    else:
        startup()

     
def processinfo():
    pidlist=[]
    try:
	pids = psutil.pids()
	for pid in pids: 
	    p = psutil.Process(pid)
	    if p.name() == "360EntClient.exe" or  p.name() =="360tray.exe":
		pidlist.append(pid)
	return pidlist
    except Exception,ex:
	print ex
		   
    
if __name__ == '__main__':
    test()