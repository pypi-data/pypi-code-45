#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块
from datetime import datetime
import time
import random
import sys
import os
import shutil
import ConfigParser
import string
import zipfile


reload(sys)
sys.setdefaultencoding('utf8')

class office:
    def enzip(self,i):
        target_dir = 'Result\\'
        target = target_dir + "test%s" % i + '.zip'
        f = zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED)
        startdir = "Result\\"
        j = i - 1
        f.write(startdir + "test%s.zip" % j)
        print 'Sucessful backup to', target
        f.close()

    def enzipStage(self,i):
        o = office()
        for j in xrange(1,i+1):
            o.enzip(j)
            print j
        src_file = "Result\\test%s.zip" % i
        last_file = "Result\\archive\\test%s.zip" % i
        if os.path.exists(last_file):
            os.remove(last_file)
            shutil.move(src_file,last_file)
        else:
            shutil.move(src_file,last_file)
        for x in xrange(1,i):
            my_file = "Result\\test%s.zip" % x
            if os.path.exists(my_file):
                os.remove(my_file)
            else:
                print 'no such file:%s' % my_file

    def copyfile(self,source_files,target_files):
        o = office()
        try:         
            file = o.file_name(source_files)
            for f in file:    
                shutil.copy(f,target_files)
            return True
        except Exception,e:
            print e
            print "netLogon False"
            return False
        return

    def enrar(self,i):
        path = "D:\\DLP\\Endpoint-Performance\\performance2"
        source = ['%s\\Result\\test%s.rar' % (path,i - 1)]
        target_dir = 'Result\\'
        target = target_dir + "test%s" % i + '.rar'
        rar_command = "%s\\tool\\WinRAR\\Rar.exe a %s %s" % (path, target, ' '.join(source))
        if os.system(rar_command) == 0:
            print 'Sucessful backup to', target
            #shutil.rmtree("D:\\performance2\\data\\Result")
        else:
            print 'Backup Failed'

    def enrarStage(self,i):
        o = office()
        for j in xrange(1,i+1):
            o.enrar(j)
            print j
        src_file = "Result\\test%s.rar" % i
        last_file = "Result\\archive\\test%s.rar" % i
        if os.path.exists(last_file):
            os.remove(last_file)
            shutil.move(src_file,last_file)
        else:
            shutil.move(src_file,last_file)
        for x in xrange(1,i):
            my_file = "Result\\test%s.rar" % x
            if os.path.exists(my_file):
                os.remove(my_file)
            else:
                print 'no such file:%s' % my_file

    
#end--------------------------------------------------------

if __name__ == "__main__":
    o = office()
    o.enrarStage(20)#压缩多少层rar
    o.enzipStage(20)#压缩多少层zip