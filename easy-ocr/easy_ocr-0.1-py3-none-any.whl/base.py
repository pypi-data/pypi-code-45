#!/usr/bin/env python
# -*-coding:utf-8 -*-

class OCR(object):
    def __init__(self, name):
        self.name = name

    def upload_file(self, filename):
        raise NotImplementedError


    def get_result(self):
        raise NotImplementedError