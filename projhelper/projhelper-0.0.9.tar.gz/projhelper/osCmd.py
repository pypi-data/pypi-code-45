#!/usr/bin/python
# -*- coding: utf-8 -*-

file_info = '''
 @Time    : 18/1/7 13:34
 @Author  : oujianhua
 @mail  : ojhtyy@163.com
 '''
import locale
import commands
import subprocess
from log import logger

def runCmdBak(cmd): #flag标记数据来源, 如果是conf文件则执行一次OS命令后,把结果存起来, 发送ZABBIX不传flag 不处理
    #print(cmd)
    code,output=commands.getstatusoutput(cmd)
    return output,code

def runCmd(cmd): #flag标记数据来源, 如果是conf文件则执行一次OS命令后,把结果存起来, 发送ZABBIX不传flag 不处理
    #print(cmd)
    #logger.info(cmd)
    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except:
        return None, p.returncode
    else:
        output, err = p.communicate()
        if len(err)>0:
            logger.error("get error:%s when run cmd: %s " % (err.decode(locale.getdefaultlocale()[1]), cmd))
            raise Exception("run cmd error")
    #return output+err, p.returncode
    return output.decode(locale.getdefaultlocale()[1]), p.returncode


def runCmdWithDir(cmd,dir): #flag标记数据来源, 如果是conf文件则执行一次OS命令后,把结果存起来, 发送ZABBIX不传flag 不处理
    #print(cmd)
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,cwd=dir)
    except BaseException as e:
        return None, p.returncode
    else:
        output, code = p.communicate()
    return output.decode(locale.getdefaultlocale()[1]), p.returncode
