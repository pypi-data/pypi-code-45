# -*- coding: UTF-8 -*-
from setuptools import find_packages,setup
setup(
    name = 'xes-lib',
    version = '0.1.13',
    author = 'xes',
    description = '学而思库'.encode("utf-8"),
    packages = find_packages(),
    install_requires = ["requests", "pypinyin"],
    url = 'https://code.xueersi.com'
)