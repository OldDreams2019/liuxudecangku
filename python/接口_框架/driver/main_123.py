# driver中主要控制跑回归测试时只跑那些模块的
from 接口_框架.reprot.baogao import bao_gao
with open('a.txt','r') as f:
    a=f.readlines()
    if 'FPcx' in a:
        bao_gao('*')
    else:
        bao_gao(a)