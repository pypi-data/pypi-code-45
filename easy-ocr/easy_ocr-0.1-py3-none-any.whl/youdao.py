#!/usr/bin/env python
# -*-coding:utf-8 -*-
import base64
import mimetypes
import requests
from easy_ocr.base import OCR


class YouDaoOCR(OCR):
    url = "https://aidemo.youdao.com/ocrapi1"

    def upload_file(self, filename):
        self.filename = filename

    def get_result(self):
        result = []
        file_types = mimetypes.guess_type(self.filename)[0]
        with open(self.filename, "rb") as f:
            data = f.read()
        f_data = base64.b64encode(data).decode("utf-8")
        params = {
            "imgBase":"data:{},base64,{}".format(file_types, f_data),
            "lang":"auto",
            "company":""
        }
        headers = {
            "Host": "aidemo.youdao.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Origin": "http://ai.youdao.com",
            "Referer": "http://ai.youdao.com/product-ocr.s"
        }
        try:
            req = requests.post(self.url, data=params, headers=headers)
        except Exception as e:
            print(e)
        else:
            response = req.json()
            code = response.get("errorCode",1)
            code = int(code)
            if code == 0:
                lines = response.get("lines",[])
                for line in lines:
                    word = line.get("words")
                    result.append(word)
        return result

def youdao_ocr(filename):
    ocr = YouDaoOCR("youdao")
    ocr.upload_file(filename)
    return ocr.get_result()