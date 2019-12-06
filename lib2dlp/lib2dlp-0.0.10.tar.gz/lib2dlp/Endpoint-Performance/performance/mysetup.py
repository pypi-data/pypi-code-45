# mysetup.py
# from distutils.core import setup
# import py2exe

# setup(console=["helloworld.py"])

# -*- encoding:utf-8 -*-

from distutils.core import setup
import py2exe


INCLUDES = []

options = {
    "py2exe" :
        {
            #"compressed" : 1,
            "optimize" : 2,
            #"bundle_files" : 3,
            "includes" : INCLUDES,
            "dll_excludes" : ["MSVCR100.dll"]
        }
}


setup(
    options=options,
    description = "this is a py2exe test",
    zipfile=None,
    console = [{"script":'discoveryPDF.py'}])