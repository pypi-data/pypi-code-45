import time
import datetime

# 获取一个垃圾信息关键字列表
def junk_info():
    return ["保险", "投资", "银行卡", "贷款", "免息", "购车", "置房", "中奖", "中大将", "大将", "免服务费", "免费", "理财产品"]
    pass

# 公共交通查询
def public_trans(city, start, endl):
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