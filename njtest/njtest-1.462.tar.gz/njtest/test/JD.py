import threading
import time
import uiautomator2 as u2
from njtest.common import nj_cmd
from njtest.serial import nj_serial
from njtest.test import System


class JDTest(object):
    __instance = None
    __first_ap_init = False

    def __new__(cls, d):  # 创建类对象时调用
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, d):  # 创建成功调用
        if not self.__first_ap_init:
            self.__first_ap_init = True
            self.d = d
            self.package_name = 'com.jd.smart'
            self.sess = None
            self.one = True

    def find_wifi(self, wifi_name, wifi_pwd):
        '''
            切换wifi
        :param wifi_name:wifi名称
        :param wifi_pwd:wifi密码
        :return:
        '''
        # self.d.app_stop('com.jd.smart')
        System.find_wifi(self.d, wifi_name, wifi_pwd)  # 切换wifi
        time.sleep(1)
        self.d.app_start('com.jd.smart')  # 回到京东
        time.sleep(1)

    def find_text(self, txt, times=2):
        '''
            查找元素并点击
        :param txt:要查找的文字
        :return:
        '''
        if self.d(text=txt).wait(timeout=times):
            self.d(text=txt).click()

    def find_activity(self):
        '''
            查找Activity判断页面
        :param txt:查找的activity
        :return:
        '''
        try:
            self.d.app_start('com.jd.smart')
            activity = nj_cmd.get_m_activity()
            # print(activity)
            time.sleep(3)
            if not self.d(text='我的家').wait(timeout=1.5):
                self.d.press("back")
                self.find_activity()
        except Exception as err:
            print('find_activity：' + str(err))
            self.find_activity()

    def result_text(self, texts, times):
        '''
            判断是否到继续测试
        :param texts:搜索文字
        :param times:超时时间
        :return:
        '''
        start_time = time.time()
        while True:
            try:
                if texts in self.d(resourceId='com.jd.smart:id/tv_action').get_text(timeout=2):
                    return True
                else:
                    if time.time() - start_time > times:
                        return False
            except Exception as err:
                print("result_text报错：" + str(err))
            time.sleep(1)

    def direct_init(self, device_name):
        '''
            直接配网初始化
        :param device_name:设备名称
        :return:
        '''
        try:
            threading.Thread(target=self.find_text, args=('重新打开应用程序',)).start()
            threading.Thread(target=self.find_text, args=('稍后提醒',)).start()
            if self.sess is None or not self.sess.running():
                if 'com.jd.smart' in nj_cmd.get_m_package():
                    self.d.app_stop(self.package_name)
                self.d.app_start(self.package_name)
                self.sess = self.d.session(self.package_name, attach=True)
            self.find_activity()
            if self.d(text=device_name).wait(timeout=9):  # 发现并删除设备
                self.d(text=device_name).click(timeout=2)
                self.d(resourceId='com.jd.smart:id/web_title').wait(timeout=6)
                self.d(resourceId='com.jd.smart:id/web_title').click(offset=(0.9, 0.5), timeout=3)
                self.d(text='删除设备').wait(timeout=6)
                self.d(text='删除设备').click(timeout=3)
                self.d(text='确定').wait(timeout=7)
                self.d(text='确定').click(timeout=3)
            self.d(resourceId='com.jd.smart:id/iv_right').click(timeout=3)  # 点击+号
            self.d(text='添加设备').wait(timeout=10)
            self.d(resourceId='com.jd.smart:id/iv_history').click(timeout=20)
            self.d(resourceId='com.jd.smart:id/iv_history').wait_gone(timeout=60)
            self.d(text='已添加设备').click(timeout=3)
            while not self.d(text=device_name).wait(timeout=1):
                self.d.drag(0.5, 0.2, 0.5, 0.6)
                self.d(resourceId='com.jd.smart:id/pull_to_refresh_gifimage').wait(timeout=2)
                self.d(resourceId='com.jd.smart:id/pull_to_refresh_gifimage').wait_gone(timeout=60)
            self.d(text=device_name).click(timeout=8)
            self.d(text=device_name).wait_gone(timeout=60)
        except Exception as err:
            print('direct_init报错：' + str(err))
            self.direct_init(device_name)

    def smap_network(self, device_name, wifi_name, wifi_pwd, ser, cmd):
        '''
            直接一键配网
        :param device_name:设备名称
        :param wifi_name:WiFi名称
        :param wifi_pwd:wifi密码
        :param ser:串口
        :param cmd:复位指令
        :return:是否配网成功
        '''
        try:
            self.direct_init(device_name)  # 直接配网初始化
            self.find_wifi(wifi_name, wifi_pwd)  # 切换wifi
            self.d(resourceId='com.jd.smart:id/tv_pwd').wait(timeout=6)  # 搜索wifi界面
            self.d(resourceId='com.jd.smart:id/tv_pwd').set_text(wifi_pwd)  # 输入wifi密码
            self.d(text='请选择设备要加入的Wi-Fi').click(timeout=2)  # 隐藏输入键盘
            ser.send_cmd(cmd)  # 串口复位
            time.sleep(0.5)
            ser.send_cmd(cmd)  # 串口复位
            self.d(text='下一步').click(timeout=6)
            self.d(resourceId='com.jd.smart:id/id_cb_tip').click(timeout=6)
            time.sleep(1)
            self.d(text='下一步').click(timeout=2)
            self.d(text='添加中').wait(timeout=2)
            if self.result_text('完成', 63):  # 判断是否搜索到设备
                self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)
                return True
            else:
                self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)
                return False
        except Exception as err:
            print('smap_network报错：' + str(err))
            return self.smap_network(device_name, wifi_name, wifi_pwd, ser, cmd)

    def ap_network(self, device_name, wifi_name, wifi_pwd, ser, cmd, ap_wifi, ap_pwd):
        '''
            直接ap配网
        :param device_name:设备名称
        :param wifi_name:wifi名称
        :param wifi_pwd:wifi密码
        :param cmd:复位指令
        :param ap_wifi:ap—wifi名称
        :param ap_pwd:ap-wifi密码
        :return:
        '''
        try:
            self.find_wifi(wifi_name, wifi_pwd)  # 切换wifi
            self.direct_init(device_name)  # 直接配网初始化
            self.d(resourceId='com.jd.smart:id/tv_pwd').wait(timeout=6)  # 搜索wifi界面
            self.d(resourceId='com.jd.smart:id/tv_pwd').set_text(wifi_pwd)  # 输入wifi密码
            self.d(text='请选择设备要加入的Wi-Fi').click(timeout=2)  # 隐藏输入键盘
            ser.send_cmd(cmd)  # 串口复位
            time.sleep(0.5)
            self.d(text='下一步').click(timeout=6)
            self.d(resourceId='com.jd.smart:id/id_cb_tip').click(timeout=6)
            time.sleep(1)
            self.d(text='下一步').click(timeout=2)
            self.d(text='添加中').wait(timeout=2)
            if self.d(text="去连接").wait(timeout=25):
                self.find_wifi(ap_wifi, ap_pwd)  # 切换wifi
                if self.result_text('完成', 25):
                    self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)
                    return True
                else:
                    self.find_wifi(wifi_name, wifi_pwd)  # 切回wifi
            else:
                if self.result_text('完成', 2):
                    self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)
                    return True
                else:
                    self.find_wifi(wifi_name, wifi_pwd)  # 切回wifi
            while True:
                if not self.d(resourceId='com.jd.smart:id/tv_action').exists():  # 判断是否在配网界面
                    return False
                if self.result_text('完成', 1):  # 判断是否搜索到设备
                    self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)
                    return True
                elif self.result_text('联网失败，再试一次', 1):
                    self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)
                    return False
        except Exception as err:
            print('ap_network报错：' + str(err))
            return self.ap_network(device_name, wifi_name, wifi_pwd, ser, cmd, ap_wifi, ap_pwd)

    def test_init(self, device_name):
        '''
            测试入口初始化
        :param device_name:设备名称
        :return:
        '''
        try:
            self.d.app_start(self.package_name)
            self.sess = self.d.session(self.package_name, attach=True)
            self.find_activity()
            self.d(text='测').click(timeout=3)
            self.d(text='开始测试')[0].click(timeout=3)
            self.d(text='添加设备').wait(timeout=10)
            self.d(resourceId='com.jd.smart:id/iv_history').click(timeout=20)
            self.d(resourceId='com.jd.smart:id/iv_history').wait_gone(timeout=60)
            self.d(text='已添加设备').click(timeout=3)
            while not self.d(text=device_name).wait(timeout=1):
                self.d.drag(0.5, 0.2, 0.5, 0.6)
                self.d(resourceId='com.jd.smart:id/pull_to_refresh_gifimage').wait(timeout=2)
                self.d(resourceId='com.jd.smart:id/pull_to_refresh_gifimage').wait_gone(timeout=60)
            self.d(text=device_name).click(timeout=8)
            self.d(text=device_name).wait_gone(timeout=60)
        except Exception as err:
            print("test_init报错:" + str(err))
            self.test_init(device_name)

    def test_smap_network(self, device_name, wifi_name, wifi_pwd, ser, cmd):
        '''
            测试一键配网
        :param device_name:设备名称
        :param wifi_name:wifi名称
        :param wifi_pwd:wifi密码
        :param ser:串口
        :param cmd:复位指令
        :return:
        '''
        try:
            self.find_wifi(wifi_name, wifi_pwd)  # 切换wifi
            threading.Thread(target=self.find_text, args=('重新打开应用程序',)).start()
            threading.Thread(target=self.find_text, args=('稍后提醒',)).start()
            if self.sess is None or not self.sess.running():
                if 'com.jd.smart' in nj_cmd.get_m_package():
                    self.d.app_stop(self.package_name)
                self.test_init(device_name)
            else:
                self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)  # 继续测试
            self.d(resourceId='com.jd.smart:id/tv_pwd').wait(timeout=6)  # 搜索wifi界面
            self.d(resourceId='com.jd.smart:id/tv_pwd').set_text(wifi_pwd)  # 输入wifi密码
            self.d(text='请选择设备要加入的Wi-Fi').click(timeout=2)  # 隐藏输入键盘
            ser.send_cmd(cmd)  # 串口复位
            time.sleep(0.5)
            self.d(text='下一步').click(timeout=6)
            self.d(resourceId='com.jd.smart:id/id_cb_tip').click(timeout=6)
            time.sleep(1)
            self.d(text='下一步').click(timeout=2)
            self.d(text='添加中').wait(timeout=2)
            if self.result_text('继续测试', 63):  # 判断是否搜索到设备
                return True
            else:
                return False
        except Exception as err:
            print("test_smap_network报错:" + str(err))
            self.test_smap_network(device_name, wifi_name, wifi_pwd, ser, cmd)

    def test_ap_network(self, device_name, wifi_name, wifi_pwd, ser, cmd, ap_wifi, ap_pwd):
        '''
            test入口进行ap配网
        :param device_name:设备名称
        :param wifi_name:wifi名称
        :param wifi_pwd:wifi密码
        :param cmd:复位指令
        :param ap_wifi:ap—wifi名称
        :param ap_pwd:ap-wifi密码
        :return:
        '''
        try:
            self.find_wifi(wifi_name, wifi_pwd)  # 切换wifi
            threading.Thread(target=self.find_text, args=('重新打开应用程序',)).start()
            threading.Thread(target=self.find_text, args=('稍后提醒',)).start()
            if self.sess is None or not self.sess.running():
                if 'com.jd.smart' in nj_cmd.get_m_package():
                    self.d.app_stop(self.package_name)
                self.test_init(device_name)
            else:
                self.d(resourceId='com.jd.smart:id/tv_action').click(timeout=2)  # 继续测试
            self.d(resourceId='com.jd.smart:id/tv_pwd').wait(timeout=6)  # 搜索wifi界面
            self.d(resourceId='com.jd.smart:id/tv_pwd').set_text(wifi_pwd)  # 输入wifi密码
            self.d(text='请选择设备要加入的Wi-Fi').click(timeout=2)  # 隐藏输入键盘
            ser.send_cmd(cmd)  # 串口复位
            time.sleep(0.5)
            self.d(text='下一步').click(timeout=6)
            self.d(resourceId='com.jd.smart:id/id_cb_tip').click(timeout=6)
            time.sleep(1)
            self.d(text='下一步').click(timeout=2)
            self.d(text='添加中').wait(timeout=2)
            if self.d(text="去连接").wait(timeout=35):
                self.find_wifi(ap_wifi, ap_pwd)  # 切换wifi
                if self.result_text('继续测试', 25):
                    return True
                else:
                    self.find_wifi(wifi_name, wifi_pwd)  # 切回wifi
            else:
                if self.result_text('继续测试', 1):
                    return True
                else:
                    self.find_wifi(wifi_name, wifi_pwd)  # 切回wifi
            if self.result_text('继续测试', 180):  # 判断是否搜索到设备
                return True
            else:
                return False
        except Exception as err:
            print("test_ap_network报错:" + str(err))
            self.test_ap_network(device_name, wifi_name, wifi_pwd, ser, cmd, ap_wifi, ap_pwd)

    def add_device(self):
        '''
            JD测试入口进入配网
        :return:
        '''
        sum = 0
        count = 0
        # while not self.d(text="我知道了").wait(timeout=1.5):
        #     sum += 1
        #     a = jd.test_ap_network('通用KV测试产品古北空调', 'BL_tenda', 'nj12345678', ser, 'A5 A5 5A 5A 9A C1 EA 03 00 00 00 00',
        #                            'JDKongTiao0039', '12345678')
        #     # a = jd.test_smap_network('雷士-LED台灯', 'BL_xiaomi', 'nj12345678', ser, 'A5 A5 5A 5A 98 C1 E8 03 00 00 00 00')
        #     if a:
        #         count += 1
        #     print(count, sum)
        # self.d.screenshot('./配网.png')
        for i in range(11000000):
            sum += 1
            a = jd.ap_network('通用KV测试产品古北空调', 'BL_tenda', 'nj12345678', ser, 'A5 A5 5A 5A 9A C1 EA 03 00 00 00 00',
                              'JDKongTiao0039', '12345678')
            # a = jd.smap_network('雷士-LED台灯', 'BL_xiaomi', 'nj12345678', ser, 'A5 A5 5A 5A 98 C1 E8 03 00 00 00 00')
            if a:
                count += 1
            print(count, sum)


if __name__ == "__main__":
    d1 = u2.connect("")
    jd = JDTest(d1)
    ser = nj_serial.Ser()
    ser.connect(port='COM14', baudrate=9600, parity='N')
    jd.add_device()
    print('1')
    ser.stop_serial()
    print('通过')
