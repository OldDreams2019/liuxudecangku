from 接口_框架.reprot.FPcx_Bgao import bao_gao
with open('a.txt','r') as f:
    a=f.readlines()
    if 'FPcx' in a:
        bao_gao('*')
    else:
        bao_gao(a)