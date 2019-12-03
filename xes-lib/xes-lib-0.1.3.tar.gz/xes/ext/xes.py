#conding:utf-8
import os
import time
import random
import datetime
from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict
from xes.ext import data
import requests
import sys
import json
from xes.common import XesUtils as XesUtils
import time



# https://luosimao.com/service/sms?f=baidu&renqun_youhua=165440
#发送短信
def send_message(mobile, content):

    if not isinstance(mobile, str) and not isinstance(mobile, int):
        raise Exception("参数必须为字符串或者数字")

    #如果输入了逗号，只给第一个手机号发短信
    if isinstance(mobile, str):
        mobile = mobile.split(",")[0]
    params1 = {"mobiles":mobile, "content": content}
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass

    try:
        headers = {"Cookie": cookies}
        rep = requests.get("https://code.xueersi.com/api/ai/python_sms/send", params=params1, headers=headers)
        repDic = json.loads(rep.text)
        if repDic["data"]["state"] == "SUCCESS":
            print("信息正在通过短信运营商发送，大约20S后可查看信息发送结果.....")
            time.sleep(5)
            params2 = {"batchId":repDic["data"]["batchId"], "mobile":mobile}
            for i in range(1,5):
                rep2 = requests.get("https://code.xueersi.com/api/ai/python_sms/report", params=params2)
                repDic2 = json.loads(rep2.text)
                if repDic2["data"]["msg"] != None:
                    return repDic2["data"]["msg"]
                time.sleep(4)
        else:
            return repDic["data"]["msg"]

        return "运营商状态报告超时,信息可能发送失败了"

    except:
        return "运营商状态报告错误,信息可能发送失败了"

# 播放mp3
def play_mp3(music):

    if not isinstance(music, str):
        raise Exception("参数必须为字符串")

    allMusics = {
        "baba.mp3":5,
        "lala.mp3":6,
        "lulu.mp3":6,
        "goodbye.mp3":10,
        "oh no.mp3":7,
        "try again.mp3":6,
        "蔡健雅,MC Hotdog - Easy Come Easy go.mp3":226,
        "胡66 - 浪人琵琶.mp3":224
    }
    if music not in allMusics.keys():
        return "所选音乐不存在，请检查音乐名称拼写是否正确"
    musicUrl = "https://icourse.xesimg.com/programme/python_music/v20190814/" + music
    data = { 'type':'result','desc':'播放音乐','value' : musicUrl }
    XesUtils.InfoTransferAndExchange(data)

    #播放音乐直到停止，sleep音乐的时长
    #冗余1秒的加载延迟
    s = allMusics[music] + 1
    time.sleep(s)
    return ""

# 获得温度
def get_weather_t(location, start = 0):
    params = {"location":location,"day":start}
    try:
        rep = requests.get("https://code.xueersi.com/api/ai/python_weather/temperature", params=params)
        repDic = json.loads(rep.text)
        return int(repDic["data"])
    except:
        return 0

# 获得风速
def get_weather_s(location, start = 0):
    params = {"location":location,"day":start}
    try:
        rep = requests.get("https://code.xueersi.com/api/ai/python_weather/wind_speed", params=params)
        repDic = json.loads(rep.text)
        return int(repDic["data"])
    except:
        return 0


# 获得一串汉字的拼音，返回List
def pinyin(str, ls = None):
    # return lazy_pinyin(str, style=Style.FIRST_LETTER)
    if len(str) < 1:
        return ""

    #黄澄澄拼音错误，特殊处理
    personalized_dict = {
        '黄澄澄': [['huáng'], ['dēng'], ['dēng']],
        '呷茶': [['xiā'], ['chá']]
    }
    load_phrases_dict(personalized_dict)
    la = lazy_pinyin(str)
    if ls == "list":
        return la
    else:
        if len(str) == 1:
            return la[0]
        else:
            return la

# 获得一串汉字的拼音,返回空格隔开的字符串
def pinyin2(str, ls = None):
    # return lazy_pinyin(str, style=Style.FIRST_LETTER)
    if len(str) < 1:
        return ""

    #黄澄澄拼音错误，特殊处理
    personalized_dict = {
        '黄澄澄': [['huáng'], ['dēng'], ['dēng']],
        '呷茶': [['xiā'], ['chá']]
    }
    load_phrases_dict(personalized_dict)
    la = lazy_pinyin(str)
    if ls == "list":
        return la
    else:
        if len(str) == 1:
            return la[0]
        else:
            return " ".join(la)

# 获得一个汉字的拼音
def pinyin_one(str):
    if len(str) < 1:
        return ""
    return lazy_pinyin(str)[0]

# 随机生成一个汉字
def rand_shengpizi():
    return random.choice(data.shengpizi)

# 随机生成一个词
def rand_shengpici():
    return random.choice(data.shengpici)


# 判断是否是成语
def is_chengyu(str):
    if str[0] in data.chengyu:
        if str in data.chengyu[str[0]]:
            return "y"
    return "n"


# 成语接龙
def next_chengyu(str = None):
    if str:
        if str[-1] in data.chengyu:
            return random.choice(data.chengyu[str[-1]])
        else:
            return "n"
    else:
        return random.choice(data.chengyu_base)


# 获取一个垃圾信息关键字列表
def junk_information():
    return ["保险", "投资", "银行卡", "贷款", "免息", "购车", "置房", "中奖", "中大将", "大将", "免服务费", "免费", "理财产品"]
    pass

# 公共交通查询
def public_transport(city, start, endl):
    return [["四号线 -> 1号线", "中关村", "西单", "天安门东", "天安门"],["四号线 -> 2号线 -> 1号线", "中关村", "西直门", "复兴站", "天安门东站", "天安门"]]


def count_info():
    return "大鹏老师，恭喜您，您于2019年5月10日在中国福利彩票中2等奖，688万元，请您于2019年7月前至中国福利彩票处用此密码兑换：例：11798843588。"


# 计算两个日期之间差几天
def date_diff(d1, d2):
    d1 = time.strptime(d1, "%Y-%m-%d")
    d2 = time.strptime(d2, "%Y-%m-%d")
    data1 = datetime.datetime(d1[0], d1[1], d1[2])
    data2 = datetime.datetime(d2[0], d2[1], d2[2])
    da = data1 - data2
    return da.days


if __name__ == '__main__':
    pass
