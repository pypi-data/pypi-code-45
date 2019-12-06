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
    series_volume.setData(image)
    series_view.setCamera_FitAll()
    series_view.updateAtOnce()
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
            file_id = file_db.put(image_bytes, fileType='.nii', scalarType=image.GetScalarTypeAsString())
            # 检查上传结果是否与本地一致
            if file_db.find_one({'_id': file_id}).md5 != image_hash['md5']:
                file_db.delete(file_id)
                return print('远端MD5校验失败 {}'.format(repr(kw_value)))

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


def output_upload_pelvisCT():
    p = vmi.askDirectory('DICOM根目录')
    if p is not None:
        save_filenames_list = pathlib.Path(p) / 'filenames_list.json'
        if save_filenames_list.exists():
            filenames_list = json.loads(save_filenames_list.read_bytes())
        else:
            filenames_list = vmi.sortFilenames(p)
            pathlib.Path(str(save_filenames_list)).write_text(json.dumps(filenames_list))

        uploaded_list = []
        n = len(filenames_list)
        for i in range(n):
            filenames = filenames_list[i]
            with pydicom.dcmread(filenames[0]) as ds:
                if 'Modality' not in ds or 'PatientID' not in ds or 'StudyInstanceUID' not in ds or 'SeriesInstanceUID' not in ds:
                    print('{}/{} 标签不符'.format(i, n))
                if ds['Modality'].value != 'CT':
                    print('{}/{} 模态不符 Modality={}'.format(i, n, ds['Modality'].value))
                    continue
                if 'StudyDescription' in ds:
                    if 'Spine' in ds['StudyDescription'].value:
                        print('{}/{} 检查不符 StudyDescription={}'.format(i, n, ds['StudyDescription'].value))
                        continue

                one = data_db.find_one({'PatientID': ds['PatientID'].value,
                                        'StudyInstanceUID': ds['StudyInstanceUID'].value})

                if one is not None:
                    if len(filenames) < one['slices']:
                        print('{}/{} 本地跳过 slices={} < {}'.format(i, n, len(filenames), one['slices']))
                        continue
                    elif len(filenames) >= one['slices']:
                        data_db.find_one_and_delete(one)
                        if one['SeriesInstanceUID'] in uploaded_list:
                            uploaded_list.remove(one['SeriesInstanceUID'])
                        save_snapshot = pathlib.Path(p) / '{}.png'.format(one['SeriesInstanceUID'])
                        save_snapshot.unlink() if save_snapshot.exists() else 0
                        print('{}/{} 远端删除 slices={} {} {}'.format(i, n, len(filenames),
                                                                  '==' if len(filenames) == one['slices'] else '>',
                                                                  one['slices']))

                series = vmi.SeriesData(filenames)
                image = series.read()

                if image.GetScalarTypeAsString() != 'short':
                    print('{}/{} 值型不符 scalarType={}'.format(i, n, image.GetScalarTypeAsString()))
                    continue

                upload(image, series.toKeywordValue())
                print('{}/{} 上传成功 slices={} {}'.format(i, n, len(filenames), ds['SeriesInstanceUID'].value))
                uploaded_list.append(ds['SeriesInstanceUID'].value)

                input_image(image)
                save_snapshot = pathlib.Path(p) / ds['SeriesInstanceUID'].value
                series_view.snapshot_PNG(str(save_snapshot))

        save_uploaded_list = pathlib.Path(p) / 'uploaded_list.json'
        save_uploaded_list.write_text(json.dumps(uploaded_list))
        print('自动上传完成 总数={}'.format(len(uploaded_list)))


def LeftButtonPressRelease(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        v = vmi.askInt(-10000, series_opacity_range[0], series_opacity_range[1])
        if v is not None:
            series_opacity_range[0] = v
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        v = vmi.askInt(series_opacity_range[0], series_opacity_range[0], 10000)
        if v is not None:
            series_opacity_range[1] = v
        series_opacity_range_box[1].draw_text('min {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def NoButtonWheel(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        series_opacity_range[0] = min(max(series_opacity_range[0] + kwargs['delta'],
                                          -10000), series_opacity_range[1])
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        series_opacity_range[1] = min(max(series_opacity_range[1] + kwargs['delta'],
                                          series_opacity_range[0]), 10000)
        series_opacity_range_box[1].draw_text('max {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def return_globals():
    return globals()


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
    data_db: pymongo.collection.Collection = client.testDB.normalPelvisCT
    # data_db.delete_many({})
    file_db = gridfs.GridFS(client.testDB, collection='normalPelvisCTFS')

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
    menu_output.addAction('自动上传 骨盆CT').triggered.connect(output_upload_pelvisCT)

    series_list, series_dict = [], {}
    series_view = vmi.View()
    series_view.setCamera_Coronal()
    series_volume = vmi.ImageVolume(series_view)

    series_opacity_range = [200, 3000]
    update_series_opcity()

    series_opacity_range_box = [vmi.TextBox(series_view, text='min {:.0f}'.format(series_opacity_range[0]),
                                            size=[0.1, 0.03], pos=[0, 0.03], anchor=[0, 0], pickable=True),
                                vmi.TextBox(series_view, text='max {:.0f}'.format(series_opacity_range[1]),
                                            size=[0.1, 0.03], pos=[0.1, 0.03], anchor=[0, 0], pickable=True)]
    for box in series_opacity_range_box:
        box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    main.layout().addWidget(series_view, 0, 0, 1, 1)
    vmi.appexec(main)
    vmi.appexit()
