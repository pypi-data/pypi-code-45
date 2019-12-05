#!/usr/bin/env python
# -*-coding:utf-8 -*-


def ocr_image(filename, service="qq"):
    if service == "qq":
        from easy_ocr.qq import qq_ocr as ocr
    else:
        from easy_ocr.youdao import youdao_ocr as ocr
    return ocr(filename)