#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置类模块，本模块封装了对机器人进行配置的类、方法、结构
"""

import grpc
from harix.rdk.proto.robot_skill_api import robot_config_api_pb2, robot_config_api_pb2_grpc
from harix.rdk.tools import tools


class RobotConfigService(object):

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotConfigService init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = robot_config_api_pb2_grpc.RobotConfigServiceStub(channel)

    def config_robot(self, header, request):
        """
        配置机器人参数

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        config_robot_request = robot_config_api_pb2.ConfigRobotRequest(
            common_req_info=tools.convert_header(header),
            config_names=request["config_names"],
            config_values=request["config_values"]

        )
        res_data = self.stub.ConfigRobot(config_robot_request)
        print(res_data)
        return res_data

    def get_robot_state(self, header, request):
        """
        查询机器人参数

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """

        get_robot_state_request = robot_config_api_pb2.GetRobotStateRequest(
            common_req_info=tools.convert_header(header),
            config_names=request["config_names"]
        )
        res_data = self.stub.GetRobotState(get_robot_state_request)
        print(res_data)
        return res_data

    def config_record_media(self, header, request):
        """
        视频录制设置

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        config_record_media_request = robot_config_api_pb2.ConfigRecordMediaRequest(
            common_req_info=tools.convert_header(header)
        )

        if request["start_param"] is not None:
            config_record_media_request.start_param = request["start_param"]

        if request["stop_param"] is not None:
            config_record_media_request.stop_param = request["stop_param"]

        res_data = self.stub.ConfigRecordMedia(config_record_media_request)
        print(res_data)
        return res_data

    def config_asr(self, header, request):
        """
        控制ARS开/关

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """

        config_asr_request = robot_config_api_pb2.ConfigAsrRequest(
            common_req_info=tools.convert_header(header),
            enable_asr=request["enable_asr"]
        )

        res_data = self.stub.ConfigAsr(config_asr_request)
        print(res_data)
        return res_data

    def config_fr(self, header, request):
        """
        控制识别功能开/关

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        config_fr_request = robot_config_api_pb2.ConfigFrRequest(
            common_req_info=tools.convert_header(header),
            enable_fr=request["enable_fr"]
        )

        res_data = self.stub.ConfigFr(config_fr_request)
        print(res_data)
        return res_data

    def config_face_cam(self, header, request):
        """
        控制机器人本体摄像头识别功能开/关

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """

        config_face_cam_request = robot_config_api_pb2.ConfigFaceCamRequest(
            common_req_info=tools.convert_header(header),
            open_face_cam=request["open_face_cam"],
            camera_index=request["camera_index"]
        )

        res_data = self.stub.ConfigFaceCam(config_face_cam_request)
        print(res_data)
        return res_data

    def config_screen_shot(self, header, request):
        """
        控制短视频与截图录制

        :param request: 配置信息
        :param header: robot基本信息
        :return:
        """
        CameraConfigs = []
        camera_configs = request["camera_configs"]

        for camera_config in camera_configs:
            name = camera_config["name"]
            grabber = camera_config["grabber"]
            CameraConfig = robot_config_api_pb2.CameraConfig(
                name=name,
                grabber=grabber
            )
            screen_shot = camera_config["screen_shot"]
            if screen_shot is not None:
                CameraConfig.screen_shot = robot_config_api_pb2.ScreenShot(
                    filename=screen_shot["filename"]
                )

            short_video = camera_config["short_video"]
            if short_video is not None:
                CameraConfig.short_video = robot_config_api_pb2.ShortVideo(
                    duration=short_video["duration"],
                    filename=short_video["filename"]
                )

            cache = camera_config["cache"]
            if cache is not None:
                CameraConfig.cache = robot_config_api_pb2.Cache(
                    duration=cache["duration"],
                    enable=cache["enable"]
                )

            CameraConfigs.append(CameraConfig)

        config_screen_shot_request = robot_config_api_pb2.ConfigScreenShotRequest(
            common_req_info=tools.convert_header(header),
            camera_configs=CameraConfigs
        )

        res_data = self.stub.ConfigScreenShot(config_screen_shot_request)
        print(res_data)
        return res_data

