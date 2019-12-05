# -*- coding: utf-8 -*-


def str_dict(str_headers):
    di = []
    try:
        for i in str_headers.split("\n"):
            he = i.split(": ", 1)
            if he != [""]:
                di.append(he)
        return dict(di)
    except ValueError as error:
        print("请把请求类型一行去掉：POST /xxx/xxx/xxx HTTP/1.1" + "\n" + "错误为：%s" % error)

