#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os
import smtplib
import email
import time
from faker import Factory
from faker import Faker
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr
reload(sys)
sys.setdefaultencoding("utf-8")

def addAttch(path):
   faker = Faker("zh_CN")
   SUBJECT = '%s发送的邮件' % faker.name()
   FROM = 'datasec360@126.com'
   PASSWORD = '1234qwer'
   To = 'datasec360@163.com'
   msg = MIMEMultipart('related')

   # 创建一个用于发送文本的MIMEText对象
   content = faker.text(max_nb_chars=2048) + "参考资料"
   msg_text = MIMEText(content,_subtype='plain',_charset='utf-8')
   msg.attach(msg_text)

   os.chdir(path)
   dir = os.getcwd()

   # 将xls作为附件添加到邮件中
   # 创建MIMEText对象，保存txt文件
   for fn in os.listdir(dir):
      attach = MIMEText(open(fn,'rb').read())
      # 指定当前文件格式类型
      attach['Content-type'] = 'application/octet-stream'
      # 配置附件显示的文件名称,当点击下载附件时，默认使用的保存文件的名称
      # gb18030 qq邮箱中使用的是gb18030编码，防止出现中文乱码
      #attach['Content-Disposition'] = 'attachment;filename="我是tupian附件.txt"'.decode('utf-8').encode('gb18030')
      attach['Content-Disposition'] = 'attachment;filename=' + fn
      # 把附件添加到msg中
      msg.attach(attach)
   # 设置必要请求头信息
   msg['From'] = FROM
   msg['To'] = To
   msg['Subject'] = SUBJECT

   return msg

def sendMail(msg):
   HOST = 'smtp.126.com'
   FROM = 'datasec360@126.com'
   PASSWORD = '1234qwer'
   To = 'datasec360@163.com'
   ret = True
   try:
      # 发送邮件
      server = smtplib.SMTP() # SMTP协议默认端口是25
      server.connect(HOST, 25)
      #server.ehlo() 
      #server.starttls()  #开启加密传输
      #server.set_debuglevel(0)#打印出和SMTP服务器交互的所有信息，不想打印就设置为0
      server.login(FROM,PASSWORD)#登录服务器
      server.sendmail(FROM,To,msg.as_string())
      server.quit()
      print "SMTP OK" 
      return ret
   except Exception,e:
      print e
      print "SMTP False" 
      return False
   return

if __name__ == "__main__":
    path = "data\\smtp"
    msg = addAttch(path)
    sendMail(msg)