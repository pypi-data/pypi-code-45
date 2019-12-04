from qcloudsms_py import SmsSingleSender


class QCloudSMS:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # config = app.config
        self.appid = app.config['QCLOUDSMS_APPID']
        self.appkey = app.config['QCLOUDSMS_APPKEY']
        self.default_sign = app.config['QCLOUDSMS_DEFAULT_SIGN']

    def send(self, phone, template_id, params, sign=None):
        ssender = SmsSingleSender(self.appid, self.appkey)
        result = ssender.send_with_param(
            86, phone, template_id, params, sign=sign or self.default_sign, extend="", ext=""
        )  # 签名参数不允许为空串
        return result
