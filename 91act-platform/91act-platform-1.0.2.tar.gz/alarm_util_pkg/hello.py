from core import SimpleCronControl
import os,sys
# SimpleCronControl("lilei").list_cron()
SimpleCronControl("lilei").cron_control("http://127.0.0.1:5000/test","My Token")
# print os.path.abspath(__file__)
