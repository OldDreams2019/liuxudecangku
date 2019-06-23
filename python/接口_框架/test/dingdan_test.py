from 接口_框架.config import dingdan1
from 接口_框架.data import dingdan_duqu
import unittest


# 出现Launching unittests with arguments python -m unittest 提示语的原因 是pycharm本身自带一个unittest模块



class ding_dan(unittest.TestCase):
    ss = dingdan_duqu.shuju()
    def test_1(self):
        aaa = dingdan1.dingdan().cha_mixi(int(self.ss[1][0]))
        self.assertEqual(aaa["errMsg"],'null',msg='成功处理')
    # def test_2(self):
    #     bbb = dingdan1.dingdan().cha_mixi(int(self.ss[2][0]))
    #     self.assertEqual(bbb[])

if  __name__=='__main___':
     unittest.main()

#
# 将所有的以test开头的函数当成测试用例