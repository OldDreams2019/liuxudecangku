import HTMLTestReportCN
import unittest

def bao_gao(name):
    suite = unittest.TestSuite()
    for i in name:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\Administrator\Desktop\pycharm-dome\web自动化\test',pattern='fxxk_test.py')
        for j in dis:
            suite.addTest(j)
    f = open(r'C:\Users\Administrator\Desktop\pycharm-dome\web自动化\report\c.html', 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
                stream=f,
                title='报告',
                description='报告描述',
                verbosity=2,
            )
    runner.run(suite)
if __name__=="__main__":
    bao_gao('*')


