# web自动化
# selenium：自动化测试工具集
# selenium 1.0的组成
# 1：selenium IDE 是火狐浏览器的一个插件 主要作用：录制和回放
# 2：selenium Grid 是自动化测试的一个辅助工具 作用：可以实现在不同的环境中同时执行测试
# 3：selenium Rc selenium1.0是自动化测试的核心  作用:控制浏览器的行为

# selenium2.0的组成
# selenium1.0（selenium IDE/selenium Grid/selenium Rc）+ 4：webdriver
# webdriver selenium2.0的核心 作用：控制浏览器的行为

# selenium3.0的组成
# selenium1.0（selenium IDE/selenium Grid/selenium Rc）+ 4：webdriver

# Rc：通过将测试代码转换成javascript能够识别的动作 从而间接地去控制浏览器
# webdriver：通过将浏览器的所有的原生接口集成到webdriver驱动中 然后通过驱动直接控制浏览器
# webdriver.exe


# 任何浏览器管理窗口的原理
# 将每个窗口用一个特定的字符来标识
# 只需要获取到每个窗口的标识号 通过来切换标识号 就能达到切换窗口的目的




from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# dr=webdriver.Chrome()
# # 自动登录qq
# sleep(5)
# dr.get('https://qzone.qq.com')
# sleep(2)
# # iframe 内嵌框架（窗口）
# # switch_to.frame 切换到某个框架上  通过id，name的值切换
# dr.switch_to.frame('login_frame')
# 回退到最初的页面上
# dr.switch_to_default_content()
# 回退到上一个框架中
# dr.switch_to.parent_frame()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('316986137')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('qwer1234')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.switch_to.frame('tcaptcha_iframe')
# sleep(2)
# wd=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# sleep(2)
# drag_and_drop 两个参数（从起始位置，到结束位置）
# drag_and_drop_by_offset三个参数(起始位置，x轴坐标，y轴坐标)
# perform 立即执行
# ActionChains(dr).drag_and_drop_by_offset(wd,190,0).perform()





# 定位一组对象
# ww= dr.find_elements_by_class_name('mn')
# 层级定位  先定位一个大的区域  再从大的区域中定位
# 先定位父元素 再定位子元素 定位的父元素必须是唯一的  子元素可以是定位一组 也可以是单独定位一个
# ww=dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
# 模拟鼠标移动
# ww=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# print(len(ww))
#enumerate：下标与字符串对应
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
#     i.click()
#     sleep(2)
#     # b = i.get_attribute('text') # 获取某个属性的值
#     # print(b)


# 任何浏览器管理窗口的原理
# 将每个窗口用一个特定的字符来标识(专业术语：句柄)
# 只需要获取到每个窗口的标识号 通过来切换标识号 就能达到切换窗口的目的
from selenium import webdriver
from time import sleep
# 导入模块智能等待
# import selenium.webdriver.support.ui as  ui
# dr=webdriver.Chrome()
# dr.get('https://www.baidu.com')
# # sleep(2) # 强制休息
# # 智能等待  10是最大等待时间
# # 创建一个智能等待器
# unitl=ui.WebDriverWait(dr,10)
# # 如果定位的元素出现了就不必再等待
# unitl.until(lambda dr:dr.find_element_by_link_text('hao123').is_displayed())
#
# dr.find_element_by_link_text('新闻').click()
# # 检测hao123这个文本内容是否出现
# 如果出现了执行下面的代码
# 如果一直米有出现就一直等待 最大等待10秒



# # 处理弹出框
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# # 切换到弹出框上去
# ww=dr.switch_to_alert()
# # 获取弹出框上面的文本
# print(ww.text)
# # 点击确定
# ww.accept()
# # 点击取消
# ww.dismiss()
# # 向弹出框输入数据
# ww.send_keys('qwerwewqeqeq')

# js='var q=document.documentElement.scrollTop=5000'
# dr.execute_script(js)

# 获取当前窗口的标识
# print(dr.current_window_handle)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# # 获取所有窗口的标识
# aa=dr.window_handles
# # 切换窗口
# dr.switch_to.window(aa[-1])
# print(dr.title)
# sleep(2)
# dr.switch_to.window(aa[0])
# print(dr.title)

class fx():
    def web(self):
        self.dr=webdriver.Firefox()
        self.dr.get('https://www.fxiaoke.com')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="cssmenu"]/div[5]/a[1]').click()
        sleep(2)
        self.aa=self.dr.window_handles
        sleep(2)
        self.dr.switch_to.window(self.aa[-1])
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/ul/li[2]').click()
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[8]/span[2]').click()
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/input').send_keys('fktest183')
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys('13014623984')
        sleep(2)
        self.dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/input').send_keys('1234qwer')
        sleep(4)
        self.dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[5]').click()

if __name__=='__main__':
    fx().web()