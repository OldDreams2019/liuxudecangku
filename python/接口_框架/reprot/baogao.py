import HTMLTestReportCN
import unittest

def bao_gao(name):
    #创建一个测试套件
    suite = unittest.TestSuite()
    #将测试用例添加到测试套件
    #将某一个类中所有的测试用例添加到测试套件中
    # suite.addTest(unittest.makeSuite())
    #第一个参数：存放测试脚本的路径
    #第二个参数：匹配测试文件的通配符
    # 自动去发现符合通配符的文件中以test开头的函数
    for i in name:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\Administrator\Desktop\pycharm-dome\接口_框架\test',pattern='{}_test.py'.format(i.strip()))
        for j in dis:
            suite.addTest(j)
    f= open(r'C:\Users\Administrator\Desktop\pycharm-dome\接口_框架\reprot\ac.html','wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
            stream=f,
            title='报告',
            description='报告描述',
            verbosity=2,
        )
    runner.run(suite)
    f.close()
# if __name__=='__main__':
#      bao_gao('*')