# -*- coding: utf-8 -*-
from crontab import CronTab
import os
import inspect
import hashlib
import requests

frame = inspect.stack()[1]
index = inspect.getmodule(frame[0])
LOG_FILE_NAME_DEFAULT = "RunTime.log"
# FILENAME = index.__file__
FILENAME = os.path.abspath(index.__file__)
LOG_PATH = os.path.dirname(FILENAME) + "/log/"
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
LOG_FILE = LOG_PATH + LOG_FILE_NAME_DEFAULT


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
    def __init__(self, user_name):
        self.user_name = user_name
        self.my_cron = CronTab(user=self.user_name)
        self.register_flag = 0
        self.work = None
        self.job_state = False

    def list_cron(self):
        """
        list all cron jobs of this user
        :return: Return jobs list
        """
        crontab_jobs = list()
        for job in self.my_cron:
            crontab_jobs.append(job)
        return crontab_jobs

    def cron_control(self, url, token, command_core="python"):
        """
        You can control your cron job whih this function
        :param setall: cron job's frequency
        :param command_core: basic command for this cron job
        :return:
        """
        job_status_response = requests.get(url=url, params={"token": token}, timeout=20)
        if job_status_response.status_code != 200:
            raise RuntimeError("Can not get expect Response from %s, Code:%s" % (url, job_status_response.status_code))
        res = job_status_response.json()

        if not res.get("setall") or not res.get("status"):
            raise RuntimeError("The Response is not expected")

        setall = res.get("setall")
        global JOB_ID
        JOB_ID = get_md5_value(token)

        if res.get("status") == "1":
            self.job_state = True

        if not self.job_state:
            print("Job Status is False!")
            exit()

        if not self.is_register(setall):
            print("Prepare to Register Job")
            job = self.my_cron.new(command='%s %s >> %s  2>&1 &' % (command_core, FILENAME, LOG_FILE),
                                   comment="%s|%s" % (JOB_ID, setall))
            job.setall(setall)
            self.my_cron.write()
            print("Register Cron Job Success")
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
                    job.setall(setall)
                    job.set_comment("%s|%s" % (JOB_ID, setall))
                    self.my_cron.write()
                    print("Cron Job's Frequency has changed")

                self.register_flag = 1
                self.work = job
                return True
        return False
