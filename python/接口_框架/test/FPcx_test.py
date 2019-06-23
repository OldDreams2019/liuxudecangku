import unittest
from 接口_框架.config import FPcx
from 接口_框架.data import FP_duqu


class FP_cx(unittest.TestCase):
    ss = FP_duqu.du_qu()
    print(ss[1][0])
    def test_1(self):
            self.aaa = FPcx.FPcx().cha_xun(self.ss[1][0])
            self.assertEqual(self.aaa['errMsg'],'处理成功', msg='成功')

if __name__=='__main__':
     unittest.main()
     # FPcx