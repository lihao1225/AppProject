from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestApp:

    def setup(self):
        desired_caps = {}
        # 连接的系统
        desired_caps["platformName"] = "Android"
        # 连接的版本
        desired_caps["platformVersion"] = "6.0"
        # 连接用户名
        desired_caps["deviceName"] = "emulator-5554"
        # 连接app的名字
        desired_caps["appPackage"] = "com.xueqiu.android"
        # 连接app进入的页面
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 是否在测试后进行重制（清除缓存）
        desired_caps["noReset"] = True
        # 输入中文
        desired_caps["unicodeKeyBoard"] = "true"
        # 首次启动的时候，不停止app
        # desired_caps["dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    @pytest.mark.skip
    def test_start(self):
        search_ele = self.driver.find_element(By.XPATH, "//*[@resource-id ='com.xueqiu.android:id/tv_search']")
        # 判断元素是否可用
        search_ele.is_enabled()
        search_ele.get_attribute("name")
        print(search_ele.size)
        print(search_ele.location)
        search_ele.click()
        input_ele = self.driver.find_element(By.XPATH, "//*[@resource-id ='com.xueqiu.android:id/search_input_text']")
        input_ele.send_keys("alibaba")
        alibab_ele = self.driver.find_element(By.XPATH,
                                              "//*[@resource-id ='com.xueqiu.android:id/name' and @text = '阿里巴巴']")
        if True == alibab_ele.is_displayed():
            print("搜索成功")
        else:
            print("搜索失败")

    def test_touch_action(self):
        self.driver.find_element(By.XPATH, "//*[@resource-id ='com.xueqiu.android:id/tv_search']")
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        height = window_rect["height"]
        width = window_rect["width"]
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        
