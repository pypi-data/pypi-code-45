import json
from urllib import parse
import random
import aiohttp
import asyncio
resps = []


# 为所有的请求构建一个session
async def main(urls,pool,method,params=None, datas=None, headers=None, cookies=None, proxy_str=None, timeout=None): # 启动
    try:
        if isinstance(headers,str):
            headers = str_to_dict(headers)
        if isinstance(params,str):
            params = str_to_dict(params)
        # 如果url是字符串,把其加到列表里
        if isinstance(urls,str):
            urls = [urls,]  # 如果urls 是字符串,放到列表里
            # print(urls,'当前url列表')
        sem = asyncio.Semaphore(pool)  # 限制同时请求数量 ,是一个semaphore对象

        async with aiohttp.ClientSession(cookies=cookies) as session:  # 给所有请求,创建同一个session
            tasks = []
            for url in urls:  # url 列表
                if url:
                    tasks.append(control_sem(sem,url,session,method,params=params,datas=datas,headers=headers, proxy_str=proxy_str, timeout=timeout)) # 放入tasks
            await asyncio.wait(tasks)  # 这个地方写错位置了
    except:
        pass


async def control_sem(sem, url, session,method, params=None, datas=None, headers=None, proxy_str=None, timeout=None):
    try:
        async with sem: # 在这个对象下
            await fetch(url,session,method,params=params, datas=datas, headers=headers, proxy_str=proxy_str, timeout=timeout)
    except:
        pass


async def fetch(url,session, method,params=None, datas=None, headers=None, proxy_str=None, timeout=None):
    try:
        '''
            request 函数,被get post 调用,接收多个参数
            1. 判断method
        '''
        if method in 'GETS':  # 发送url ,返回响应数据
            #  使用的 get
            async with session.get(url,params=params,headers=headers,proxy=proxy_str,timeout=timeout) as resp:
                body = await resp.read()
                resp = Myresponse(body,resp)
                resps.append(resp)
        elif method == 'POST':
            # aiohttp 的post 数据是data 不是datas
            async with session.post(url,data=datas,headers=headers,proxy=proxy_str,timeout=timeout) as resp:
                body = await resp.read()
                resp = Myresponse(body,resp)
                resps.append(resp)
    except:
        pass


def get(url, params=None, datas=None, headers=None, cookies=None, proxy_str=None, timeout=None, pool=100):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls=url,method='GET',params=params,datas=datas,headers=headers,cookies=cookies,proxy_str=proxy_str,timeout=timeout,pool=pool))
    try:
        return resps[0]
    except:
        return []


def gets(urls, params=None, datas=None, headers=None, cookies=None, proxy_str=None, timeout=None, pool=100):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls=urls, method='GETS', params=params, datas=datas, headers=headers, cookies=cookies,proxy_str=proxy_str, timeout=timeout, pool=pool))
    return resps


def post(url, params=None, datas=None, headers=None, cookies=None, proxy_str=None, timeout=None, pool=100):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls=url, method='POST', params=params, datas=datas, headers=headers, cookies=cookies,proxy_str=proxy_str, timeout=timeout, pool=pool))
    try:
        return resps[0]
    except:
        return []


class Myresponse(object):
    def __init__(self,body, resp):
        self.body = body
        self.resp = resp
        self.results = []

    @property
    def text(self):  # text 类型
        try:
            return self.body.decode('utf-8')
        except:
            return self.body.decode('gbk')
    @property
    def content(self):
        return self.body

    def json(self,value):
        text = json.loads(self.body)
        get_v(text,value)
        if len(results) == 1:
            return results[0]  # 如果只有一个元素,直接返回元素,不返回列表套一个元素
        else:
            return results
    @property
    def cookies(self):
        print(self.resp.cookies)
        return self.resp.cookies
    @property
    def headers(self):
        return self.resp.headers
    @property
    def url(self):
        return self.resp.url
    @property
    def status(self):
        return self.resp.status


results = []


def get_v(text, value):
    if not text:
        return results
    if isinstance(text, dict):
        try:
            results.append(text[value])
            if not isinstance(text[value],str):  # 这个地方要考虑到 列表的值也可能是字典
                get_v(text[value],value)
        except:
            for k, v in text.items():
                get_v(text[k], value)
    if isinstance(text, list):
        result = []
        for t in text:
            if t == value:
                result.append(t)
                results.append(t)
        if result:
            return results
        else:
            for i in text:
                get_v(i, value)


def str_to_dict(str1):
    headers = {}
    for i in str1.split('\n'):
        try:
            l = i.split(':', 1)
            headers[l[0].strip()] = l[1].strip()
        except:
            pass
    return headers


def ua():
    user_agent_ = [
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",

        # 各种移动端

        # IPhone
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPod
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPAD
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # Android
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # QQ浏览器 Android版本
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # Android Opera Mobile
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        # Android Pad Moto Xoom
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        # BlackBerry
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        # WebOS HP Touchpad
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        # Nokia N97
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        # Windows Phone Mango
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        # UC浏览器
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        # UCOpenwave
        "Openwave/ UCWEB7.0.2.37/28/999",
        # UC Opera
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"

    ]
    return random.choice(user_agent_)




