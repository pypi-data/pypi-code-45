'''test for git'''
import vmi
import nibabel as nib
import numpy as np
import pydicom
import vtk
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from numba import jit
import pandas as pd
import os
import pymongo
import gridfs
import pickle
import hashlib
import threading

from typing import List, Optional

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import vmi


dic_list = ['髂前上棘',
            '耻骨结节',
            '髂脊',
            '坐骨结节',
            '髂后上棘',
            '髂前下棘',
            '股骨中心']
color_map = {
    '髂前上棘': [128, 0, 0],
    '耻骨结节': [255, 204, 0],
    '髂脊': [128, 128, 0],
    '坐骨结节': [0, 255, 128],
    '髂后上棘': [0, 128, 128],
    '髂前下棘': [0, 0, 128],
    '股骨中心': [75, 0, 128]
}

mark_points = {
    '髂前上棘': [],
    '耻骨结节': [],
    '髂脊': [],
    '坐骨结节': [],
    '髂后上棘': [],
    '髂前下棘': [],
    '股骨中心': []}
radius = 2.5
center_props = []
center_pts = []
###
from PySide2.QtWidgets import QInputDialog



def load_by_md5():
    print('zzzzzzz')
    global case_md5,case_info,case_image_data
    text = QInputDialog.getText(None, '请输入案例MD5', 'MD5')
    if text[1]:
        case_md5 = text[0]

    search_dict = {'md5': case_md5}
    if not file_db.exists(search_dict):
        return 'case_md5 not floud'
    else:
        case_info = data_db.find_one({'seriesImage': case_md5})
        case_image_data =file_db.find_one(search_dict)


def output_upload():
    data_id =''
    mark_dict = {
        '髂前上棘': [center_pts[0], center_pts[1]],
        '耻骨结节': [center_pts[2], center_pts[3]],
        '髂脊': [center_pts[4], center_pts[5]],
        '坐骨结节': [center_pts[6], center_pts[7]],
        '髂后上棘': [center_pts[8], center_pts[9]],
        '髂前下棘': [center_pts[10], center_pts[11]],
        '股骨中心': [center_pts[12], center_pts[13]]}

    mark_bytes = pickle.dumps(mark_dict)
    mark_hash = {'md5': hashlib.md5(mark_bytes).hexdigest()}

    # 上传文件，避免重复上传完全一样的文件
    if not file_db.exists(mark_hash):
        file_db.put(mark_bytes, fileType='.json')

    # 替换旧数据,增加marked数据的md5
    unmarked_data_dict = data_db.find_one({'seriesImage':case_md5})
    marked_data_dict = {**unmarked_data_dict, 'markData': mark_hash['md5']}
    data_db.find_one_and_replace(unmarked_data_dict,marked_data_dict)

    data_id = mark_hash['md5']


    # 记录上传的id
    if vmi.askYesNo('上传成功 {} 复制到剪贴板？'.format(str(data_id))):
        vmi.app.clipboard().setText(str(data_id))




def render_pts_only(pts):
    center_prop = vmi.PolyActor(voi_view, color=[0.8, 0.8, 1], pickable=True)
    center_prop.alwaysOnTop()
    center_prop.mouse['LeftButton']['PressMove'] = LeftButtonPressMove
    center_prop.mouse['LeftButton']['PressRelease'] = LeftButtonPressRelease
    center_prop.setData(vmi.pdSphere(radius, pts[0]))


def render_pts_line(pts):
    center_prop_1 = vmi.PolyActor(voi_view, color=[0.8, 0.8, 1], pickable=True)
    center_prop_2 = vmi.PolyActor(voi_view, color=[0.8, 0.8, 1], pickable=True)
    center_prop_1.alwaysOnTop()
    center_prop_1.mouse['LeftButton']['PressMove'] = LeftButtonPressMove
    center_prop_1.mouse['LeftButton']['PressRelease'] = LeftButtonPressRelease
    center_prop_1.setData(vmi.pdSphere(radius, pts[0]))

    center_prop_2.alwaysOnTop()
    center_prop_2.mouse['LeftButton']['PressMove'] = LeftButtonPressMove
    center_prop_2.mouse['LeftButton']['PressRelease'] = LeftButtonPressRelease
    center_prop_2.setData(vmi.pdSphere(radius, pts[1]))



def render_all_pts(pts):
    ith = -1
    global center_props
    center_prop = vmi.PolyActor(voi_view, color=[0, 0, 0], pickable=True)
    center_props.append(center_prop)
    center_props = center_props[:14]
    for i in range(len(center_props)):
        if i % 2 == 0:
            ith += 1
            rbg = np.array(color_map[dic_list[ith]]) / 255
        center_props[i].setColor(rbg)
        center_props[i].setData(vmi.pdSphere(radius, pts[i]))

def LeftButtonPressRelease(**kwargs):
    global center_pts
    if kwargs['picked'] in [voi_view]:
        if kwargs['double'] is True:
            center_pts.append(voi_view.pickPt_Cell())
            render_all_pts(center_pts)
    elif kwargs['picked'] is upload_box:
        output_upload()
        print(111)
    elif kwargs['picked'] is download_box:
        load_by_md5()
        voi_image = pickle.loads(case_image_data.read())
        voi_volum.setData(voi_image)
        voi_volum.setOpacity_Threshold(threshold)
        voi_view.setCamera_FitAll()
        voi_view.setCamera_Coronal()

def LeftButtonPressMove(**kwargs):
    if kwargs['picked'] in center_props:
        i = center_props.index(kwargs['picked'])

        center_pts[i] += voi_view.pickVt_FocalPlane()
        center_props[i].setData(vmi.pdSphere(radius, center_pts[i]))
    else:
        voi_view.mouseRotateFocal(**kwargs)


class Main(QScrollArea):
    def __init__(self):
        QScrollArea.__init__(self)
        brush = QBrush(QColor(255, 255, 255, 255))
        palette = QPalette()
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.setPalette(palette)
        self.setWidgetResizable(True)

    def closeEvent(self, ev: QCloseEvent):
        ev.accept() if vmi.askYesNo('退出程序？') else ev.ignore()


if __name__ == '__main__':

    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
    data_db: pymongo.collection.Collection = client.testDB.data
    file_db = gridfs.GridFS(client.testDB, collection='file')

    threshold = 200
    voi_view = vmi.View()

    voi_volum = vmi.ImageVolume(voi_view, pickable=True)

    voi_view.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]
    voi_view.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]



    pelvis_qiaqianshangji_box = vmi.TextBox(voi_view, pickable=True, text='髂前上棘', size=[0.1, 0.04], pos=[0.02, 0],
                                            anchor=[0, 0])
    pelvis_qiaqianshangji_color = np.array(color_map['髂前上棘']) / 255
    pelvis_qiaqianshangji_color_box = vmi.TextBox(voi_view, back_color=QColor.fromRgbF(pelvis_qiaqianshangji_color[0],
                                                                                       pelvis_qiaqianshangji_color[1],
                                                                                       pelvis_qiaqianshangji_color[2]),
                                                  size=[0.02, 0.04], pos=[0, 0], anchor=[0, 0])

    pelvis_chigujiejie_box = vmi.TextBox(voi_view, pickable=True, text='耻骨结节', size=[0.1, 0.04], pos=[0.14, 0],
                                         anchor=[0, 0])
    pelvis_chigujiejie_color = np.array(color_map['耻骨结节']) / 255
    pelvis_chigujiejie_color_box = vmi.TextBox(voi_view, back_color=QColor.fromRgbF(pelvis_chigujiejie_color[0],
                                                                                    pelvis_chigujiejie_color[1],
                                                                                    pelvis_chigujiejie_color[2]),
                                               size=[0.02, 0.04], pos=[0.12, 0], anchor=[0, 0])

    pelvis_qiaji_box = vmi.TextBox(voi_view, pickable=True, text='髂脊', size=[0.1, 0.04], pos=[0.02, 0.06],
                                   anchor=[0, 0])
    pelvis_qiaji_color = np.array(color_map['髂脊']) / 255
    pelvis_qiaji_color_box = vmi.TextBox(voi_view,
                                         back_color=QColor.fromRgbF(pelvis_qiaji_color[0], pelvis_qiaji_color[1],
                                                                    pelvis_qiaji_color[2]),
                                         size=[0.02, 0.04], pos=[0, 0.06], anchor=[0, 0])
    pelvis_zuogujiejie_box = vmi.TextBox(voi_view, pickable=True, text='坐骨结节', size=[0.1, 0.04], pos=[0.14, 0.06],
                                         anchor=[0, 0])
    pelvis_zuogujiejie_color = np.array(color_map['坐骨结节']) / 255
    pelvis_zuogujiejie_color_box = vmi.TextBox(voi_view,
                                               back_color=QColor.fromRgbF(pelvis_zuogujiejie_color[0],
                                                                          pelvis_zuogujiejie_color[1],
                                                                          pelvis_zuogujiejie_color[2]),
                                               size=[0.02, 0.04], pos=[0.12, 0.06], anchor=[0, 0])

    pelvis_qiahoushangji_box = vmi.TextBox(voi_view, pickable=True, text='髂后上棘', size=[0.1, 0.04], pos=[0.02, 0.12],
                                           anchor=[0, 0])
    pelvis_qiahoushangji_color = np.array(color_map['髂后上棘']) / 255

    pelvis_qiahoushangji_color_box = vmi.TextBox(voi_view,
                                                 back_color=QColor.fromRgbF(pelvis_qiahoushangji_color[0],
                                                                            pelvis_qiahoushangji_color[1],
                                                                            pelvis_qiahoushangji_color[2]),
                                                 size=[0.02, 0.04], pos=[0, 0.12], anchor=[0, 0])
    pelvis_qiaqianxiaji_box = vmi.TextBox(voi_view, pickable=True, text='髂前下棘', size=[0.1, 0.04], pos=[0.14, 0.12],
                                          anchor=[0, 0])

    pelvis_qiaqianxiaji_color = np.array(color_map['髂前下棘']) / 255

    pelvis_qiaqianxiaji_color_box = vmi.TextBox(voi_view,
                                                back_color=QColor.fromRgbF(pelvis_qiaqianxiaji_color[0],
                                                                           pelvis_qiaqianxiaji_color[1],
                                                                           pelvis_qiaqianxiaji_color[2]),
                                                size=[0.02, 0.04], pos=[0.12, 0.12], anchor=[0, 0])

    pelvis_guguzhongxin_box = vmi.TextBox(voi_view, pickable=True, text='股骨中心', size=[0.1, 0.04], pos=[0.02, 0.18],
                                          anchor=[0, 0])

    pelvis_guguzhongxin_color = np.array(color_map['股骨中心']) / 255

    pelvis_guguzhongxin_color_box = vmi.TextBox(voi_view,
                                                back_color=QColor.fromRgbF(pelvis_guguzhongxin_color[0],
                                                                           pelvis_guguzhongxin_color[1],
                                                                           pelvis_guguzhongxin_color[2]),
                                                size=[0.02, 0.04], pos=[0, 0.18], anchor=[0, 0])
    pelvis_guguzhongxin_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    upload_box = vmi.TextBox(voi_view, pickable=True, text='上传标记数据', size=[0.12, 0.04], pos=[0.12, 0.24],
                             anchor=[0, 0])
    upload_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    download_box = vmi.TextBox(voi_view, pickable=True, text='下载原始数据', size=[0.12, 0.04], pos=[0, 0.24],
                                            anchor=[0, 0])
    download_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    widget = QWidget()
    layout = QGridLayout(widget)
    layout.addWidget(voi_view)

    main = Main()
    main.setWidget(widget)

    vmi.appexec(main)  # 执行主窗口程序
    vmi.appexit()  # 清理并退出程序
