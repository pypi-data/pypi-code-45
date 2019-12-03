#coding=utf-8
import requests
import json
import random
from urllib3 import encode_multipart_formdata

class XesFileUpload:

	#单个file上传
	def upload(self, filepath, ext):

			#1、调用upload服务获取上传信息
			xes_response = self.__getUploadParams(ext)

			#2、使用upload服务返回的信息，调用阿里云直传 注意 python3 open(filepath,'rb').read()
			ali = xes_response[0]

			response = requests.request(method="PUT", url=ali['host'], data=open(filepath,'rb').read(), headers=ali['header'])

			#返回可以访问的url
			return ali['asurl']

    #从编程接口获取阿里云直传的参数
	def __getUploadParams(self, ext):
		#测试环境需要绑host: 10.97.15.72 code.xueersi.com
		url = 'https://code.xueersi.com/api/python/get_upload_service_params?ext=' + ext
		response = requests.get(url)
		data = json.loads(response.text)['data']

		return data

##调用示例
##测试环境需要绑host: 10.97.15.72 code.xueersi.com
#uploader = XesFileUpload()
#imgurl = uploader.upload(file("/Users/sdzhu/Desktop/laba.png"), 'png')
#print imgurl

		