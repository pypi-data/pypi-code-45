#     LOFTER-POP-INDEX, an automatic tool used for increase LOFTER blogs' popular index.
#     Copyright (C) 2019  PengFCB
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


from selenium import webdriver
from time import sleep
import random


def create_window(proxy_flag, ip=''):
    print('\033[0minit chrome')
    chromeOptions = webdriver.ChromeOptions()
    if proxy_flag:
        chromeOptions.add_argument('--proxy-server=http://'+ip)
        print('proxy:'+ip)
    try:
        driver = webdriver.Chrome(options=chromeOptions)
    except:
        try:
            driver = webdriver.Chrome('./chromedriver', options=chromeOptions)
        except:
            print('\033[31m unable found correct chromedriver')
            eixt(0)
    print('chrome have been inited')
    return driver


def login_page(driver):
    print('Loading login page')
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.get(f"http://www.lofter.com")
    sleep(5)
    print("Finish loading login page")
    return driver


def login(driver, account):
    print("logging in account" + account[0] + account[1])
    frame = driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]")
    driver.switch_to.frame(frame)
    driver.find_element_by_css_selector("form input[class='j-inputtext dlemail j-nameforslide']").send_keys(account[0])
    driver.find_element_by_css_selector("form input[class='j-inputtext dlpwd']").send_keys(account[1])
    driver.find_element_by_id("dologin").click()
    sleep(5)
    print("Finish logging in")
    return driver


def target_page(driver, target):
    print("Loading target blog:"+target)
    js = 'window.open("' + target + '");'
    print(js)
    driver.execute_script(js)
    sleep(10)
    print("Finish loading target blog")
    return driver


def switch_window(driver, index):
    handles = driver.window_handles
    driver.switch_to.window(handles[index])
    sleep(2)
    return driver


def exec_hot(driver, percent=100, follow_flag=0):
    print("Increasing popular index")
    driver.switch_to.frame("control_frame")
    driver.find_element_by_link_text("喜欢").click()
    if random.randint(0, 100) < percent:
        driver.find_element_by_link_text("推荐").click()
    if follow_flag:
        driver.find_element_by_link_text("添加关注").click()
    sleep(5)
    return driver


def one_loop(account, target_list, proxy_flag=1, ip='', percent_of_recommend=100, follow_flag=0):
    exception_flag = 0
    driver = create_window(proxy_flag, ip)
    try:
        driver = login_page(driver)
        driver = login(driver, account)
        for i in range(len(target_list)):
            driver = target_page(driver, target_list[i])
            driver = switch_window(driver, i+1)
            driver = exec_hot(driver, percent_of_recommend, follow_flag)
        driver.quit()
        print("Completed current loop\n")
        return exception_flag
    except:
        exception_flag = 1
        print("Detected exception!\n")
        driver.quit()
        return exception_flag


if __name__ == '__main__':

    exit(0)
