#!/usr/bin/python
# -*- coding: UTF-8 -*-
from jpype import *
from faker import Factory
import os.path
import random
import pycurl
from StringIO import StringIO
import xlrd
import base64
import multiprocessing
import threading

def getUuid():
   faker = Factory().create('zh_CN')
   s = faker.uuid4()
   uuid = s.replace('-', '')
   return uuid

def getPhone():
   faker = Factory().create('zh_CN')
   phone = faker.phone_number()
   return phone

def run(uuid,phoneNum):
   #userId = "178"
   userId = random.randint(100,999)
   #uuid = "2c5682de1a3247b2bf1521cbacfa0c4c"
   #phoneNum = "13810582372"
   code = "6666"
   t = "1562994935"

   jarpath = os.path.join(os.path.abspath('.'), 'jar\\')
   startJVM("D:\\jdk1.8.0_221\\jre\\bin\\server\\jvm.dll", "-ea","-Dproperty=value", "-Djava.class.path=%s" % (jarpath + 'newdes.jar'))
   JDClass = JClass("com.encode.encode.des.TestUnit4Des")
   jd = JDClass()
   print jd.sc(str(userId),uuid,phoneNum,code,t)
   shutdownJVM()

def getUrl(ip,port):
   url = "http://%s:%s/api" % (ip,port)
   return url

def getLoginUrl(ip,port):
   url = "http://%s:%s/api/gettoken" % (ip,port)
   return url

def getData(username):
   post_data = '{"session":{"version":"1",\
   "sid":"2919219201219329320329329",\
   "computer_name":"desktop_vvv",\
   "checksum":"",\
   "username":"%s",\
   "winuser":"administrator",\
   "mid":"mid1292121032",\
   "ip":"192.168.50.203",\
   "op":"dlp",\
   "type":3},\
   "data":{"actid":2,\
   "notes":"我在TEST申请理由->电话公司新闻一起准备注册只有作者这个出来历史表示大小拥有评论拥有地区帖子重要服务一样中国帖子管理相关来自进行关系事情直接应该首页大学语言不是推荐更新开始自己文章经济相关觉得影响基本电话公司新闻一起准备注册只有作者朋友",\
   "loginfo":[],\
   "extrainfo":{"file_list":[{"filename":"奇安信终端数据防泄漏系统快速部署手册.docx",\
   "filemd5":"B13CF5B68E3D8E919A8163B6C1539BF2",\
   "file1kmd5":"44D2BC6D9A01EE946C49618701827C60",\
   "file63kmd5":"A011302C04C8854450D8DF3ECB113BA1",\
   "fileremainmd5":"11218160C41067795BEE536885E334A9",\
   "filesize":737337}]}},\
   "callback":"/api/OaChannel/dlpEncryptionUpdate"}' % username
   return post_data

def getXlsData(i):
   try:
      data = xlrd.open_workbook("..\\conf\\user6.xls")
      table = data.sheet_by_index(i)   #第i个sheet
      nrows = table.nrows
      ncols = table.ncols
      excel_list = []
      for row in range(0, nrows):
         for col in range(1):
            cell_value = table.cell(row, col).value
            excel_list.append(cell_value)
      return excel_list
   except Exception, e:
      print str(e)

def approval(ip,port,username):
   storage = StringIO()
   c = pycurl.Curl()
   c.setopt(c.POST,1)
   values = getData(username)
   c.setopt(pycurl.URL,getUrl(ip,port))
   c.setopt(c.POSTFIELDS, values)
   c.perform()
   c.close()
   content = storage.getvalue()
   print content

def rc4crypt(data, key):
   x = 0
   box = range(256)
   for i in range(256):
     x = (x + box[i] + ord(key[i % len(key)])) % 256
     box[i], box[x] = box[x], box[i]
   x = 0
   y = 0
   out = []
   for char in data:
     x = (x + 1) % 256
     y = (y + box[x]) % 256
     box[x], box[y] = box[y], box[x]
     out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

   return ''.join(out)

def salt(username):
   key = 'nZ8ZRGyT3ZdrGHlI'
   s = '{"username": "%s"}' % username
   data = rc4crypt(s,key)
   basedata = base64.b64encode(data)
   print basedata
   return basedata

def login(ip,port,username):
   storage = StringIO()
   c = pycurl.Curl()
   c.setopt(c.POST,1)
   values = salt(username)
   c.setopt(pycurl.URL,getLoginUrl(ip,port))
   c.setopt(c.POSTFIELDS, values)
   c.perform()
   c.close()
   content = storage.getvalue()
   print content

def runAsThread():
   ip = "10.95.27.161"
   port = 85
   username = "zhanglu"
   threads = []

   for i in xrange(1,10):
      i = threading.Thread(target=login(ip,port,username),name='login')
      threads.append(i)

   for t in threads:
      t.start()
      print threading.current_thread()
      t.join()

def runAsProcess():
   for i in range(4):
      p = multiprocessing.Process(target=runAsThread(),name='runAsThread')
      p.start()

if __name__ == "__main__":
   ip = "10.95.27.161"
   port = 85
   #username = "zhanglu"
   #login(ip,port,username)
   #approval(ip,port,username)
   for x in range(0,6):
      for username in getXlsData(x):
         print username
         #approval(ip,port,str(username))
         login(ip,port,username)

   #while 1:
   #   runAsProcess()