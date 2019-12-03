#!/usr/bin/python3
from csepy.System.Configurations.SystemConfig import SystemConfig
import json


def GetConfig(name="SystemConfig"):
    return json.loads(json.dumps(SystemConfig))
