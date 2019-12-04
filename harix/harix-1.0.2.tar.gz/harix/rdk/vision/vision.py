#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
语音识别接口
"""

import grpc
from harix.rdk.proto.vision import vision_pb2, vision_pb2_grpc
from harix.rdk.tools import tools


def generate_stream_param(image_request_list):
    for image_request in image_request_list:
        yield image_request


class VisionService(object):

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("VisionService init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url,
                                        options=[('grpc.default_authority', authority)])
        self.stub = vision_pb2_grpc.VisionStub(channel)

    def vision_recognize(self, header, request):
        """
        图像识别

        :param request: 参数
        :param header: robot基本信息
        :return:RecognizeType
        """
        common_req_info = tools.convert_header(header)
        image_request = vision_pb2.ImageRequest(
            common_req_info=common_req_info,
            body=request["body"],
            extra=request["extra"]
        )
        res_data = self.stub.Recognize(image_request)
        return res_data

    def vision_stream_recognize(self, header, images):
        """
        图像识别

        :param images: 图片信息
        :param header: robot基本信息
        :return:
        """
        common_req_info = tools.convert_header(header)
        image_request_list = []
        for image in images:
            image_request = vision_pb2.ImageRequest(
                common_req_info=common_req_info,
                body=image["body"],
                extra=image["extra"]
            )
            image_request_list.append(image_request)

        responses = self.stub.StreamingRecognize(generate_stream_param(image_request_list))
        return responses



