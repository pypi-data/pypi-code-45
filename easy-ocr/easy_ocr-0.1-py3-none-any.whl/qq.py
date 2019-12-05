#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
from easy_ocr.base import OCR


class QQ_OCR(OCR):
    url = "https://ai.qq.com/cgi-bin/appdemo_generalocr?g_tk=5381"

    def upload_file(self, filename):
        self.filename = filename

    def get_result(self):
        result = []
        headers = {"Host": "ai.qq.com",
                   "Referer": "https://ai.qq.com/product/ocr.shtml"
                   }
        with open(self.filename, "rb") as f:
            params = {"image_file": f}
            try:
                req = requests.post(self.url, files=params, headers=headers)
            except Exception as e:
                print(e)
            else:
                data = req.json()
                msg = data.get("msg")
                if msg == "ok":
                    item_list = data.get("data", {}).get("item_list", [])
                    for item in item_list:
                        code = item.get("itemstring")
                        result.append(code)
            finally:
                return result


def qq_ocr(filename):
    ocr = QQ_OCR("qq")
    ocr.upload_file(filename)
    return ocr.get_result()