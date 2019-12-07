import os
import random
import time
import requests
from bs4 import BeautifulSoup as bs


class HeadersSelector(object):
    """
    Header 中缺少几个字段  Host 和 Cookie
    """
    headers_1 = {
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "Referer": "https://www.baidu.com/s?wd=%BC%96%E7%A0%81&rsv_spt=1&rsv_iqid=0x9fcbc99a0000b5d7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=If-None-Match&inputT=7282&rsv_t",
        "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
    }  # 网上找的浏览器
    headers_2 = {
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
        "Accept": "image/gif,image/x-xbitmap,image/jpeg,application/x-shockwave-flash,application/vnd.ms-excel,application/vnd.ms-powerpoint,application/msword,*/*",
        "DNT": "1",
        "Referer": "https://www.baidu.com/link?url=c-FMHf06-ZPhoRM4tWduhraKXhnSm_RzjXZ-ZTFnPAvZN",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }  # window 7 系统浏览器
    headers_3 = {
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": "image/x-xbitmap,image/jpeg,application/x-shockwave-flash,application/vnd.ms-excel,application/vnd.ms-powerpoint,application/msword,*/*",
        "DNT": "1",
        "Referer": "https://www.baidu.com/s?wd=http%B4%20Pragma&rsf=1&rsp=4&f=1&oq=Pragma&tn=baiduhome_pg&ie=utf-8&usm=3&rsv_idx=2&rsv_pq=e9bd5e5000010",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    }  # Linux 系统 firefox 浏览器
    headers_4 = {
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Accept": "*/*",
        "DNT": "1",
        "Referer": "https://www.baidu.com/link?url=c-FMHf06-ZPhoRM4tWduhraKXhnSm_RzjXZ-ZTFnP",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.7,en;q=0.6",
    }  # Win10 系统 firefox 浏览器
    headers_5 = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.baidu.com/link?url=c-FMHf06-ZPhoRM4tWduhraKXhnSm_RzjXZ-",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.7,en;q=0.6",
        "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
    }  # Win10 系统 Chrome 浏览器
    headers_6 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Referer": "https://www.baidu.com/s?wd=If-None-Match&rsv_spt=1&rsv_iqid=0x9fcbc99a0000b5d7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rq",
        "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    }  # win10 系统浏览器

    def select_header(self):
        n = random.randint(1, 6)
        switch = {
            1: self.headers_1,
            2: self.headers_2,
            3: self.headers_3,
            4: self.headers_4,
            5: self.headers_5,
            6: self.headers_6
        }
        headers = switch[n]
        return headers

    def get_ip_kuai(self, cn):
        ip_list_kuai = []
        headers_select = HeadersSelector()
        headers_ip = headers_select.select_header()  # 随机拿去响应头
        for g in range(1, cn + 1):
            time.sleep(1)
            res = requests.get('https://www.kuaidaili.com/free/inha/{}/'.format(g), headers=headers_ip)  # get访问代理网站
            soup = bs(res.text, 'lxml')  # 使用bs4解析
            for i in soup.find_all('td', attrs={'data-title': 'IP'}):  # 遍历查找到的元素
                for j in soup.find_all('td', attrs={'data-title': 'PORT'}):
                    ip_list_kuai.append(i.text + ':' + j.text)
                    break
            self.keep(soup)  # 将解析后手机保存到本地
        for t in ip_list_kuai:  # 输出所有爬到值
            print(t)
        return ip_list_kuai

    def keep(self, soup):
        file = './test.html'
        if not os.path.exists(file):  # 判断文件是否存在
            f = open(file, 'w')  # 创建文件
            f.close()  # 关闭
        with open('./test.html', 'r+', encoding='utf-8')as fd:  # 打开文件
            fd.write(str(soup))  # 写入
        fd.close()
