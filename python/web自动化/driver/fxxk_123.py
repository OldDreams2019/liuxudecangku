from web自动化.report.FXxk_baogao import bao_gao
with open('a.txt','r') as f:
    a=f.readlines()
    if 'fxxk' in a:
        bao_gao('*')
    else:
        bao_gao(a)