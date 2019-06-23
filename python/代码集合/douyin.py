from HTMLTestReportCN import HTMLTestRunner
import unittest
from appium import webdriver
from time import sleep
import warnings
import selenium
from time import sleep
import unittest
from diesheng2.config import ds
class DS(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.des = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity",
            "noReset": "true",
        }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5.0)
    def test_1(self):
        self.dr.find_element_by_id('com.ss.android.ugc.aweme:id/a2f ').click()