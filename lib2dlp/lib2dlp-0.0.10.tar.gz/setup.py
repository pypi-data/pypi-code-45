#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: luoxianghui
# Mail: lxh_xwj@126.com
# Created Time: 2019-12-05 18:25:34 PM
#############################################

from setuptools import setup, find_packages
import io
import os

package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name = "lib2dlp",
    version = "0.0.10",
    keywords = ("pip","dlp","dlplib","libdlp"),
    description = "Data Loss Prevention (DLP) TEST",
    long_description = readme,
    license = "Apache 2.0",

    url = "https://pypi.org/project/lib2dlp/#files",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Linux; Windows",
    author = "luoxianghui",
    author_email = "lxh_xwj@126.com",
    packages = find_packages(),
    package_data = {
        '': ['*.py','*.ini','*.json','*.ico','*.dll','*.au3'],
    },
    install_requires = ["requests","selenium","paramiko","xlrd","xlwt","python-docx","python-pptx","pygame","canvas","reportlab","wmi","psutil","comtypes","configobj","configparser","faker","pyinstaller","docx","apscheduler==2.1.2","pycrypto"],
    python_requires = '>=2.7.14',
    zip_safe = False,
)