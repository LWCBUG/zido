#!/usr/bin/env python
# coding=utf-8
# import time
from selenium import webdriver
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# import requests
# from selenium.webdriver.common.keys import Keys


# 自动化操作创研系统的线索导入功能
def ui_auto_operation():
    # 模拟登陆
    # rep = requests.Session()
    browser = webdriver.Edge(EdgeChromiumDriverManager().install())
    browser.implicitly_wait(10)  # 设置隐性等待,等待10S加载出相关控件再执行之后的操作
    browser.maximize_window()
    browser.get('http://121.5.10.180:9999')
    # time.sleep(10) # 强制等待一般只用于测试
    # browser.refresh()
    # 输入用户名
    username = browser.find_element(By.ID,"accountid")
    username.clear()
    username.send_keys('admin')
    print('username input success')
    # 输入密码
    pwd=browser.find_element(By.ID,"accountpwd")
    pwd.clear()
    pwd.send_keys("000000")
    print('password input success')
    # # 加载验证码
    # yzm = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/dl[3]/dd/input')
    # yzm.send_keys(input('输入验证码:'))
    # 点击登陆
    browser.find_element(By.ID,"loginBtn").click()
    print('login success')
    browser.find_element(By.XPATH,'//*[@id="noticeModal"]/div/div/div[3]/button').click()
    time.sleep(30)
    browser.find_element(By.CLASS_NAME,'dropdown-toggle').click()
    browser.implicitly_wait(30)
    browser.find_element(By.XPATH,'//*[@id="operationMenuBox"]/a').click()
    browser.implicitly_wait(15)
    browser.find_element(By.XPATH,'//*[@id="uploadFileButtonLi"]/a').click()
    browser.implicitly_wait(15)
    browser.find_element(By.ID,"uploadfile").send_keys(r"C:\service.zip")
    # os.system(r"C:\Users\24218\Documents\1.exe")
    time.sleep(30)
    browser.find_element(By.ID,'umbutton').click()
    time.sleep(3000)
    browser.close()
    # browser.quit()
    # # cookies = browser.get_cookies()
    # # for cookie in cookies:
    # #    rep.cookies.set(cookie['name'], cookie['value'])
    # # 爬取对应网页的数据
    # browser.current_window_handle
    # browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[8]/div/a/span').click()
    # # 切换到当前窗口
    # browser.current_window_handle
    # # time.sleep(5)
    # tow_drive = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[8]/ul/li[5]/a')
    # tow_drive.click()
    # print('turn success')
    # browser.current_window_handle
    # # time.sleep(2)
    # # 切换到iframe框架里面
    # browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="mainFrame"]'))
    # # # 输入框只读属性的修改
    # # js = 'document.getElementById("Text1").removeAttribute("readonly");'
    # # browser.execute_script(js)
    # # # 定位并且输入路径数据
    # # receiveStart = browser.find_element_by_xpath('//*[@id="Text1"]')
    # # receiveStart.clear()
    # # receiveStart.send_keys('C:\\fakepath\\5096.xls')
    # # # receiveStart.send_keys(Keys.RETURN)
    # # 点击上传文件按钮
    # browser.find_element_by_xpath('//*[@id="btn1"]').click()
    #
    # # 调用写好的exe实现上传,autoup.exe的建立参考下面的网站
    # # https://www.cnblogs.com/sunjump/p/7268805.html
    # os.system("C:\\fakepath\\autoup.exe")
    # # time.sleep(5)
    # load = browser.find_element_by_xpath('//*[@id="btn_lead"]')
    # load.click()
    # try:
    #     # 每隔2s就去扫描弹出框是否存在,总时长是60s,存在就继续执行之后代码
    #     WebDriverWait(browser, 60, 2).until(EC.alert_is_present())
    #     # 处理弹出alert框
    #     alert = browser.switch_to.alert
    #     alert.accept()
    # finally:
    #     browser.close()
    #     # browser.quit()

ui_auto_operation()
# if __name__ == '__main__':
#     # @version : 3.4
#     # @Author  : robot_lei
#     # @Software: PyCharm Community Edition
#     ui_auto_operation()