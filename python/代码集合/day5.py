# !/usr/bin/python #定义一个解释器
# -*- coding:utf-8 -*- #定义编码方式

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#         if i==j:
#             break
#     print('')
# a='123'
# b=a[::-1]
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==b[i]:
#             c+=j*10**i
# print(c)
# import os
# os.mkdir('bbb')
# f=open('z.txt','w',encoding='utf-8')
# for i in range(10):
#     f.write('qwwe\n/23')

# import pymysql
# import xlwt
# import xlrd
# conn=pymysql.connect(host='192.168.0.211',
#                      port=3306,
#                      user='root',
#                      passwd='123456')
# m=conn.cursor()
# m.execute('use python_sql;')
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# for i in range(len(a)):
#     b=a[i].split(",")
#     print(b)
#     if i == 0:
#        continue
#        m.execute('create table txt({} char(50),{} int,{} char(50),{} char(50));'.format(b[0],b[1],b[2],b[3]))
#     else:
#        m.execute('insert into txt values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# m.execute('select * from txt;')



# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.74',3000))
# s.listen(3)
# while True:
#     client, addr = s.accept()
#     reg=client.recv(1024)
#     print(reg.decode('utf-8'))
#     msg=input('')
#     client.send(msg.encode('utf-8'))


# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
#
# message = mul.MIMEMultipart()
# message['Subject'] = 'python_test'
# message['From'] = '15660513120@163.com'
# message['To'] = '825069672@qq.com'
# txt = """
#     你好你好
#
#
# """
# tet = text.MIMEText(txt)
# message.attach(tet)
# smtp123 = smtplib.SMTP_SSL('smtp.163.com', 465)
# att1 = text.MIMEText(open('ddd.jpg', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="ddd.jpg"'
# message.attach(att1)
#
# smtp123.login('15660513120@163.com', 'A123456')
# smtp123.sendmail('15660513120@163.com', '825069672@qq.com', message.as_string())
# smtp123.close()

import re
import requests
import json
import xlrd
import xlwt
import pymysql
# conn=pymysql.connect(host='192.168.0.211',
#                      port=3306,
#                      user='root',
#                      passwd='123456')
# m=conn.cursor()
# m.execute('use python_sql;')
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python_test')
# f=open('aa.txt','w',encoding='utf-8')
# url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.54063434&x-zp-page-request-id=7efb19850c67462586b7e407111c156d-1557228416151-771519'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;    WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# res=requests.get(url,headers=head)
# html=res.content.decode('utf-8')
# aa=json.loads(html)
# c=[]
# d=['工作名称','公司名称','工资','地址']
# for z in range(len(d)):
#     sheet.write(0,z,d[z])
#     if z == 0:
#         m.execute('create table AAA({} char(50),{} char(50),{} char(200),{} char(50));'.format(d[0], d[1], d[2], d[3]))
# for i in range(20):
#         a1=[]
#         b1=aa['data']['results'][i]['jobName']
#         b2=aa['data']['results'][i]['company']['name']
#         b3=aa['data']['results'][i]['salary']
#         b4=aa['data']['results'][i]['city']['display']
#         a1.append(b1)
#         a1.append(b2)
#         a1.append(b3)
#         a1.append(b4)
#         # print(a1[2])
#         # if i == 0:
#         #    continue
#         #    m.execute('create table AAA({} char(50),{} char(50),{} char(200),{} char(50));'.format(d[0],d[1],d[2],d[3]))
#         if i>0 :
#            m.execute('insert into AAA values("{}","{}","{}","{}")'.format(a1[0],a1[1],a1[2],a1[3]))
#            m.execute('select * from AAA;')



#         for t in range(len(d)):
#             sheet.write(i+1,t,'{}'.format(a1[t]))
#             if i+1==20:
#                 break
# f.save('bbb.xls')




    # f.write('{}.{}.{}.{}'.format(b1,b2,b3,b4))
    # f.write('\n')
#a=0
# for i in items:
#     j='http://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     msg=requests.get(j,headers=head)
#     hh =msg.content
#     with open('{}.jpg'.format(a),'wb') as f:
#         f.write(hh)
#     a+=1
#
#
#
# import re
# import requests
# class freeBuf_():
#     def send_请求(self,):
#         url='https://sou.zhaopin.com/?jl=538&kw=软件测试工程师'
#         # 伪装
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
#         #发送请求
#         res=requests.get(url,headers=head)
#         #读取结果  1.text以文本的方式接收，结果是字符串
#         #          2.content 以字节的方式接收，结果是字节
#         hh=res.content.decode('utf-8')
#         return (hh)
#     def guolv(self,x):
#         for i in range(90)
#
#         title=[]
#         patt=re
#
#         .compile('<div class="news-img">(.*?)<dd>',re.S)
#         itesms=patt.findall(x)
#         for i in itesms:
#             aa=re.findall('title="(.*?)"',i)
#             title.append(aa[0])
#         print(title)
#         return title
#     def save(self,y):
#         with open('c.txt','a',encoding='utf-8') as f:
#             for i in y:
#                 f.write(i+'\n')


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j ),end='\t')
#         if j==i:
#             break
#     print('')

# sum=0
# a=int(input())
# for i in range(2,a):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         sum=sum+1
# print(sum)
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#         if i==j:
#             break
#     print('')

import requests
import re
# url='http://baijiahao.baidu.com/s?id=1600536056863584317&wfr=spider&for=pc'
# # head=''
# res=requests.get(url)
# hh=res.content.decode('utf-8')
# patt=re.compile(r'src="http://t10.baidu.com/it/u=(.*?)1&amp;fm=173&amp;app=25&amp;f=JPEG?w=639&amp;h=399&amp;s=39946191D042D6F412A4D503030060C9"')
# a=patt.findall(hh)
# #b=patt2.findall(hh)
# print(a)
# for i in itesms:
# fm=173&amp;app=25&amp;f=JP EG?w=(.*?)&amp;h=(.*?)&amp;s=(.*?)"





from selenium import webdriver
from time import sleep
#打开浏览器
# dr=webdriver.Chrome()
#请求要打开的网页
# dr.get('https://www.baidu.com')
# sleep(2)
#打印打开的网页的标题
# if dr.title=='百度一下,你就知道':
#     print(yes)
#打印网页的网址
# print(dr.current_url)
# sleep(2)
#设置浏览器窗口的大小
# dr.set_window_size(400,400)
# #设置浏览器的位置
# dr.set_window_position(400,400)
#z最大化浏览器
# dr.maximize_window()
# #最小化浏览器
# dr.minimize_window()
# dr.get('https://www.jd.com')
# sleep(2)
# #回退
# dr.back()
# #前进
# sleep(2)
# dr.forward()
#最重要：定位   动作   send_keys输入  click点击
# 1.通过id定位
# 2.通过name属性
# 3.class属性定位
# 4.link_text定位  根据文本定位
# dr.find_element_by_link_text('新闻').click()   #(clic是点击确认的)
# 5.partial link text 根据模糊文本定位
# 6.tage_name根据标签的名称定位
# 7.xpath   根据路径定位
#   xpath 路径标记语言
# dr.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
# 8 css_selector  根据css定位
# dr.find_element_by_css_selector('#u1 > a:nth-child(5)').click()
# 不论采用任何方式的定位  一定要保证定位的唯一性
# dr.find_element_by_class_name_('s_').send_keys('python')
# sleep(2)

dr=webdriver.Chrome()
dr.get('https://qzone.qq.com/')
sleep(2)
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_xpath('//*[@id="img_out_316986133"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="composebtn"]').click()
sleep(2)
dr.find_element_by_class_name('fui-icon icon-op-praise').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[1]').send_keys('316986133')
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('3366420860')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('qwer1234')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# dr.find_element_by_xpath('//*[@id="composebtn"]').click()
# sleep(2)
# dr.find_element_by_css_selector('#toAreaCtrl').send_keys('1056868079@qq.com')
# dr.find_element_by_xpath('//*[@id="lm1558687660644019976747404445172tree"]/div[2]/div[2]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="to_btn"]').send_keys('1056868079@qq.com')
# dr.find_element_by_xpath('//*[@id="lm1558689432256004856542240978623tree"]/div[2]/div[2]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="subject"]').send_keys('小可爱')
# sleep(2)
# dr.find_element_by_xpath('/html/body').send_keys('hello,小可爱')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()



# dr=webdriver.Chrome()
# dr.get('https://mail.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath()


# import unittest
# # unittest 写单元测试用的，写断言用的。
# # 拿预期结果和实际结果做对比的过程
# class demo(unittest.TestCase):
#     def test_1(self):
#         #假设预期结果是1
#         #实际结果是2
#         #判断预期结果是否等于实际结果
#          a=1 #预期结果
#         # 断言：
#          self.assertEqual(a,2)
# if __name__=='__main__':
#     unittest.main()
# def a(x):
#     num=0
#     for i in range(x+1):
#         num+=i
#     return num
# print(a(100))



# import requests
# import re
#
# url='https://www.phb123.com/renwu/meinv/27189.html'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res=requests.get(url,headers=head)
# html=res.content.decode('utf-8')
# patt=re.compile(r'src="https://img.phb123.com/uploads/allimg/(.*?).jpg" />')
# a=patt.findall(html)
# b=0
# for i in a:
#     j='https://img.phb123.com/uploads/allimg/{}.jpg" />'.format(i)
#     print(j)
#     msg=requests.get(j)
#     hh=msg.content
#     f=open(r'{}.jpg'.format(b),'wb')
#     f.write(hh)
#     b=b+1


# import requests
# import re
# import os
# url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=测试工程师&kt=3&=0&_v=0.49296401&x-zp-page-request-id=7f9d3783f7d04a7cb118e10ffe39500c-1560168947158-901662&x-zp-client-id=2eb12edc-e346-4255-9c7a-9a3cc6c4e439'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res=requests.get(url,headers=head)
# html=res.content.decode('utf-8')
# patt=re.compile(r'img src="//pic.qiushibaike.com/system/(.*?).jpg"')
# a=patt.findall(html)
# b=0
# for i in a:
#     j='https://img src="//pic.qiushibaike.com/system/{}.jpg".jpg'.format(i)
#     msg=requests.get(j)
#     hh=msg.content
#     f=open('{}.jpg'.format(b),'wb')
#     f.write(hh)
#     b=b+1

# for i in range(18):
#     os.remove('{}.jpg'.format(i))
