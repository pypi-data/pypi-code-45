#!/usr/bin/python3
from csepy.System.Models.OperatingSystemModel.OsModel import OsModel
from csepy.System.OperatingSystem.OperatingSystemIdentifier import GetOperatingSystemName, \
    GetOperatingSystemRelease, GetOperatingSystemVersion


def GetOsModel():
    operatingSystemName = GetOperatingSystemName()
    operatingSystemRelease = GetOperatingSystemRelease()
    operatingSystemVersion = GetOperatingSystemVersion()

    osModel = OsModel(operatingSystemName, operatingSystemRelease, operatingSystemVersion)

    return osModel
