import json
import threading
import uuid

from paho.mqtt import client as mqtt

from adapay_core.log_util import log_info, log_error


class AdapayMessage:

    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token

        self.group_id = 'GID_CRHS_ASYN'
        self.client_id = self.group_id + '@@@' + str(hash(api_key + (str(uuid.uuid1()))))
        self.topic = 'topic_crhs_sender/' + api_key

        self.instance_id = 'post-cn-0pp18zowf0m'
        self.access_key = 'LTAIOP5RkeiuXieW'
        self.broker_url = 'post-cn-0pp18zowf0m.mqtt.aliyuncs.com'


        self.connect_callback = None
        self.subscribe_callback = None
        self.received_callback = None

    def set_connect_callback(self, connect_callback):
        self.connect_callback = connect_callback

    def set_subscribe_callback(self, subscribe_callback):
        self.subscribe_callback = subscribe_callback

    def set_received_callback(self, received_callback):
        self.received_callback = received_callback

    def subscribe(self):
        pay_msg_thread = threading.Thread(target=self._execute)
        pay_msg_thread.start()

    def _on_connect(self, client, userdata, flags, resp_code):
        """
        建立长连接成功回调
        """
        log_info('connected with result code ' + str(resp_code))

        if self.connect_callback is not None:
            self.connect_callback(resp_code)

        if resp_code == 0:
            client.subscribe(self.topic, 0)

    def _on_disconnect(self, client, userdata, resp_code):
        """
        :param resp_code:
         长连接链接失败回调
        1	伪造 Token，不可解析
        2	Token 已经过期
        3	Token 已经被吊销
        4	资源和 Token 不匹配
        5	权限类型和 Token 不匹配
        8	签名不合法
        -1	帐号权限不合法

        :return:
        """
        log_info('unexpected disconnection %s' % resp_code)

        if self.connect_callback is not None:
            self.connect_callback(resp_code)

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        """
        订阅成功回调
        """
        log_info('on_subscribe')
        if self.subscribe_callback is not None:
            self.subscribe_callback(0)

    def _on_unsubscribe(self, client, userdata, mid):
        """
        订阅成功回调
        """
        log_info('on_unsubscribe')
        if self.subscribe_callback is not None:
            self.subscribe_callback(-1)

    def _on_message(self, client, userdata, messages):
        """
        接收到交易结果回调
        """
        message_str = messages.payload.decode('utf-8')
        log_info('on_msg_receive:' + message_str)

        if self.received_callback is not None:
            try:
                msg_dict = json.loads(message_str)
                self.received_callback(msg_dict)
            except Exception as e:
                log_error(str(e))
                log_error('pay message loads error:' + message_str)

    def _execute(self):
        client = mqtt.Client(self.client_id, protocol=mqtt.MQTTv311, clean_session=True)

        client.on_connect = self._on_connect
        client.on_disconnect = self._on_disconnect
        client.on_subscribe = self._on_subscribe
        client.on_unsubscribe = self._on_unsubscribe
        client.on_message = self._on_message

        user_name = 'Token|' + self.access_key + '|' + self.instance_id
        password = 'R|' + self.token
        client.username_pw_set(user_name, password)
        client.connect(self.broker_url, 1883, 60)
        client.loop_forever()
