import hashlib
import json
import pathlib
import pickle
import threading
from typing import Dict, Any

import gridfs
import pydicom
import pymongo
import vtk

import vmi


def input_dicom():
    global series_list
    dcmdir = vmi.askDirectory('DICOM')

    if dcmdir is not None:
        series_list = vmi.sortSeries(dcmdir)
        input_series()


def input_series():
    global series_dict
    series = vmi.askSeries(series_list)
    if series is not None:
        series_dict = series.toKeywordValue()
        input_image(series.read())


def input_image(image: vtk.vtkImageData):
    global series_opacity_range, series_scalar_range
    series_scalar_range = list(image.GetScalarRange())

    series_opacity_range[0] = 0.7 * series_scalar_range[0] + 0.3 * series_scalar_range[1]
    series_opacity_range[1] = series_scalar_range[1]
    series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
    series_opacity_range_box[1].draw_text('max {:.0f}'.format(series_opacity_range[1]))

    series_volume.setData(image)
    series_view.setCamera_FitAll()
    update_series_opcity()
    vmi.appupdate()


def update_series_opcity():
    series_volume.setOpacityScalar({series_opacity_range[0] - 1: 0,
                                    series_opacity_range[0]: 1,
                                    series_opacity_range[1]: 1,
                                    series_opacity_range[1] + 1: 0})
    series_volume.setColor({series_opacity_range[0]: [1, 1, 0.9],
                            series_opacity_range[1]: [1, 1, 0.1]})


def output_nifti():
    vmi.imSave_NIFTI(series_volume.data())


def upload(image: vtk.vtkImageData, kw_value: Dict[str, Any]):
    data_id = ''

    def func():
        # 图像序列化为文件，计算特征码
        vmi.setPickleNIFTI_gz(False)
        image_bytes = pickle.dumps(image)
        image_hash = {'md5': hashlib.md5(image_bytes).hexdigest()}

        # 上传文件，避免重复上传完全一样的文件
        if not file_db.exists(image_hash):
            file_db.put(image_bytes, fileType='.nii')

        # 数据项，引用图像文件特征码
        data_dict = {**kw_value, 'seriesImage': image_hash['md5']}

        # 上传数据项，避免重复上传完全一样的数据项
        nonlocal data_id
        data_one = data_db.find_one(data_dict)
        if data_one is None:
            data_one = data_db.insert_one(data_dict)
            data_id = data_one.inserted_id
        else:
            data_id = data_one['_id']

    t = threading.Thread(target=func)
    t.start()
    vmi.appwait(t)
    return data_id


def output_upload():
    data_id = upload(series_volume.data(), series_dict)

    # 记录上传的id
    if vmi.askYesNo('上传成功 {} 复制到剪贴板？'.format(str(data_id))):
        vmi.app.clipboard().setText(str(data_id))


def output_upload1():
    p = vmi.askDirectory('DICOM根目录')
    if p is not None:
        filenames_list = vmi.sortFilenames(p)

        uploaded = []
        for filenames in filenames_list:
            with pydicom.dcmread(filenames[0]) as ds:
                if len(filenames) < 500:
                    print('层数不符 {} < 500'.format(len(filenames)))
                    continue
                if ds['Modality'].value != 'CT':
                    print('模态不符 {}'.format(ds['Modality'].value))
                    continue

                data_one = data_db.find_one({'PatientID': ds['PatientID'].value,
                                             'StudyInstanceUID': ds['StudyInstanceUID'].value})
                if data_one is not None:
                    if len(filenames) < data_one['slices']:
                        print('已存在 {} < {} {}'.format(len(filenames), data_one['slices'], data_one['_id']))
                        continue
                    elif len(filenames) == data_one['slices']:
                        print('已存在 {} = {} {}'.format(len(filenames), data_one['slices'], data_one['_id']))
                        continue
                    else:
                        data_db.find_one_and_delete(data_one)
                        print('删除 {} > {} {}'.format(len(filenames), data_one['slices'], data_one['_id']))

            series = vmi.SeriesData(filenames)
            image = series.read()
            kw_value = series.toKeywordValue()
            data_id = upload(image, kw_value)
            uploaded.append(str(data_id))
            print('上传成功 {} {}'.format(len(filenames), str(data_id)))

            input_image(image)
            series_view.snapshot_PNG(str(pathlib.Path(p) / str(data_id)))

        uploaded = list(set(uploaded))
        p = vmi.askSaveFile(nameFilter='*.json', title='文件列表')
        if p is not None:
            pathlib.Path(p).write_text(json.dumps(uploaded))


def LeftButtonPressRelease(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        v = vmi.askInt(series_scalar_range[0], series_opacity_range[0], series_opacity_range[1])
        if v is not None:
            series_opacity_range[0] = v
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        v = vmi.askInt(series_opacity_range[0], series_opacity_range[0], series_scalar_range[1])
        if v is not None:
            series_opacity_range[1] = v
        series_opacity_range_box[1].draw_text('min {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def NoButtonWheel(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        series_opacity_range[0] = min(max(series_opacity_range[0] + kwargs['delta'],
                                          series_scalar_range[0]), series_opacity_range[1])
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        series_opacity_range[1] = min(max(series_opacity_range[1] + kwargs['delta'],
                                          series_opacity_range[0]), series_scalar_range[1])
        series_opacity_range_box[1].draw_text('max {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def return_globals():
    return globals()


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
    data_db: pymongo.collection.Collection = client.testDB.data
    file_db = gridfs.GridFS(client.testDB, collection='file')

    main = vmi.Main(return_globals)
    main.setAppName('dicom_to_series')
    main.setAppVersion(vmi.version)
    main.excludeKeys += ['main']

    menu_input = main.menuBar().addMenu('输入')
    menu_input.addAction('DICOM').triggered.connect(input_dicom)
    menu_input.addAction('Series').triggered.connect(input_series)

    menu_output = main.menuBar().addMenu('输出')
    menu_output.addAction('NIFTI').triggered.connect(output_nifti)
    menu_output.addAction('上传').triggered.connect(output_upload)
    t = '自动上传 CT(Modality)同一(PatientID)(StudyInstanceUID)最多(slices)'
    menu_output.addAction(t).triggered.connect(output_upload1)

    series_list, series_dict = [], {}
    series_view = vmi.View()
    series_view.setCamera_Coronal()
    series_volume = vmi.ImageVolume(series_view)

    series_opacity_range, series_scalar_range = [200, 3000], [200, 3000]
    series_opacity_range_box = [vmi.TextBox(series_view, text='min', pickable=True,
                                            size=[0.1, 0.03], pos=[0, 0.03], anchor=[0, 0]),
                                vmi.TextBox(series_view, text='max', pickable=True,
                                            size=[0.1, 0.03], pos=[0.1, 0.03], anchor=[0, 0])]
    for box in series_opacity_range_box:
        box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    main.layout().addWidget(series_view, 0, 0, 1, 1)
    vmi.appexec(main)
    vmi.appexit()
