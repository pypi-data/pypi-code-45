import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

'''
pip install Appium-Python-Client  安装WebDriverWait
https://blog.csdn.net/cz9025/article/details/70160273
'''


class Browser(object):
    __instance = None
    __first_init = False

    def __new__(cls, tips=True):  # 创建类对象时调用
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, tips=True):  # 创建成功调用
        '''
            电脑游览器控制
        :param tips:错误提示是否打开
        '''
        self.tips = tips
        if not self.__first_init:
            chromedriver = "C:/Users/Apply/chromedriver/78/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.d = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
            self.d.maximize_window()  # 窗口最大化

    def find_click(self, locator, times=3, sleep=True):
        '''
            发现元素并且点击
        :param locator:元素
        :param times:超时时间
        :return:
        '''
        if self.wait(locator, times):
            self.d.find_element(*locator).click()
            if sleep:
                time.sleep(0.5)

    def find_input(self, locator, value, times=3, clean=True):
        '''
            发现元素并且输出值
        :param locator: 元素
        :param value: 输入值
        :param times: 发现超时时间
        :param clean: 是否清空
        :return:
        '''
        if self.wait(locator, times):
            if clean:
                loc = self.d.find_element(*locator)
                loc.send_keys(Keys.CONTROL + 'a')  # 清空原有数据
            self.d.find_element(*locator).send_keys(value)

    def find_alert(self, value):
        '''
            发现警觉弹框
        :param value:yes,no
        :return:警告框信息
        '''
        try:
            a = br.d.switch_to_alert()
            text = a.text
            if value == 'yes':
                a.accept()
            else:
                a.dismiss()
            return text
        except Exception as err:
            pass

    def set_scroll(self, height):
        '''
            设置游览器滑动条
        :param height:滑动值
        :return:
        '''
        js_top = "var q=document.documentElement.scrollTop={}".format(height)
        # js_bot = "var q=document.documentElement.scrollTop={}".format(height)
        self.d.execute_script(js_top)
        time.sleep(1)
        # time.sleep(10)
        # self.d.execute_script(js_top)

    def find_list(self, name, text):
        S = Select(self.d.find_element_by_name('cars')).select_by_visible_text('Audi')

    def wait(self, locator, times=3):
        '''
            循环查找元素
            文本定位("link text", "无线设置")
            xpath定位("xpath", "//*[@id='form']/span/input[@id='kw']")
            多个元素定位("css selector", "li[class='lgBtns'][id='loginSub']")
        :param locator:("css selector", "li[class='lgBtns']>a[id='loginSub']")
        :param times:查找多长时间
        :return:
        '''
        try:
            WebDriverWait(self.d, times, 0.2).until(lambda x: x.find_element(*locator))
            return True
        except Exception as err:
            if self.tips:
                print("{}元素不存在：{}".format(str(locator), str(err)))
            return False

    def wait_gone(self, locator, times=3):
        '''
            循环等待元素消失
        :param locator:元素定位
        :param times:超时时间
        :return:
        '''
        try:
            start_time = time.time()
            while time.time() - start_time < times:
                if not self.wait(locator, 0.3):
                    return True
        except Exception as err:
            if self.tips:
                print(err)

    '''
        self.d.get(path) 打开网址
        self.d.quit() 退出
        self.d.find_element(*locator).click() 点击
        self.d.find_element(*locator).send_keys(value) 输入
        self.d.find_element(*locator).text 获取文本
        is_selected() 判断是否选中
    '''


if __name__ == "__main__":
    br = Browser()
    br.d.get('http://192.168.7.1/html/index.html')
    br.set_scroll(100)
    br.find_click(("link text", "无线设置"), 3)
    br.find_input(("css selector", "input[name='wifiSSID']"), 'BL_tenda1', 3)
