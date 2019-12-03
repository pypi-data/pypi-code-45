import requests
import json
import threading
import time
import random
from njtest.reptle import nj_ip


class postrequests():

    def __init__(self):
        # self.url = "http://funcal.ibroadlink.com/devicetype/gettoken/"
        self.url = "http://123.207.29.239/testapp/hello/"

        self.headers = {
            'tokenshare': 'tdev_pWXB8VT',
            'wxsessionid': '6514b6213a7dce4e6071f99b5f0a2d6a',
            'from': 'wx',
            'Accept': 'application/json;',
            'Connection': 'close'
        }

        formdata = {"control": {
            "reqbody": "eyJkaXJlY3RpdmUiOnsiaGVhZGVyIjp7Im5hbWVzcGFjZSI6IkROQS5GcmVlQ29udHJvbCIsIm5hbWUiOiJEbmFDb2RlQ29udHJvbCIsImludGVyZmFjZVZlcnNpb24iOiIyIiwibWVzc2FnZUlkIjoiX19NRVNTQUdFSURfVE9fUkVQTEFDRSJ9LCJlbmRwb2ludCI6eyJzY29wZSI6eyJ0eXBlIjoiQmVhcmVyVG9rZW4iLCJ0b2tlbiI6Il9fQUNDRVNTVE9LRU5fVE9fUkVQTEFDRSJ9LCJlbmRwb2ludElkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDA3ODBmNzcwMjgzZDYiLCJjb29raWUiOnsiZGV2bmFtZSI6IllLMzAwMEFIIiwiZGlkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDA3ODBmNzcwMjgzZDYiLCJmYW1pbHlpZCI6IjAwY2NhMTc5ZGYyNTdiMzM4ZGI4MmNiNjVmNTI2MjAxIiwiZmFtaWx5bmFtZSI6IjExMDEiLCJtb2R1bGVpZCI6IiIsIm1vZHVsZXR5cGUiOiIiLCJwaWQiOiIyMDM2NiIsInNkaWQiOiIiLCJzcGlkIjoiIiwidXNlcmlkIjoiMDA2MGJhMjMxNjU1ODAxODljZmY0MmQ2YTRjZjQ3OTAifX0sInBheWxvYWQiOnsiZG5hQ29kZSI6IntcInRwaWRcIjpcIjIwMzY2XCIsXCJzcnZcIjpbXCI0LjEuNTBcIl0sXCJ2YWxzXCI6W1t7XCJ2YWxcIjpcIjFcIixcImlkeFwiOjF9XV0sXCJwYXJhbXNcIjpbXCJwd3JcIl0sXCJhY3RcIjpcInNldFwiLFwicHJvcFwiOlwic3RkY3RybFwifSJ9fX0="
        }}
        self.data = json.dumps(formdata)

    def post(self, ip):
        global a
        try:
            self.proxies = {'http': ip, 'https': ip}
            r = requests.post(self.url, self.data, headers=self.headers, proxies=self.proxies)
            print(r.text)
            a += 1
        except Exception as err:
            print(err)

    def get(self, ip=None):
        global a
        try:
            if ip != None:
                self.proxies = {'http': ip, 'https': ip}
                r = requests.get(self.url, headers=self.headers, proxies=self.proxies, timeout=5)
            else:
                r = requests.get(self.url, headers=self.headers, timeout=5)
            a += 1
            return r.text
        except Exception as err:
            print(err)


def kquan_bf(ip):
    login = postrequests()
    print(login.get())
    # return login.post(ip)
    return login.get()


if __name__ == "__main__":
    try:
        a = 0
        i = 0
        tasks_number = 10  # 开启线程数目
        # get_ip = nj_ip.HeadersSelector()
        # ip_list_kuai = get_ip.get_ip_kuai(5)
        while i < tasks_number:
            # ip = random.randint(1, len(ip_list_kuai))
            t = threading.Thread(target=kquan_bf, args=('',))
            t.start()
            i += 1
        print(a)
    except Exception as err:
        print(err)
