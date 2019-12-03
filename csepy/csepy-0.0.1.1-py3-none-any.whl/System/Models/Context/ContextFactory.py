#!/usr/bin/python3
from csepy.System.CommandQueue.CommandQueueFactory import GetCommandQueue
from csepy.System.Configurations.ConfigArchivist import GetConfig
from csepy.System.Logger.LoggerFactory import GetLogger
from csepy.System.Models.Context.Context import Context
from csepy.System.Models.OperatingSystemModel.OsModelFactory import GetOsModel


def GetContext():
    commandQueue = GetCommandQueue()
    osModel = GetOsModel()
    config = GetConfig("SystemConfig")
    logger = GetLogger(config, osModel.OperatingSystemName)
    context = Context(commandQueue, osModel, logger, config)
    commandQueue.SetContext(context)
    return context
