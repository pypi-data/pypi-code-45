"""
spider标准库
"""
import time
import os
import sqlite3 as sql
import platform
if platform.system() == "Linux":
    from ddcmaker.linux.armv7l import get_equipment_type as ge
    from ddcmaker.spider.hwax import HWAX
else:
    from ddcmaker.confusion.err_system import get_equipment_type
    # ge = get_equipment_type()
from ddcmaker.spider import SerialServoCmd as ssc
from ddcmaker.pubulic import config_serial_servo
import threading
runningAction = False
stopRunning = False
online_action_num = None
online_action_times = -1
update_ok = False