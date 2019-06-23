import selenium
from appium import webdriver
from time import sleep
#建立与appium服务器需要的参数 以字典的形式
# des={
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.tencent.tim",
#     "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#     "noReset": "true",
#     # "unicodeKeyboard":"true",
#     # "resetKeyboard":"true"
# }
# des={
#     "device": "android",
#     "platformName": "Android",
#     "platformVersion": "9",
#     "deviceName": "4c928276",
#     "appPackage": "com.tencent.tim",
#     "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#     "noReset": "True",
#     "automationName": "uiautomator2"
# }
# # http://127.0.0.1:4723/wd/hub 固定的 写死的 不需要改  或者localhost=127.0.0.1
# # 测试脚本与appium服务器建立一个session连接
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# # 先清除输入框 再输入
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# # 安卓独有的定位  输入账号
# dr.find_element_by_accessibility_id('输入QQ号码或手机或邮箱请').send_keys('316986133')
# sleep(2)
# # 输入密码
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('qwer1234')
# # sleep(2)
# # 点击登录
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# sleep(10)
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.FrameLayout')[-1].click()
# sleep(10)
# t=dr.find_element_by_id('com.tencent.tim:id/lebasv').find_element_by_class_name('android.widget.RelativeLayout')[-1].click()
# print(a)
# sleep(10)
# for i in a:
#     sleep(2)
#     i.click()
#     sleep(2)


# dr.quit()

# 滑动操作
# 第一步获取手机屏幕大小
# s=dr.get_window_size()
# print(s)
# # # 第二部 放缩x y轴
# x1=s['width']*0.5
# y1=s['height']*0.15
# y2=s['height']*0.95
# #
# # # 第三步  使用swipe方法  进行滑动操作
# dr.swipe(x1,y2,x1,y1)
# sleep(3)
# print(6666)
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')a[-1].click()

#dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.TabWidget')
# dr.find_elements_by_class_name('android.widget.RelativeLayout')
# dr.find_elements_by_class_name('android.widget.TextView')
# x=dr.find_elements_by_class_name('android.widget.ImageView')
# print(x)
# x[1].click()
# sleep(2)
# x[2].click()
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# a[-1].click()
# t=dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name("android.widget.RelativeLayout")
# t[-1].click()
# sleep(1)


# 面向对象
# class Tim(object):
#     #初始化属性
#     def __init__(self):
#         #建立与appium服务器需要的参数 以字典的形式
#         self.des = {
#             "device": "android",
#             "platformName": "Android",
#             "platformVersion": "9",
#             "deviceName": "4c928276",
#             "appPackage": "com.tencent.tim",
#             "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#             "noReset": "True",
#             "automationName": "uiautomator2"
#         }
#         # http://127.0.0.1:4723/wd/hub 固定的 写死的 不需要改  或者localhost=127.0.0.1
#         # 测试脚本与appium服务器建立一个session连接
#         dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
#     def dian_zan(self):
#         #第一步 点击办公
#         a =dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.FrameLayout')[-1].click()
#         sleep(10)
#         # 点击好友动态
#         t =dr.find_element_by_id('com.tencent.tim:id/lebasv').find_element_by_class_name('android.widget.RelativeLayout')[
#             -1].click()


# from appium import webdriver
# from time import sleep
#
#
# # 面向对象
# class Tim(object):
#
#     # 初始化属性
#     def __init__(self):
#         # 建立与appium服务器需要的参数，以字典的形式
#         self.des = {
#             "device": "android",
#             "platformName": "Android",
#             "platformVersion": "9",
#             "deviceName": "46HDU19314003325",
#             "appPackage": "com.tencent.tim",
#             "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#             "noReset": "true",
#         }
#         # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
#         # 测试脚本与appium服务器建立一个session连接
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#         sleep(5)
#
#     # def dian_zan(self):
#     #     # 第一步，点击办公
#     #     self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[
#     #         -1].click()
#     #     # 第二步，点击好友动态
#     #     t = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name(
#     #         'android.widget.RelativeLayout')
#     #     t[-1].click()
#     #     sleep(0.5)
#     #     # 第三步 点赞
#     #     x = self.dr.find_elements_by_class_name('android.widget.ImageView')
#     #     print(x)
#     #     x[1].click()
#     #     sleep(2)
#     #     x[2].click()
#     #获取文字
#     # def get_wenzi(self):
#     #     c=self.dr.find_element_by_id('com.tencent.tim:id/ivTitleName').text
#     #     print(c)
#     #     return c
#     def anjian(self):
#         # 模拟人点击物理按键
#         #点击home
#         # self.dr.keyevent(3)
#         #点击返回键
#         self.dr.keyevent(4)
#         sleep(5)
#         #点击相机开启
#         self.dr.keyevent(27)
# # 调用类
# if __name__ == '__main__':
#     yasuo = Tim()
#     # yasuo.dian_zan()
#     # yasuo.get_wenzi()
#     yasuo.anjian()


# unittest 单元测试模块
# 生成html测试报告
import HTMLTestReportCN
# # 用于单元测试 验证预期结果和实际结果是否一致  一致代表通过 不一致代表失败
import unittest

# class T(unittest.TestCase):
#       # 测试用例方法 必须用test开头
#       def test_1(self):
#           #预期结果
#           x='宝马'
#           #实际结果
#           y='宝马'
#           # 第一个断言方法  判断预期结果与实际结果是否相等
#           # x ,y 位置是可以互换的
#           self.assertEqual(x,y,'msg的作用就是填写备注信息的')
#
#
# if __name__ == '__main__':
#     #使用unittest类的main方法  自动加载当前脚本中的类  并自动运行测试用例
#     # unittest.main()
#
#     ################   生成测试报告    ##############
#     # 第一步 创建一个测试套件 理解成玩具枪的弹夹
#     suite=unittest.TestSuite()
#     # 第二步 向测试套件里面添加测试用例  理解成玩具枪弹夹添加bb弹【子弹】
#     suite.addTest(T('test_1'))
#     # 第三步 将生成的测试结果写入html文件里
#     with open(r'C:\Users\Administrator\Desktop\a.html','wb') as fb:
#         runner=HTMLTestReportCN.HTMLTestRunner(
#             stream=fb,
#             title='报告',
#             description='报告描述',
#             verbosity=2,
#             # 输出内容的详细等级 默认是0，2代表最详细
#         )
#         # 执行测试用例 并声称html测试报告 理解成玩具枪发射子弹
#         runner.run(suite)

