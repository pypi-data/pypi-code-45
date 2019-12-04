import requests
import json
from xes import common
# 获得温度
def air_temp(location, start = 0):
    cookies = common.getCookies()
    headers = {"Cookie": cookies}
    params = {"location": location, "day": start}
    try:
        rep = requests.get("https://code.xueersi.com/api/ai/python_weather/temperature", params=params, headers=headers)
        repDic = json.loads(rep.text)
        return int(repDic["data"])
    except:
        return 0

# 获得风速
def air_speed(location, start = 0):
    cookies = common.getCookies()
    headers = {"Cookie": cookies}
    params = {"location":location,"day":start}
    try:
        rep = requests.get("https://code.xueersi.com/api/ai/python_weather/wind_speed", params=params, headers=headers)
        repDic = json.loads(rep.text)
        return int(repDic["data"])
    except:
        return 0