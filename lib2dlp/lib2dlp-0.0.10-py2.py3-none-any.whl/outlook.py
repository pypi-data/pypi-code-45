#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pathlib import Path
from datetime import date
import pandas as pd
import win32com.client as win32
import win32api
import os
import time
import socket

class defOutlook:
	def outlook(self):
		ret = True
		try:
			#win32api.ShellExecute(0,'open',r'C:\Program Files\Microsoft Office\Office15\OUTLOOK.EXE','','',1)
			#time.sleep(5)
			outlook = win32.Dispatch('outlook.application')
			mail = outlook.CreateItem(0)
			mail.To = 'datasec360@126.com'
			mail.Subject = u'张秀昌发送的带附件的测试邮件'
			mail.Body = u'王宝强先生！恭喜您查收到该邮件'
			mail.HTMLBody = u'<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">' #this field is optional
			# To attach a file to the email (optional):
			#attachment  = 'menu.py'
			#mail.Attachments.Add(attachment)
			mail.Send()
			#time.sleep(5)
			#os.system("taskkill /F /IM OUTLOOK.EXE")
			print "OUTLOOK OK" 
			return ret
		except Exception,e:
			print e
			print "OUTLOOK False" 
			return False
		return

	def openOutLook(self):

		to_email = """
		zhangxiuchang@tell.com
		"""

		cc_email = """
		yangshuguang@tell.com
		"""

		out_file = Path.cwd() / "file\\test.docx"

		outlook = win32.gencache.EnsureDispatch('Outlook.Application')
		new_mail = outlook.CreateItem(0)

		new_mail.Subject = "{:%m/%d} Report Update".format(date.today())

		new_mail.To = to_email
		new_mail.CC = cc_email

		attachment1 = out_file

		new_mail.Attachments.Add(Source=str(attachment1))

		new_mail.Display(True)

		new_mail.Send()

		outlook.Quit()

	def get_host_ip(self):
		"""
		查询本机ip地址
		:return: ip
		"""
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 80))
			ip = s.getsockname()[0]
		finally:
			s.close()
		return ip


if __name__ == "__main__":
	app = defOutlook()

	app.get_host_ip()
	print socket.gethostname()
	app.openOutLook()