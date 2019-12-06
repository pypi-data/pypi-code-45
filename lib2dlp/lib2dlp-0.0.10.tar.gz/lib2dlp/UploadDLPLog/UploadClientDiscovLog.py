#!/usr/bin/python
# -*- coding: UTF-8 -*-

from faker import Factory
from faker import Faker
from faker.providers import BaseProvider
from Crypto.Cipher import AES
import base64
import time
import string
import random
import os.path
import shutil
import requests
import urllib2
import urllib
import xlwt
import xlrd
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


letter_list = ["a","b","c","d","e","f"]
methd_list = [0,1,3,4,5]
operflag_list = [1,2,3,4]
num_list = ["a","b","c","d","e","f","g","h","i","j"]
keyword = ["大众市场纸皮书版式","启蒙读物","文摘通报","学位论文","组稿编辑","胶粘装订联动线","青少年读物","文稿代理人","出版日期和书价","会议建议","会议指出","持续进行","会议充分肯定了","正式启动","会议安排","会议倡议","会议要求贯彻落实","各部门依照","整个会议共持续"]
ext_list = ["doc","docx","xls","xlsx","ppt","pptx","pdf"]


def timeget():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def genCode():
   return ''.join(random.sample(string.ascii_lowercase + string.digits, 31))

def genStr(num):
   H = '0123456789abcdef'
   salt = ''
   for i in range(num):
      salt += random.choice(H)
   return salt

def genMac():
   faker = Faker("zh_CN")
   return str(faker.mac_address())

def getExcelData(i,column):#column代表取excel第几列的值
   try:
      data = xlrd.open_workbook("../conf/md5.xls")

      table = data.sheet_by_index(i)   #第i个sheet
      nrows = table.nrows
      ncols = table.ncols
      excel_list = []
      for row in range(0, nrows):
         for col in range(column):
            cell_value = table.cell(row, col).value
            excel_list.append(cell_value)
      return excel_list
   except Exception, e:
      print str(e)

#上传终端日志接口
def getLogUrl(ip,port,mid):
   url = "http://%s:%s/api/upload_client_log.json?mid=%s&ver=1.0" % (ip,port,mid)
   return url

#生成时间戳
def getTimestamp():
   return int(time.time())

def getLogData(methd,operflag,filename,ext):
   post_data = {"module":"dlp_archivefile","guid":"da53890555c24da0bc","logdata":[{"content":[{"filename":"%s.%s" % (filename,ext),"filemd5":"94fcd11d5c472c5b1c76b5aabc43adf7","lastmodify":getTimestamp(),"matchedinfo":"{}","filesize":random.randint(1,10240),"method":methd,"location":2,"scandate":getTimestamp(),"opflag":operflag}],"serial":1}]}
   return post_data

def uploadLog(ip,port,mid,methd,operflag,filename,ext):
   head = {"Content-Type": "application/x-www-form-urlencoded"}
   r = requests.post(url=getLogUrl(ip,port,mid),headers=head,data=json.dumps(getLogData(methd,operflag,filename,ext)))
   if r.status_code == 200:
      print r.text
      return 1
   else:
      print r.text
      return 0

if __name__ == "__main__":
   ip = "10.95.27.161"
   port = 80

   faker = Faker("zh_CN")
   while 1:
      for md5 in getExcelData(0,1):
         ret = uploadLog(ip,port,md5,faker.random_element(methd_list),faker.random_element(operflag_list),faker.random_element(keyword),faker.random_element(ext_list))
         time.sleep(0.1)
         if ret == 1:
            print "%s\t\t——>上传终端数据发现日志成功" % timeget()
         else:
            print "%s\t\t——>上传终端数据发现日志成功" % timeget()