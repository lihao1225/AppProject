from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

class TestToast:

    def setup(self):
        desired_caps = {}
        # 连接的系统
        desired_caps["platformName"] = "Android"
        # 连接的版本
        desired_caps["platformVersion"] = "6.0"
        # 连接用户名
        desired_caps["deviceName"] = "emulator-5554"
        # 连接app的名字
        desired_caps["appPackage"] = "io.appium.android.apis"
        # 连接app进入的页面
        desired_caps["appActivity"] = "io.appium.android.apis.view.PopupMenu1"
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

    def test_toast1(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id = 'android:id/title' and @text = 'Search']").click()
        toast = self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']").text
        print(toast)
        assert 'Clicked popup menu item Search' == toast

    def test_hamcrest(self):
        assert_that(9 ,equal_to(10),"错误提示")