import time
import uiautomator2 as u2
from njtest.common import nj_cmd
from njtest.ui2 import browser
from selenium.webdriver.common.action_chains import ActionChains
import threading


def find_text(d, txt, times=2):
    '''
        查找元素并点击
    :param txt:要查找的文字
    :return:
    '''
    if d(text=txt).wait(timeout=times):
        d(text=txt).click()


def find_wifi(d, wifi_name, wifi_pwd, second=1):
    '''
        手机查找wifi切换
    :param wifi_name:wifi名称
    :param wifi_pwd:wifi密码
    :param second:次数
    :return:
    '''
    try:
        d.app_start('com.example.aux1')
        if d(text='取消').wait(timeout=2):
            d(text='取消').click()
        if nj_cmd.get_m_activity() == 'com.android.settings.wifi.WifiPickerActivity':  # 判断当前是否在wifi界面
            d.press("back")
        print(d(resourceId='com.example.aux1:id/wifi_name_tv').get_text(timeout=3))
        if second > 6:
            return False
        if not d(resourceId='com.example.aux1:id/wifi_name_tv').get_text(timeout=3) == wifi_name:
            d(resourceId='com.example.aux1:id/wifi_iv').click(timeout=3)
            locator = d(resourceId='android:id/title')
            d.swipe(0.5, 0.1, 0.5, 0.6, 0.5)
            if d(resourceId='com.android.settings:id/scanning_progress').wait(timeout=5):
                d(resourceId='com.android.settings:id/scanning_progress').wait_gone(timeout=20)
            second += 1
            try:
                if locator.wait(timeout=10):
                    time.sleep(0.3)
                    for zhi in range(6):
                        i = len(locator)
                        for view in locator:
                            get_value = view.get_text(timeout=6)
                            # print(get_value)
                            if get_value == wifi_name:
                                view.click(timeout=3)
                                if d(text='忘记').wait(timeout=2):
                                    d(text='取消').click(timeout=3)
                                if d(resourceId='com.android.settings:id/scanning_progress').wait(timeout=1):
                                    d(resourceId='com.android.settings:id/scanning_progress').wait_gone(timeout=6)
                                    time.sleep(4)
                                if d(text='连接').wait(timeout=2):
                                    if d(resourceId='com.android.settings:id/password').wait(timeout=1):
                                        d(resourceId='com.android.settings:id/password').set_text(wifi_pwd)
                                    d(text='连接').click(timeout=3)
                                if d(resourceId='com.android.settings:id/scanning_progress').wait(timeout=1):
                                    d(resourceId='com.android.settings:id/scanning_progress').wait_gone(timeout=6)
                                time.sleep(2)
                                return find_wifi(d, wifi_name, wifi_pwd, second)  # 再次确定wifi名称
                            elif get_value in '添加网络':
                                if wifi_pwd is None:
                                    view.click(timeout=3)  # 点击添加网络
                                    if d(resourceId='com.android.settings:id/ssid').wait(timeout=6):
                                        d(text='输入网络名称').set_text(wifi_name)
                                        d(text='连接').click(timeout=3)
                                    time.sleep(2)
                                    return find_wifi(d, wifi_name, wifi_pwd, second)  # 再次确定wifi名称
                                else:
                                    return find_wifi(d, wifi_name, wifi_pwd, second)  # 再次确定wifi名称
                        x, y = locator[i - 2].center()
                        x1, y1 = locator[0].center()
                        d.swipe(x, y, x1, y1, 1)
                return find_wifi(d, wifi_name, wifi_pwd, second)  # 再次确定wifi名称
            except Exception as err:
                # print('系统wifi界面报错：' + str(err))
                return find_wifi(d, wifi_name, wifi_pwd, second)
        else:
            return True
    except Exception as err:
        print('切换wifi报错：' + str(err))


def start(br):
    '''
        初始启动访问路由后台
    :param br: 游览器
    :return:
    '''
    br.d.get('http://192.168.7.1/html/index.html')
    br.find_click(("link text", "无线设置"), 3)


def set_name_pwd(br, username, password, check=False):
    '''
        更换路由名称和密码
    :param br:游览器
    :param username:路由名称
    :param password:路由密码
    :param check:是否只查
    :return:
    '''
    br.set_scroll(0)
    if check:
        return br.d.find_element("css selector", "input[name='wifiSSID']").get_attribute('value')
    br.find_input(("css selector", "input[name='wifiSSID']"), username, 3)
    br.find_input(("css selector", "input[name='wifiPwd']"), password, 3)


def set_pwd_mode(br, mode, password='', check=False):
    '''
        加密方式
    :param br:游览器
    :param mode:路由模式【open，WPA，WPA2，WPA/WPA2】
    :param password:路由密码
    :param check:是否只查
    :return:
    '''
    br.set_scroll(0)
    if check:
        return br.d.find_element("css selector", "select[id='wifiSecurityMode'][class='form-control']").get_attribute(
            'value')
    br.find_click(("css selector", "select[id='wifiSecurityMode'][class='form-control']"), 3)  # 点击加密方式
    if mode == 'open':
        br.find_click(("css selector", "option[value='NONE']"), 3)  # 设置加密方式
    elif mode == 'WPA':
        br.find_click(("css selector", "option[value='WPA/AES']"), 3)
        br.find_input(("css selector", "input[name='wifiPwd']"), password, 3)
    elif mode == 'WPA2':
        br.find_click(("css selector", "option[value='WPA2/AES']"), 3)
        br.find_input(("css selector", "input[name='wifiPwd']"), password, 3)
    elif mode == 'WPA/WPA2':
        br.find_click(("css selector", "option[value='WPAWPA2/AES']"), 3)
        br.find_input(("css selector", "input[name='wifiPwd']"), password, 3)


def set_wifi_hide(br, value, check=False):
    '''
        设置wifi是否隐藏
    :param br:游览器
    :param value:True,False
    :param check:是否只查
    :return:
    '''
    br.set_scroll(0)
    state = br.d.find_element("css selector", "input[type='checkbox'][name='wifiHideSSID']")
    if check:
        return state.is_selected()
    if value:
        if not state.is_selected():
            state.click()
    else:
        if state.is_selected():
            state.click()


def set_wifi_mode(br, value, check=False):
    '''
        设置wifi模式
    :param br:游览器
    :param value:【bgn，bg，g，b】
    :param check:是否只查
    :return:
    '''
    br.set_scroll(1000)
    if check:
        return br.d.find_element("css selector", "select[id='wifiMode'][class='form-control']").get_attribute('value')
    br.find_click(("css selector", "select[id='wifiMode'][class='form-control']"), 3)
    if value == 'bgn':
        br.find_click(("css selector", "option[value='bgn']"), 3)
    elif value == 'bg':
        br.find_click(("css selector", "option[value='bg']"), 3)
    elif value == 'g':
        br.find_click(("css selector", "option[value='g']"), 3)
    elif value == 'b':
        br.find_click(("css selector", "option[value='b']"), 3)


def set_wifi_channel(br, value, check=False):
    '''
        设置wifi信道
    :param br:游览器
    :param value:【1-13】
    :param check:是否只查
    :return:
    '''
    br.set_scroll(1000)
    if check:
        return br.d.find_element("xpath", "//select[@id='wifiChannel']").get_attribute('value')
    br.find_click(("xpath", "//select[@id='wifiChannel']"), 3)
    br.find_click(("xpath", "//select[@id='wifiChannel']/option[@value='{}']".format(value)), 3)


def set_wifi_bandwidth(br, value, check=False):
    '''
        设置wifi频宽
    :param br:游览器
    :param value:频宽【20,40,auto】
    :param check:是否只查
    :return:
    '''
    br.set_scroll(1000)
    if check:
        return br.d.find_element("xpath", "//select[@id='wifiBandwidth']").get_attribute('value')
    br.find_click(("xpath", "//select[@id='wifiBandwidth']"), 3)
    br.find_click(("xpath", "//select[@id='wifiBandwidth']/option[@value='{}']".format(value)), 3)


def keep_wifi(br):
    '''
       保存wifi设置
    :param br:游览器
    :return:
    '''
    br.find_click(("css selector", "button[id='submit'][class='btn btn-frist btn-primary']"), 3)
    br.find_alert(br, 'yes')
    time.sleep(1)


if __name__ == "__main__":
    # 游览器模拟运行
    br = browser.Browser()
    start(br)
    print(set_name_pwd(br, 'bl_tenda1', 'nj12345678', True))
    print(set_pwd_mode(br, 'WPA', '', True))
    print(set_wifi_hide(br, False, True))
    print(set_wifi_mode(br, 'b', True))
    print(set_wifi_channel(br, '4', True))
    print(set_wifi_bandwidth(br, '20', True))
    # set_name_pwd(br, 'bl_tenda', 'nj12345678', False)
    keep_wifi(br)
    # 手机运行,切换WiFi密码
    # d1 = u2.connect("")
    # while True:
    #     print('换网---BL_huawei')
    #     find_wifi(d1, 'BL_huawei', 'nj12345678')
    #     print('换网---mdww')
    #     find_wifi(d1, 'mdww', 'nj12345678')
