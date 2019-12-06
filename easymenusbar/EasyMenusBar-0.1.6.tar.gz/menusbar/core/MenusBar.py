#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QWidget, QFileSystemModel, QTreeView, QAction, QMenu, QVBoxLayout, QAbstractItemView
from PySide2 import QtCore
from PySide2.QtCore import QMargins, QFileInfo
from PySide2.QtGui import QMouseEvent
from .FileUtils import createFile, createDir, deleteDir, deleteFile, getProjectPath
import uuid
from .Dialog import Dialog as MKDialog
import json
import os
from .FileUtils import createFile


class MemusBar(QWidget):
    handlerAfterSignal = QtCore.Signal(int, str)
    handlerBeforeSignal = QtCore.Signal(int, str)
    HANLDER_CREATE_DIR = 0
    HANLDER_DELETE_DIR = 1
    HANLDER_CREATE_FILE = 2
    HANLDER_DELETE_FILE = 3

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lastSettingFile = "lastSettingFile"
        self.init()
        self._initUI()
        self.defaultForCreateMD = ["metaData-id:%s" % uuid.uuid1(), "metaData-title:"]
        self.initEvent()

    def init(self):
        self.workDir = ""
        self.defualtSuffix = 'md'
        self.defualtSuffixList = None

    def createDir(self, value):
        createDir(self.workDir, value)

    def createFile(self, value, default: str = ""):
        createFile(self.workDir, value, self.defaultForCreateMD)

    def initEvent(self):
        pass

    def getSettingFile(self):
        if not os.path.exists(os.path.join(getProjectPath(), "lastSettingFile.json")):
            with open(os.path.join(getProjectPath(), "lastSettingFile.json"), mode='w')  as jsonFile:
                pass
        with open(os.path.join(getProjectPath(), "lastSettingFile.json"), mode='r') as jsonFile:
            try:
                data = json.load(jsonFile)
                return data
            except Exception as e:
                print(e)
                return {}

    def saveSettingFile(self, setting):
        with open(os.path.join(getProjectPath(), "lastSettingFile.json"), mode='w') as jsonFile:
            json.dump(setting, jsonFile)

    def getLastWorkDirRecord(self):
        setting: dict = self.getSettingFile()
        value = setting.get("lastWorkDirRecord")
        if value:
            return value
        else:
            return "/"

    def saveWorkDirRecord(self, value):
        setting = self.getSettingFile()
        setting["lastWorkDirRecord"] = value
        self.saveSettingFile(setting)

    def updateWorkDir(self, value: str = ""):
        if not value or value == "":
            # 去最后一次的目录信息
            self.workDir = self.getLastWorkDirRecord()
        else:
            self.workDir = value
            self.saveWorkDirRecord(value)
        self.treeModel.setRootPath(self.workDir)
        self.treeView.setRootIndex(self.treeModel.index(self.workDir))
        filtersList = list()
        if self.defualtSuffixList:
            for s in self.defualtSuffixList:
                filtersList.append("*.%s" % s)

        else:
            filtersList.append("*.%s" % self.defualtSuffix)

        self.treeModel.setNameFilters(filtersList)

    def _initUI(self):
        self.mainLayout = QVBoxLayout(self)

        self.mainLayout.setContentsMargins(QMargins(0, 0, 0, 0))

        self.treeModel = QFileSystemModel(self)
        self.treeModel.setReadOnly(False)
        self.treeView = QTreeView(self)
        self.treeView.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeView.setDragEnabled(True)
        self.treeView.setAcceptDrops(True)
        self.treeView.setDropIndicatorShown(True)
        self.setMinimumHeight(100)
        self.treeView.setModel(self.treeModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.showContextMenu)
        self.treeView.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        self.treeView.setColumnHidden(1, True)
        self.treeView.setColumnHidden(2, True)
        self.treeView.setColumnHidden(3, True)
        self.mainLayout.addWidget(self.treeView, 1)
        self.setLayout(self.mainLayout)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            # 是否按下左键
            index = self.treeView.indexAt(event.pos())
            if index.isValid():
                fileInfo = self.treeModel.fileInfo(index)
                if fileInfo.isFile():
                    self.openFileEvent(fileInfo)
        else:
            event.accept()

    def showContextMenu(self, pos):
        index = self.treeView.indexAt(pos)
        if index.isValid():
            menu = QMenu(self)
            action = QAction(menu)
            action.setObjectName("create_dir")
            action.setProperty("pos", pos)
            action.setText("创建目录")
            action.triggered.connect(self.actionHandler)
            menu.addAction(action)

            action = QAction(menu)
            action.setObjectName("delete_dir")
            action.setProperty("pos", pos)
            action.setText("删除目录")
            action.triggered.connect(self.actionHandler)
            menu.addAction(action)

            action = QAction(menu)
            action.setObjectName("create_file")
            action.setProperty("pos", pos)
            action.setText("创建文件")
            action.triggered.connect(self.actionHandler)
            menu.addAction(action)

            action = QAction(menu)
            action.setObjectName("delete_file")
            action.setProperty("pos", pos)
            action.setText("删除文件")
            menu.addAction(action)
            action.triggered.connect(self.actionHandler)
            menu.exec_(self.treeView.mapToGlobal(pos))

    def handlerBeforeEvent(self, type: int, filePath: str) -> bool:
        return True

    def _handlerBeforeEvent(self, type: int, filePath: str) -> bool:
        self.handlerBeforeSignal.emit(type, filePath)
        return self.handlerBeforeEvent(type, filePath)

    def _handlerAfterEvent(self, type: int, filePath: str):
        self.handlerAfterSignal.emit(type, filePath)
        self.handlerAfterEvent(type, filePath)

    def handlerAfterEvent(self, type: int, filePath: str):
        pass

    def actionHandler(self):
        type = self.sender().objectName()
        fileInfo = self.treeModel.fileInfo(self.treeView.currentIndex())
        # print(fileInfo.fileName())
        # print(fileInfo.filePath())
        # print(fileInfo.path())
        # print(fileInfo.isRoot())
        file = fileInfo.filePath()
        if type == "create_dir":
            text = MKDialog().inputDirNameDialog()
            if text:
                if self._handlerBeforeEvent(self.HANLDER_CREATE_DIR, os.path.join(self.getDir(fileInfo), text)):
                    createDir(self.getDir(fileInfo), text)
                    self._handlerAfterEvent(self.HANLDER_CREATE_DIR, os.path.join(self.getDir(fileInfo), text))

        elif type == "delete_dir":
            if self._handlerBeforeEvent(self.HANLDER_DELETE_DIR, fileInfo.filePath()):
                deleteDir(fileInfo.filePath())
                self._handlerAfterEvent(self.HANLDER_DELETE_DIR, fileInfo.filePath())

        elif type == "create_file":
            text = MKDialog().inputFileNameDialog()
            temp = str(text).split(".")
            if len(temp) < 2:
                text = text + "." + self.defualtSuffix
            else:
                fileSuffix = temp[len(temp) - 1]
                if self.defualtSuffixList:
                    if fileSuffix not in self.defualtSuffixList:
                        text = text + "." + self.defualtSuffix
                elif self.defualtSuffix and self.defualtSuffix != fileSuffix:
                    text = text + "." + self.defualtSuffix
            if text:
                if self._handlerBeforeEvent(self.HANLDER_CREATE_FILE, os.path.join(self.getDir(fileInfo), text)):
                    createFile(self.getDir(fileInfo), text)
                    self._handlerAfterEvent(self.HANLDER_CREATE_FILE, os.path.join(self.getDir(fileInfo), text))

        elif type == "delete_file":
            if self._handlerBeforeEvent(self.HANLDER_DELETE_FILE, file):
                deleteFile(file)
                self._handlerAfterEvent(self.HANLDER_DELETE_FILE, file)

    def getDir(self, fileInfo: QFileInfo):
        if fileInfo.isFile():
            return fileInfo.path()
        else:
            return fileInfo.filePath()

    def openFileEvent(self, fileInfo: QFileInfo):
        pass

    def setSupportFileSuffix(self, suffix: list, defualtSuffix: str):
        self.defualtSuffixList = suffix
        self.defualtSuffix = defualtSuffix
