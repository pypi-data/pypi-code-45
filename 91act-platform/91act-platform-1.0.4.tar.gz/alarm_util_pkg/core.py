# -*- coding: utf-8 -*-
from crontab import CronTab
import os
import inspect
import hashlib
import requests
import sys
import pymysql
import getpass
import json
from flask import request, json, session, abort
from functools import wraps
from flask_session import Session
frame = inspect.stack()[1]
index = inspect.getmodule(frame[0])
LOG_FILE_NAME_DEFAULT = "RunTime.log"
FILENAME = os.path.abspath(index.__file__)
LOG_PATH = os.path.dirname(FILENAME) + "/log/"
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
LOG_FILE = LOG_PATH + LOG_FILE_NAME_DEFAULT
APP = None
AUTH_SERVER = None


def build(app, server, project_id, secret_key):
    global AUTH_SERVER, APP
    AUTH_SERVER = server
    APP = app
    APP.config["SESSION_COOKIE_NAME"] = project_id
    APP.config["SESSION_TYPE"] = 'filesystem'
    APP.secret_key = secret_key
    Session(APP)

    @APP.route('/userInfo', methods=['GET'])
    @login_required
    def userInfo():
        userinfo = {}
        for key, value in session.items():
            userinfo[key] = value
        return json.dumps(userinfo)

    @APP.route('/api/logout', methods=['GET'])
    def logOut():
        session.clear()
        return ''


def login_required(f):
    """
    Auth wraps
    :param f:
    :return:
    """

    @wraps(f)
    def verify(*args, **kwargs):
        # 存在局部会话, 放行
        if session.get('isLogin') == True:
            print ("pass")
            return f(*args, **kwargs)
        # 不存在局部会话, 校验
        # check1: 检验是否存在全局会话，并取得ssoToken
        ssoToken = request.args.get('ssoToken')
        headers = {
            'act': request.headers.get('act'),
            'cookie': request.headers.get('cookie')
        }
        if ssoToken is None or ssoToken == '':
            req = requests.get(AUTH_SERVER + '/auth/checkLogin', headers=headers)
            print req.status_code
            if req.status_code != 200:
                return abort(401)
            else:
                ssoToken = json.loads(req.text).get('ssoToken')
        # check2: 携带ssoToken向认证中心注册并取得用户信息
        # 创建临时session, 以获得session.sid
        session['isLogin'] = False
        payload = {
            'appkey': 'alarm',
            'ssoToken': ssoToken,
            'sessionId': session.sid,
            'logoutUrl': request.scheme + '://' + request.host + '/api/logout'
        }
        req = requests.post(AUTH_SERVER + '/auth/verifyToken', headers=headers, data=payload)
        if req.status_code != 200:
            print req.status_code
            session.clear()
            return abort(401)
        else:
            auth_info = json.loads(req.text)

            # 生成局部会话
            for key, value in auth_info.items():
                session[key] = value
            session['isLogin'] = True
            # 放行
            return f(*args, **kwargs)

    return verify


def get_md5_value(value):
    """
    :param value: String
    :return: MD5 result
    """
    my_md5 = hashlib.md5()
    my_md5.update(value)
    my_md5_Digest = my_md5.hexdigest()
    return my_md5_Digest


JOB_ID = get_md5_value(FILENAME)
IS_REGISTER = 0


class SimpleCronControl:
    def __init__(self, url, token):
        self.user_name = getpass.getuser()
        self.my_cron = CronTab(user=self.user_name)
        self.register_flag = 0
        self.work = None
        self.job_state = False
        self.threshold = {}
        self.base_url = url
        self.token = token

    def list_cron(self):
        """
        list all cron jobs of this user
        :return: Return jobs list
        """
        crontab_jobs = list()
        for job in self.my_cron:
            crontab_jobs.append(job)
        return crontab_jobs

    def get_url(self, path):
        return "%s/%s" % (self.base_url, path)

    def send(self, type, message):
        url = self.get_url("message_receiver")
        token = self.token
        req_body = dict()
        req_body["token"] = token
        req_body["type"] = type
        req_body["message"] = message
        job_status_response = requests.post(url=url, json=req_body, timeout=200)
        if job_status_response.status_code != 200:
            msg = job_status_response.json().get("message")
            raise RuntimeError(
                "Can not get expect Response from %s, Code: %s, Msg:%s" % (url, job_status_response.status_code, msg))

    def cron_control(self, command_core="python"):
        """
        You can control your cron job whih this function
        :param setall: cron job's frequency
        :param command_core: basic command for this cron job
        :return:
        """
        url = self.get_url("verify")
        token = self.token
        job_status_response = requests.get(url=url, params={"token": token}, timeout=200)
        if job_status_response.status_code != 200:
            raise RuntimeError("Can not get expect Response from %s, Code: %s" % (url, job_status_response.status_code))
        res = job_status_response.json().get("data")

        if not res.get("job_setall") or not res.get("status"):
            raise RuntimeError("The Response is not expected")

        setall = res.get("job_setall")
        global JOB_ID
        JOB_ID = get_md5_value(token)

        if res.get("status") == "1":
            self.job_state = True

        if res.get("job_threshold"):
            self.threshold = res.get("job_threshold")

        if not self.job_state:
            print("Job Status is False!\nexit!")
            exit()

        if not self.is_register(setall):
            print("Prepare to Register Job")
            job = self.my_cron.new(
                command='%s %s %s >> %s  2>&1 &' % (command_core, FILENAME, " ".join(sys.argv[1:]), LOG_FILE),
                comment="%s|%s" % (JOB_ID, setall))
            job.setall(setall)
            self.my_cron.write()
            print("Register Cron Job Success")
        else:
            print("Job Status:Healthy")
        return self

    def is_register(self, setall):
        """
        Judge the Cron Job has register or not
        :param setall: cron job's frequency
        :return:
        """
        for job in self.my_cron:
            comment_list = job.comment.split("|")
            if comment_list.__len__() == 2 and comment_list[0] == JOB_ID:
                if comment_list[1] != setall:
                    print("Prepare to change Cron Job's Frequency")
                    job.setall(setall)
                    job.set_comment("%s|%s" % (JOB_ID, setall))
                    self.my_cron.write()
                    print("Cron Job's Frequency has changed")

                self.register_flag = 1
                self.work = job
                return True
        return False


class NormalTools:
    """
    Daily tools
    """

    def __init__(self): pass

    def mysql_connector(self, host, port, user, passwd, database, charset='utf8', write_timeout=100):
        return pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=passwd,
                               database=database, charset=charset, write_timeout=write_timeout)
