#coding:utf-8

import win32com.client
import win32api,ctypes
import time,os
import ConfigParser
from selenium import webdriver

def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime
'''
urls = ['http://baidu.com',
        'https://hao.360.cn/',
        'https://www.tmall.com/',
        'https://www.jd.com/',
        'http://www.163.com/',
        'https://www.so.com/',
        'http://weibo.com/',
        'http://www.sina.com.cn/']
'''
def openChrome(url):
    driver=webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.maximize_window()
    driver.get(url)
    driver.quit()
    return True

def openIE(url):
    Winmm = ctypes.WinDLL('Winmm.dll')
    os.system('taskkill /IM iexplore.exe /F')
    os.system('taskkill /IM 360se.exe /F')
    os.system('taskkill /IM chrome.exe /F')
    ie = win32com.client.Dispatch('InternetExplorer.Application')
    ie.Visible = 0
    begin = Winmm.timeGetTime()
    ie.Navigate(url)
    state = ie.ReadyState
    timeout = 50
    interval = 0.003

    while timeout>=0:
        try:
            state = ie.ReadyState
        except:
            pass
        #print(state)
        if(state == 4 or state == 0):
            print('%s || state:%d'%(url,state))
            break
        t = time.time()
        time.sleep(interval)
        timeout -= time.time() - t
    ret = Winmm.timeGetTime() - begin
    time.sleep(3)
    os.system('taskkill /IM iexplore.exe /F')
    os.system('taskkill /IM 360se.exe /F')
    os.system('taskkill /IM chrome.exe /F')
    return ret

def geturls():
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open('perfconf.ini'))
        urls = []
        for item in config.options('urls'):
            print(config.get('urls',item))
            urls.append(config.get('urls',item))
        return urls
    except Exception as e:
        print e


def openallurl():
    urllist = geturls()
    sum = 0
    for url in urllist:
        ret = openIE(url)
        print(ret)
        sum = sum + ret
        print(sum)
        time.sleep(1)
    return sum

if __name__ == "__main__":
    while 1:
        ieopen = openallurl()
        print(ieopen)
        logpath = 'log\\ieopen.txt'
        f = open(logpath,'a+')
        f.write('%s\t\tieopen_time:\t%s\r\n' %(timeget(),ieopen))
        f.close()