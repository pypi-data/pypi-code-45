#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 执行包：run regression cases begin with "tezign*.json"

import os
import autox.core.myemail as email
import autox.util.common as common

report = None

if os.path.exists(os.getcwd()+'/log'):

    # 每次执行前清空错误日志
    if os.path.isfile(os.getcwd()+'/log/error.log'):
        f = open(os.getcwd()+'/log/error.log', 'r+')
        f.truncate()
    else:
        pass
else:
    os.mkdir(os.getcwd()+'/log')

report_path = os.getcwd()+'/report'

if os.path.exists(report_path):
    if os.path.isfile(report_path + '/测试报告.html'):
        os.remove(report_path + '/测试报告.html')
    else:
        pass
else:
    os.mkdir(os.getcwd()+'/report')

if os.path.exists(os.getcwd()+'/model'):
    pass
else:
    os.mkdir(os.getcwd()+'/model')

regTest = common.MyRegression()


def run(scenario_list):
    global report
    report = regTest.build_report(scenario_list)
    return report
    # email.email(report)












