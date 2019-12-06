import os
from setuptools import setup, find_packages            #这个包没有的可以pip一下

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()

setup(
    name = "DobotRPC",      #这里是pip项目发布的名称
    version = "3.0.0",  #版本号，数值大的会优先被pip
    keywords = ["websocket", "JSON-RPC", "asyncio", "Dobot", "Dobotlink"],
    description = "Dobotlink communication module",
    long_description=README,
    long_description_content_type="text/markdown",
    license = "Apache Licence",

    author = "JoMar Wu",
    author_email = "songlijun@dobot.cc",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["websockets", "asyncio", "colorlog", "demjson"]          #这个项目需要的第三方库
)