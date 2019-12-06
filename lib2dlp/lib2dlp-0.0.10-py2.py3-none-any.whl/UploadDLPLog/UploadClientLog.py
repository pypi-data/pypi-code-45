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
flag_list = [2,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20,21]
operflag_list = [1,2,4,5,6,7,12]
num_list = ["a","b","c","d","e","f","g","h","i","j"]
keyword = ["大众市场纸皮书版式","启蒙读物","文摘通报","学位论文","组稿编辑","胶粘装订联动线","青少年读物","文稿代理人","出版日期和书价","会议建议","会议指出","持续进行","会议充分肯定了","正式启动","会议安排","会议倡议","会议要求贯彻落实","各部门依照","整个会议共持续"]


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

#注册终端接口
def getRegeditUrl(ip,port,mid):
   url = "http://%s:%s/api/update_client_info.json?mid=%s&ver=1.0" % (ip,port,mid)
   return url

#上传终端日志接口
def getLogUrl(ip,port,mid):
   url = "http://%s:%s/api/upload_client_log.json?mid=%s&ver=1.0" % (ip,port,mid)
   return url

#生成时间戳
def getTimestamp():
   return int(time.time())

def getRegeditData(username):
   post_data = {"key":"",\
               "os":100729089,\
               "report_ip":"10.18.31.83",\
               "group":"corp.qihoo.net 你好",\
               "user_name":"liyu-s",\
               "osex":0,\
               "computer_name":"%s-PC" % username,\
               "mac":"50:40:81:36:52:4c",\
               "ie_ver":"8.0.7601.17514",\
               "type":0,\
               "sys_space":36129,\
               "skylar_mid":"123456781234567812345678123abcde"}
   return post_data

def getLogData(flag,mid,pkg_guid,filename,operflag,ipaddr,username):#flag代表日志通道类型,opfalg代表处理动作
   #post_data = {"logdata":{"Logamount":1,"content":[{"density":10,"dstuid":"d400b35b-d152-4521-9501-aeb46e557a34","eventid":flag,"filename":"test.pdf","ip":"","location":2,"logtime":getTimestamp(),"note":"{\n    \"type\": 64,\n    \"result\": [\n        {\n            \"datahead\": \"ftp\\r\\n上海环境组织\\n\\n【VSD】\\n\\n\",\n            \"data\": \"生涯规划\",\n            \"datatail\": \"\\n\\n重返17岁\\n\\n• 如果能重来一回\\n\\n生涯规划\\n\\n\",\n            \"pos\": 0,\n            \"type\": 64,\n            \"density\": 0\n        },\n        {\n            \"datahead\": \"ftp\\r\\n上海环境组织\\n\\n【VSD】\\n\\n生涯规划\\n\\n重返17岁\\n\\n• 如果能重来一回\\n\\n\",\n            \"data\": \"生涯规划\",\n            \"datatail\": \"\\n\\n\",\n            \"pos\": 0,\n            \"type\": 64,\n            \"density\": 0\n        }\n    ],\n    \"info\": {\n        \"auditfile\": \"C:\\\\ProgramData\\\\{DFBE0C54-D918-4E74-9F88-F1BCF4728895}\\\\st76A1.tmp\\\\ftp\",\n        \"processname\": \"C:\\\\Windows\\\\explorer.exe\",\n        \"auditfilemd5\": \"d44d57c3350263b8a2e6202bbc1552ff\",\n        \"dest\": \"test.pdf\",\n        \"ftpcommandid\": \"35552\",\n        \"ftpconvertfilename\": \"test.pdf\",\n        \"ftpfilename\": \"test.pdf\",\n        \"ip\": \"10.95.27.164\",\n        \"port\": \"50136\",\n        \"sourceport\": \"63700\",\n        \"uuid\": \"c9f4ecd5-129b-4ae9-a7f0-cf14eae8e83c\",\n        \"groupname\": \"DLP_关键字\",\n        \"keyword\": \"生涯规划\",\n        \"density\": 10\n    }\n}","opflag":4,"srcuid":"","user_name":""}],"sessionid":123},"module":"dlp_loginfo","pkg_guid":"ce062d9a78644008bed15cee335b9e9e","pkg_type":"dlp","user_name":""}
   post_data = {"logdata":{"Logamount":1,\
               "content":[{"density":10,\
               "dstuid":"d400b35b-d152-4521-9501-aeb46e557a34",\
               "eventid":flag,\
               "filename":"%s.pdf" % filename,\
               "ip":"%s" % ipaddr,\
               "location":2,\
               "logtime":getTimestamp(),\
               "note":"{\n    \"type\": 64,\
               \n    \"result\": [\n        {\n            \"datahead\": \"ftp\\r\\n上海环境组织\\n\\n【VSD】\\n\\n\",\
               \n            \"data\": \"生涯规划\",\
               \n            \"datatail\": \"\\n\\n重返17岁\\n\\n• 如果能重来一回\\n\\n生涯规划\\n\\n\",\
               \n            \"pos\": 0,\
               \n            \"type\": 64,\
               \n            \"density\": 0\n        },\
               \n        {\n            \"datahead\": \"ftp\\r\\n上海环境组织\\n\\n【VSD】\\n\\n生涯规划\\n\\n重返17岁\\n\\n• 如果能重来一回\\n\\n\",\
               \n            \"data\": \"生涯规划\",\
               \n            \"datatail\": \"\\n\\n\",\
               \n            \"pos\": 0,\
               \n            \"type\": 64,\
               \n            \"density\": 0\n        }\n    ],\
               \n    \"info\": {\n        \"auditfile\": \"C:\\\\ProgramData\\\\{DFBE0C54-D918-4E74-9F88-F1BCF4728895}\\\\st76A1.tmp\\\\ftp\",\
               \n        \"processname\": \"C:\\\\Windows\\\\explorer.exe\",\
               \n        \"auditfilemd5\": \"d44d57c3350263b8a2e6202bbc1552ff\",\
               \n        \"dest\": \"test.pdf\",\
               \n        \"ftpcommandid\": \"35552\",\
               \n        \"ftpconvertfilename\": \"test.pdf\",\
               \n        \"ftpfilename\": \"test.pdf\",\
               \n        \"ip\": \"10.95.27.164\",\
               \n        \"port\": \"50136\",\
               \n        \"sourceport\": \"63700\",\
               \n        \"uuid\": \"c9f4ecd5-129b-4ae9-a7f0-cf14eae8e83c\",\
               \n        \"groupname\": \"DLP_关键字\",\
               \n        \"keyword\": \"生涯规划\",\
               \n        \"density\": 10\n    }\n}",\
               "opflag":operflag,"srcuid":"",\
               "user_name":"%s" % username}],\
               "sessionid":123},"module":"dlp_loginfo",\
               "pkg_guid":"%s" % pkg_guid,\
               "pkg_type":"dlp",\
               "user_name":"%s" % username}
   return post_data

def regeditEndpoint(ip,port,mid,username):
   head = {"Content-Type": "application/x-www-form-urlencoded"}
   r = requests.post(url=getRegeditUrl(ip,port,mid),headers=head,data=json.dumps(getRegeditData(username)))
   if r.status_code == 200:
      print r.text
      return 1
   else:
      print r.text
      return 0

def uploadLog(ip,port,mid,pkg_guid,flag,filename,operflag,ipaddr,username):
   head = {"Content-Type": "application/x-www-form-urlencoded"}
   r = requests.post(url=getLogUrl(ip,port,mid),headers=head,data=json.dumps(getLogData(flag,mid,pkg_guid,filename,operflag,ipaddr,username)))
   if r.status_code == 200:
      print r.text
      return 1
   else:
      print r.text
      return 0

def writeExcel(list):
   f = xlwt.Workbook()
   faker = Faker("zh_CN")
   sheet1 = f.add_sheet(u"mid%s" % list,cell_overwrite_ok=True)

   row0 = [u"mid"]
   #写第一行
   for i in range(0,len(row0)):
      sheet1.write(0,i,row0[i])
   
   #设置第一列列宽
   first_col=sheet1.col(0)
   first_col.width = 500*18 #8个英文字符

   #写第一列
   for i in range(0,10000):
      sheet1.write(i+1,0,list+genStr(30)+list)

   f.save("..\\Result\\mid_"+list+".xls")
   return True

def genExcelData():
   #生成多少万数据由letter_list决定
   for i in letter_list:
      writeExcel(i)

def writeMidTxt(text1,text2):
   f = open('../conf/mid.txt','a')
   f.write("%s" % timeget())
   f.write("\t%s" % text1)
   f.writelines("\t%s\n" % text2)
   f.close()

def getExcelData(i,column):#column代表取excel第几列的值
   try:
      #data = xlrd.open_workbook("conf\\mid6.xls")#mid数据
      #data = xlrd.open_workbook("conf\\user6.xls")#注册用户和上传日志同时进行
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

def getExcelUsernameData(i,column):#column代表取excel第几列的值
   try:
      data = xlrd.open_workbook("../conf/username.xls")#注册用户和上传日志同时进行

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

#生成10万用户名（用户名不重复），每个sheet有1万用户
def CreateExcelNum():
   faker = Faker("zh_CN")
   try:
      style = xlwt.XFStyle()
      font = xlwt.Font()
      font.name = 'Times New Roman'
      font.bold = True
      style.font = font
      filename = xlwt.Workbook(encoding = 'UTF-8')
      for i in num_list:#需要更多的用户，需要修改num_list
         sheet = filename.add_sheet("test%s" % i)
         #设置第一列列宽
         first_col=sheet1.col(0)
         first_col.width = 500*6 #8个英文字符
         for j in range(0,10000):
            sheet.write(j,0,faker.user_name()+str(j)+str(i),style)
      filename.save("..\\Result\\user10.xls")
      return True
   except Exception,e:
      print(str(e))
      return False

def readColumn1():
   mid_list = []
   for x in range(0,2):
      for mid in getExcelData(0,1):#第x个sheet
         mid_list.append(mid)
   return mid_list

def readColumn2():
   username_list = []
   for username in getExcelUsernameData(0,1):
      username_list.append(username)
   return username_list

def pkcs5_unpad(s):
   return s[0:-ord(s[-1])]

def decrypt(enc, aeskey):
   enc = base64.b64decode(enc)
   iv = enc[:16]
   cipher = AES.new(aeskey, AES.MODE_CBC, iv)
   return pkcs5_unpad(cipher.decrypt(enc[16:]))

def getDec(enc):
   aeskey = "aes_key_16_bytes"
   #enc = "3X0rCrJDNTSHe6ClJWAz8bsmX2tVPbH/dImKJkvf2AS2Z9uh220ObxhtbZOt3mMoJxL8IpnBvUOQbKlqxmq85ieli7lQkgxSgzhKweWlruk="

   dec = decrypt(enc,aeskey)
   #print dec
   return dec

def getToken(ip,odpport):
   head = {"Content-Type": "application/x-www-form-urlencoded"}
   url = 'http://%s:%s/oauth/token' % (ip,odpport)
   params = {"client_id":"skylar6_ent_odp",\
            "grant_type":"password",\
            "username":"admin",\
            "password":"www.360.cn"}
   response = requests.get(url=url, params=params, headers=head).text
   print getDec(response)
   return json.loads(getDec(response)).get('access_token')

def getOdpDLP(ip,odpport,limt,offst):
   head = {"Content-Type": "application/x-www-form-urlencoded"}
   url = 'http://%s:%s/v1/dlp/rptsvc_antileakage' % (ip,odpport)
   params = {"access_token":"0f250302-d4c5-4a7f-8430-d793e95f6ab8",\
            "list_type":"channelProtect",\
            "tbg":"1573401600",#2019/11/11 00:00:00\
            "ted":"1573487999",#2019/11/11 23:59:59\
            "search_content":"",\
            "limit":"%s" % limt,\
            "offset":"%s" % offst,\
            "module":""}
   response = requests.get(url=url, params=params, headers=head).text
   return response

if __name__ == "__main__":
   ip = "10.95.27.161"
   port = 80
   odpport = 8888
   limit = 200

   '''
   while 1:
      limit_list = [20,50,100,200,500,1000,2000,5000,10000]
      #【ODP】DLP日志列表接口调用
      for limit in limit_list:
         i = 0
         while i < 10000:
            start = 0
            end = 0
            start = time.time()
            content = getDec(getOdpDLP(ip,odpport,limit,random.randint(1,10000)))
            if json.loads(content).get('reason') == 'success':
               end = time.time()
               writeMidTxt(limit,(end-start))
               print "成功——>%ss" % (end-start)
            else:
               print "失败——>\n%s" % content
            #time.sleep(0.1)
            i = i + 1
      shutil.copyfile("../conf/mid.txt","../conf/mid_%s.txt" % timeget())
   '''

   #生成10万用户到xls
   #CreateExcelNum()

   #上传日志
   
   faker = Faker("zh_CN")

   while 1:
      for md5 in getExcelData(0,1):
         ret = uploadLog(ip,port,md5,genStr(32),faker.random_element(flag_list),faker.random_element(keyword),faker.random_element(operflag_list),faker.ipv4(),faker.random_element(readColumn2()))
         if ret == 1:
            print "%s\t\t——>上传终端日志成功" % timeget()
         else:
            print "%s\t\t——>上传终端日志成功" % timeget()
   
   #注册终端
   '''
   for username in readColumn2():
      md5 = genStr(32)
      print username
      writeMidTxt(username,md5)

      ret1 = regeditEndpoint(ip,port,md5,username)
      #time.sleep(3)
      if ret1 == 1:
         print "%s\t\t——>注册终端成功" % timeget()
      else:
         print "%s\t\t——>注册终端失败" % timeget()

      ret2 = uploadLog(ip,port,md5,genStr(32),faker.random_element(flag_list),faker.random_element(keyword),faker.random_element(opflag_list),faker.ipv4(),faker.random_element(readColumn2()))
      #time.sleep(3)
      if ret2 == 1:
         print "%s\t\t——>上传终端日志成功" % timeget()
      else:
         print "%s\t\t——>上传终端日志成功" % timeget()
   '''