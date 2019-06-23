import unittest
from web自动化.config import fxxk
from web自动化.config.fxxk import fx


class FX_xk(unittest.TestCase):
    aa=fxxk.fx().web()
    print(aa)
    def test_1(self):
        self.aa = fxxk.fx().web()
        self.assertEqual(self.aa,'我的工作台',msg='登陆成功')

if __name__=='__main__':
    unittest.main()






if __name__=='__main__':
     unittest.main()