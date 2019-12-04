import json
from urllib3 import encode_multipart_formdata

from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.common.abstract_client import AbstractClient
from panclient.common.cookie import cookie
from panclient.importdata import models


class ImportClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = '192.168.10.113:8186'
    _requestPath = None
    _default_content_type = 'application/x-www-form-urlencoded'
    _default_token = ''
    _panorama_source_guid = None
    _panorama_workspace_id = None

    # 1. 获取所有数据库的配置信息
    def get_database_config(self):
        try:
            self._requestPath = "/api2/load/data/database/config/get"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body,_ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)


    # 2. 保存或更新数据库配置信息
    def save_database_config(self, request):
        try:
            self._requestPath = "/api2/load/data/database/config/save"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # 3. 删除数据库配置信息
    def delete_database_config(self, request):
        try:
            self._requestPath = "/api2/load/data/database/config/delete/"
            self.httpProfile.reqMethod = "DELETE"
            self.httpProfile.keepAlive = 30
            self._requestPath = self._requestPath + request.id
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    #4. 测试连接数据库
    def ping_database_test(self, request):
        try:
            self._requestPath = "/api2/load/data/database/config/test"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    #5. 获取外部数据库全部的表和表的字段
    def get_out_database_info(self, request):
        try:
            self._requestPath = "/api2/load/data/database/metadata/one"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            self._requestPath = self._requestPath + "?id="+ request.id
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                return response
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)



    #6. 获取所有数据库和数据表信息
    def get_all_database(self):
        try:
            self._requestPath = "/api2/load/data/database/metadata/all"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body,_ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    #7. 创建Schema,生成默认的映射.
    def generate_schema_map(self,request):
        try:
            self._requestPath = "/api2/load/data/database/create/schema"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = request._serialize()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # 7. 根据连接ID获取全部映射
    def get_schema_map(self, request):
        try:
            self._requestPath = "/api2/load/data/database/mapping/all"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = request._serialize()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    #8. 修改映射
    def mod_schema_map(self, request):
        try:
            self._requestPath = "/api2/load/data/database/mapping/modify"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.rawStr
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # 9. 导出schema文件
    def export_schema_map(self, request):
        try:
            self._requestPath = "/api2/load/data/database/mapping/output"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = request._serialize()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)


    # 10.导入数据库数据
    def import_database_data(self,request):
        try:
            self._requestPath = "/api2/load/data/start"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.rawStr
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, _ = self.call(params)
            print("body:", body)
            response = json.loads(body)
            if response:
                return body
            else:
                code = "False"
                message = response["message"]
                raise PanSDKException(code, message)
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)


    # rdf 导入
    def get_rdf_mapping(self, request):
        try:
            self._requestPath = "/panorama/v4/import/rdf/get/mapping"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = request._serialize()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    def get_rdf_files(self):
        try:
            self._requestPath = "/panorama/v4/import/rdf/files"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v4/import/rdf/predicate
    def get_rdf_file_predicate(self, request):
        try:
            self._requestPath = "/panorama/v4/import/rdf/predicate"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = request._serialize()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v4/import/rdf/start
    def import_rdf_start(self, request):
        try:
            self._requestPath = "/panorama/v4/import/rdf/start"
            self.httpProfile.reqMethod = "POST"
            self._default_content_type = "application/json"
            self.httpProfile.keepAlive = 30
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Source-Guid": self._panorama_source_guid,
                      "Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # jms 导入
    # jms /panorama/v3/jms/all
    def get_all_jms(self):
        try:
            self._requestPath = "/panorama/v3/jms/all"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v3/jms/drivers
    def get_jms_drivers(self):
        try:
            self._requestPath = "/panorama/v3/jms/drivers"
            self.httpProfile.reqMethod = "GET"
            self.httpProfile.keepAlive = 30
            params = ""
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v3/jms/connectionTest
    def jms_connect_test(self, request):
        try:
            self._requestPath = "/panorama/v3/jms/connectionTest"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Source-Guid": self._panorama_source_guid,
                      "Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v3/jms/connectionTest
    def jms_connect_test(self, request):
        try:
            self._requestPath = "/panorama/v3/jms/connectionTest"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Source-Guid": self._panorama_source_guid,
                      "Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v3/jms/consumerTest
    def jms_consumer_test(self, request):
        try:
            self._requestPath = "/panorama/v3/jms/consumerTest"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Source-Guid": self._panorama_source_guid,
                      "Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /panorama/v3/jms
    def save_jms(self, request):
        try:
            self._requestPath = "/panorama/v3/jms"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'application/json'
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            header = {"Panorama-Source-Guid": self._panorama_source_guid,
                      "Panorama-Workspace-Id": self._panorama_workspace_id}
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # 上传csv
    def upload_csv_file(self, request):
        try:
            self._requestPath = "/panorama/v4/upload"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 300
            self.httpProfile.reqTimeout = 3000
            self._default_content_type = 'multipart/form-data'
            params = {"file": (request.filename, open(request.filepath, 'rb').read())}
            # params['file'] = (request.filename, open(request.filepath, 'rb').read())
            # print("params:", params)
            encode_data = encode_multipart_formdata(params)
            params = encode_data[0]
            # print(header)
            header = {"Content-Type": encode_data[1]}
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    def upload_multi_csv_file(self, request):
        try:
            self._requestPath = "/panorama/v4/multiUpload"
            self.httpProfile.reqMethod = "POST"
            self.httpProfile.keepAlive = 30
            self._default_content_type = 'multipart/form-data'
            for i in range(len(request.filename)):
                params = {request.filename[i]: (request.filename[i], open(request.filepath[i], 'rb').read())}
            # params['file'] = (request.filename, open(request.filepath, 'rb').read())
            # print("params:", params)
            encode_data = encode_multipart_formdata(params)
            params = encode_data[0]
            # print(header)
            header = {"Content-Type": encode_data[1]}
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, header = self.call(params, header)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)

    # /v4/import/csv/python/start
    def start_csv_job(self, request):
        try:
            self._requestPath = "/panorama/v4/import/csv/python/start"
            self.httpProfile.reqMethod = "POST"
            self._default_content_type = 'application/json'
            self.httpProfile.keepAlive = 3000
            params = request.to_json_string()
            c = cookie.Cookie()
            print(c.get_cookie())
            self._default_token = c.get_cookie()
            body, header = self.call(params)
            print("body:", body)
            return body
        except Exception as e:
            if isinstance(e, PanSDKException):
                raise
            else:
                raise PanSDKException(e.code, e.message)