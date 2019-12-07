import threading
import time
import uiautomator2 as u2
from njtest.common import nj_cmd
from njtest.serial import nj_serial
from njtest.test import System


class HuaWeiTest(object):
    __instance = None
    __first_ap_init = False

    def __new__(cls, d, name):  # 创建类对象时调用
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, d, name):  # 创建成功调用
        if not self.__first_ap_init:
            self.__first_ap_init = True
            self.d = d
            self.package_name = 'com.huawei.smarthome'
            self.sess = None
            self.one = True
            self.name = name

    def find_home(self):
        '''
            查找Activity判断页面
        :param txt:查找的activity
        :return:
        '''
        try:
            if self.sess is None or not self.sess.running():
                if self.package_name in nj_cmd.get_m_package():
                    self.d.app_stop(self.package_name)
                self.d.app_start(self.package_name)
                self.sess = self.d.session(self.package_name, attach=True)
                self.d(text='家居').wait(timeout=10)
            while not self.d(text='家居').wait(timeout=2):
                self.d.press("back")
        except Exception as err:
            print('find_home：' + str(err))
            self.find_home()

    def find_text(self, txt, times=3):
        '''
            查找元素并点击
        :param txt:要查找的文字
        :return:
        '''
        while self.d(text=txt).wait(timeout=times):
            self.d(text=txt).click(timeout=times)

    def add_networking(self):
        '''
            华为配网
        :return:
        '''
        self.find_home()
        threading.Thread(target=self.find_text, args=('取消',)).start()
        if self.d(text=self.name).wait(timeout=5):
            self.d(text=self.name).click(timeout=2)
            self.d(resourceId='com.huawei.smarthome:id/hw_otherdevice_title_setting').click(timeout=12)
            self.d(text='删除设备').wait(timeout=12)
            while self.d(text='删除设备').wait(timeout=2):
                self.d(text='删除设备').click(timeout=3)
                self.d(text='删除').click(timeout=3)
        self.d(resourceId='com.huawei.smarthome:id/iv_deviceadd').click(timeout=3)
        self.d(text='添加设备').click(timeout=3)
        while not self.d(text='连接').wait(timeout=2):
            self.d(text='正在扫描…').wait(timeout=3)
            self.d(text='正在扫描…').wait_gone(timeout=30)
            if self.d(text='扫描完成，没有发现设备').wait(timeout=2):
                self.d(text='重新扫描').click(timeout=3)
        self.d(text='连接').click(timeout=3)
        self.d(text='下一步').wait(timeout=16)
        self.d(text='下一步').click(timeout=6)
        self.d(text='请将手机靠近设备与路由器').wait(timeout=3)
        self.d(text='请将手机靠近设备与路由器').wait_gone(timeout=120)
        if self.d(text='连接失败').wait(timeout=2):
            return False
        else:
            if self.d(text='完成').wait(timeout=2):
                self.d(text='完成').click(timeout=2)
            return True


if __name__ == "__main__":
    d1 = u2.connect("")
    hw = HuaWeiTest(d1, '雷士护眼灯')
    # ser = nj_serial.Ser()
    # ser.connect(port='COM', baudrate=9600, parity='N')
    count = 0
    second = 0
    for i in range(20):
        count += 1
        if hw.add_networking():
            second += 1
        print(second, count)
