#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import win32com.client as win32
import win32api
import psutil
import os
import subprocess
import sys
import getopt
 
# Drafting and sending email notification to senders. You can add other senders' email in the list
def send_notification():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'datasec360@126.com', 
    #mail.Subject = 'Sent through Python'
    #mail.body = 'This email alert is auto generated. Please do not respond.'
    mail.Subject = u'张秀昌发送的带附件的测试邮件'
    mail.Body = u'王宝强先生！恭喜您查收到该邮件'
    mail.HTMLBody = u'<h1 style="text-algin:center">王宝强先生！恭喜您查收到该邮件</h1><span style="color:red">详情如下：</span><br><img src="cid:zg">' #this field is optional
    mail.Send()
     
# Open Outlook.exe. Path may vary according to system config
# Please check the path to .exe file and update below
     
def open_outlook():
    try:
    	win32api.ShellExecute(0,'open',r'C:\Program Files\Microsoft Office\Office15\OUTLOOK.EXE','','',1)
    	time.sleep(5)
        #subprocess.call(['C:\Program Files\Microsoft Office\Office15\Outlook.exe'])
        #os.system("C:\Program Files\Microsoft Office\Office15\Outlook.exe");
    except:
        print("Outlook didn't open successfully")

def send():
	# Checking if outlook is already opened. If not, open Outlook.exe and send email
	for item in psutil.pids():
	    p = psutil.Process(item)
	    if p.name() == "OUTLOOK.EXE":
	        flag = 1
	        break
	    else:
	        flag = 0

	if (flag == 1):
	    send_notification()
	else:
	    open_outlook()
	    send_notification()


if __name__ == "__main__":
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -s ：发送不带附件的邮件\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hsv", ["help", "output="])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-s", "1"):
            send()  
        elif cmd in ("-v", "--version"):
            print("version 1.0")