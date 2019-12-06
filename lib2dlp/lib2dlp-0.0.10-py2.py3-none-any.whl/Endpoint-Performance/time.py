import psutil
import time
import os,datetime

def main():
        dt =  datetime.datetime.fromtimestamp(psutil.boot_time())
        print "电脑的开机时间:%s" %dt.strftime("%Y-%m-%d,%H:%M:%S")
        timenow = timeget()
        print '程序启动的时间:%s' %timenow
        timecha = time.time() - psutil.boot_time()
        print '开机时间差：%s' %timecha
        time.sleep(3600)


def timeget():
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)    
        return otherStyleTime           
        

if __name__=="__main__":
        main()
