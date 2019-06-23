# try:
#     a=123+'chaoren'
#     print(a)
# except TypeError as e:
#     print(e)
# else:
#     print(246)
# finally:
#     print('hhh')

import  xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#        sheet.write(i-1,j-1,'{}*{}={}'.format(j,i,j*i),)
#        f.save('aaa.xls')


import  xlrd
# f=xlrd.open_workbook('aaa.xls')
# b=f.nsheets
# print(b)
# sheet=f.sheets()[0]
# b=f.sheet_names()
# print(b)
#获取文件中有多少行
# b=sheet.nrows

# sheet=f.sheet_by_name('python_test')
# for i in  range(b):
#    c=sheet.row_values(i)
#    print(c)
# 获取多少列
# b=sheet.ncols

# 读取某一列的内容
#    c=sheet.col_values(i)
#    print(c)
# for i in  range(3,8):
#     for j  in range(3,i+1):
#           b=sheet.cell(i,j).value
#           print(b)
#把txt文件中的数据放入excel表中
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# d=[]
# for i in  range(5):
#      w=a[i]
#      c=w.split(',')
#      print(c)
#      d.append(c)
# print(d)
# import xlwt
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('python_test')
# for x in  range(len(d)):
#     for y in  range(4):
#         sheet.write(x,y,d[x][y])
# ff.save('aaa.xls')

#给Excel表格中追加内容
# from xlutils.copy import  copy

# #打开要追加的文件
# f=xlrd.open_workbook('aaa.xls')
#sheet1=f.sheets()[0]
#b=sheet1.nrows
# #复制文件
# new_f=copy(f)
# #获取要追加的标签页，通过索引
# sheet=new_f.get_sheet(0)
# #写入
# sheet.write(0,2,'qwe')
# new_f.save('aaa.xls')

# from xlutils.copy import  copy
# import xlrd
# f=open('b.txt','r',encoding='utf-8')
# a=f.readlines()
# d=[]
# for i in  range(3):
#      w=a[i]
#      c=w.split(',')
#      print(c)
#      d.append(c)
# sheet1=f.sheets()[0]
# b=sheet1.nrows
# c=sheet1.ncols
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for x in  range(len(d)):
#     for y in  range(3):
#         sheet.write(b,c,d[x][y])
# new_f.save('aaa.xls')


import time
# a=time.time()
# print(a)
# a=time.localtime()
# print(a)
# a=time.strptime('2011-12-33','%Y-%m-%d')
# print(a)
#年份那一年是否是闰年，那一天是星期几，那一天是一年中的第几天
# y=int(input('输入年份'))
# if ((y%4==0 and y%100!=0) or (y%400==0)):
#     print(y,'是闰年')
# else:
#     print(y,'不是闰年')
# m=int(input('输入月'))
# d=int(input('输入ri'))
# b=time.strptime('{}-{}-{}'.format(y,m,d),'%Y-%m-%d')
# print('星期',b[6])
# print('一年中的第',b[7],'天')
#求当前日期的前一天的日期
import datetime
# x=int(input('输入年'))
# y=int(input('输入月'))
# z=int(input('输入日'))
# # a=datetime.datetime(x,y,z) - datetime.timedelta(1)
# # print(a)
# a=time.strptime('{}-{}-{}'.format(x,y,z),'%Y-%m-%d')
# print(a)
# b=(time.mktime(a)-86400)
# print(b)
# c=time.localtime(b)
# print(c)
# d=time.strftime('%Y-%m-%d')
# print(d)
#将excel文件中的内容写入txt文件
# import xlrd
# f=xlrd.open_workbook(r'aaa.xls')
# sheet=f.sheet_by_name('python_test')
# b=sheet.nrows
# ff=open('a.txt','w',encoding='utf-8')
# for i in range(b):
#     c=sheet.row_values(i)
#     d=','.join(c)
#     print(c)
#     ff.write('{}'.format(d))
# ff.close()

# import time
# sentence = "!"
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)

# c=123
# f=open('b.txt','r',encoding='utf-8')
# # # a=f.read()
# # for i in f:
# #     d=f.readline()
# #     # if d[:3]==c:
# #     print(d)
# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('aaa.xls')
# sh=f.sheets()[0]
# num=sh.nrows
# nnn=sh.ncols
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in  range(10):
#     sheet.write(num+i,0,'qwe')
# new_f.save('aaa.xls')
import  pymysql
import  xlrd
# 连接数据库
# conn=pymysql.connect(host='192.168.0.211',
#                      port=3306,
#                      user='root',
#                      passwd='123456')
# # f=xlrd.open_workbook(r'aaa.xls')
# # sheet=f.sheets()[0]
# m = conn.cursor()
# m.execute('use python_sql;')
# # 从txt文件中把数据提取出来放入数据库中
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
#
# for i in range(len(a)):
#     b=a[i].split(",")
#     print(b)
#
#     if i == 0:
#        continue
#        m.execute('create table txt({} char(50),{} int,{} char(50),{} char(50));'.format(b[0],b[1],b[2],b[3]))
#     else:
#        m.execute('insert into txt values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# m.execute('select * from txt;')
# c=m.fetchall()
    # for j in range(len(a)):
#创建游标#
# #执行sql语句  数据库的个数
# #m.execute('create database python_sql;')
# m.execute('show databases;')
# m.execute('show tables;')
# # m.execute('create table biao(name char(20),age int,sex char(20))')
# # for i in range(10):
# #     m.execute('insert into biao values("小红",{},"女");'.format(i))
# #     m.execute('select * from biao;')
# #     b = m.fetchall()
# # print(b)
# b = m.fetchall()
# 默认一次只读取一个数据，
# 传入的参数是数字几就读取几天数据
# b=m.fetchmany(1)
# 每次只读取一条数据
# b=m.fetchone()
# c=m.fetchone()
# # print(b,c)
# # #断开数据库
# # conn.colse()
#从excel表中读取数据放入数据库中
# for j in b:
#     # b=sheet.row_values(i)
#
#     if j==0:
#        m.execute('create table txt({} char(50),{} int,{} char(50),{} char(50));'.format(b[0],b[1],b[2],b[3]))
#     else:
#        m.execute('insert into excel values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# m.execute('select * from txt;')
# c=m.fetchall()
# print(c)
# b = m.fetchall()
# #默认一次只读取一个数据，
# #传入的参数是数字几就读取几天数据
# b=m.fetchmany(1)
# #每次只读取一条数据
# d=m.fetchone()
# c=m.fetchone()
# a=m.execute('select * from txt;')
# a=m.execute('show tables;')
# f=open('a.txt','w',encoding='utf-8')
# m.execute('select * from txt;')
# a=m.execute('desc txt;')
# e=[]
# for j in range(4):
#     b=m.fetchone()
#     c=list(b)
#     d=[c[0]]
#     e.append(d)
#     #xx=','.join(e[0])
#     #print(xx)
# e=str(e)
# print(e)
# f.write(e)
# f.write('\n')
# m.execute('select * from txt;')
# z=m.fetchall()
# for i in  z:
#     i = str(i)
#     f.write(i)
#     f.write('\n')





# def asd(x):
#     a=0
#     for i in range(x+1):
#         a+=i
#     return a
# print(asd(123))
import  copy
# a=[12,23,21,[231,312],321,22]
# b=a.copy()
# a[2].append(222)
# print(a)



import  os
#获取当前所在的位置
# print(os.getcwd())
# #切换目录
# os.chdir(r'C:\Users\Administrator\Desktop\pycharm-dome')
# print(os.getcwd())
#执行cmd命令,只能是有结果的命令
# b=os.popen('ping 192.168.0.1')
# print(b.read())
#查看所有文件
#默认是查看当前目录下的
# print(os.listdir(r'路径'))
#创建目录
#os.mkdir('aaa')
# 删除空目录
#os.rmdir('aaa')
#创建递归目录
#os.makedirs(r'aaa\bbb\ccc')
#删除递归目录
#(?#os.removedirs(r'aaa\bbb\ccc'))
# 将文件路径与文件分隔开
# b=os.path.split(r'路径')
# 将后缀名与路径分隔开
# b=os.path.splitext(r'路径')
# 判断是否是普通文件
# b=os.path.isfile(r'路径')
# print(b)



# c=os.listdir()
# for i in  c:
#     c=str(i)
#     d=c.endswith('.py')
#     if d==True:
#         print(i)

# m.execute('create table biao(name char(20),age int,sex char(20))')
# m.execute('create table user(id int,name char(20));')

# b=m.execute('select * from txt;')
import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python_test')
# a=m.execute('desc txt;')
# e=[]
# for j in range(a):
#         b=m.fetchone()
#         d=(b[0])
#         e.append(d)
#         sheet.write(0,j,'{}'.format(e[j]))
#         f.save('aaa.xls')

#封装了ssh协议，可以实现远程控制
import paramiko
# with paramiko.SSHClient() as ssh123:
#     #创建一个ssh客户端
#     ssh123=paramiko.SSHClient()
#     #跳过从know_host文件中验证
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     #连接主机
#     ssh123.connect(hostname='192.168.0.211',
#                    port=22,
#                    username='root',
#                    password='123456')
    #执行命令

    # while True:
    #     x=input('sss')
    #     a,b,c=ssh123.exec_command('ls -al /home')
    # #第一个变量；输入的命令
    # #第二个变量：命令输出的结果
    # #第三个变量；命令的报错
    # #.decode()解码
    #     print(b.read().decode())
    # #断开连接
    # # ssh123.close()
    #     if x==exit:
    #         break
    #     ssh123.close

# import paramiko
# #建一个传输通道
# qq=paramiko.Transport(('192.168.0.211',22))
# #连接主机
# qq.connect(username='root',password='123456')
# #使用ssh协议创建一个传输文件的功能
# sftp=paramiko.SFTPClient.from_transport(qq)
# #下载文件，从linux上传文件到windows
# sftp.get(r'/home/a.sh',r'aa.sh')
# #上传文件，从windos上传文件到linux
# sftp.put('day1.py','/etc/day1.py')
# #断开连接
# qq.close()




#发送邮件 smtp



import  smtplib #封装了smtp协议
import  email.mime.multipart as mul #制作邮件
import  email.mime.text as text #对邮件的正文进行处理
#ff='15660513120@163.com'
#ww='316986133@qq.com'
#创建一个空邮件
# message=mul.MIMEMultipart()
# #标题
# message['Subject']='pythone_test'
# #发件人
# message['From']='15660513120@163.com'
# #收件人
# message['To']='316986133@qq.com'
# #正文  多行数据
# txt="""
# 刘旭先生 恭喜你 获得了s10世界赛冠军  希望您于十日内交2w元钱到拳头公司   我将为您把您的冠军奖杯邮寄过去
# 并为您制作s10冠军皮肤
# """
# #对正文进行处理
# tet = text.MIMEText(txt)
# #将处理过后的正文添加到邮件里
# message.attach(tet)
# #定义一个邮件服务器
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# #带有附件的邮件
# att1 = text.MIMEText(open('ddd.jpg', 'rb').read(), 'base64', 'utf-8')
# #附件的字段 固定的
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="冠军杯"'
# message.attach(att1)
#
# #登陆服务器  用户名 密码   不是你的邮箱密码是授权码
# smtp123.login('15660513120@163.com','A123456')
# #发送邮件   发件人  收件人  邮件
# smtp123.sendmail('15660513120@163.com','316986133@qq.com',message.as_string())
# #断开连接
# smtp123.close()



# socket
# 套接字，提供了通信双方最底层的功能（发送，接受）
# c/s架构，通过socket实现基本的通信
#server端




import socket
# 创建一个套接字（具有发送和接收能力）
# SOCK_STREAM 指使用的是tcp的协议
#AF_INET 指的是ipv4
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip和端口号
# s.bind(('192.168.0.81',3000))
# #监听
# s.listen(3)  #当达到处理极限时最大的等待个数
# while True:
#     # 接受客户端建立的连接
#     # 接受的是建立连接
#     # 第一个变量的结果：建立连接的信息
#     # 第二个变量的结果：客户端的ip和端口号
#    j


#udp服务器
import socket
# 创建一个套接字
# iPv4  SOCK_DGRAM udp
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # 绑定ip地址
# s.bind(('192.168.0.81',3000))   #接收的是元组的类型
# while True:
#     # 接收客户端的请求
#     #第一个变量：客户端的请求数据
#     #第二个变量：是客户端的ip和端口号
#     client,addr=s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     #发送响应
#     msg=input('<<<')
#     s.sendto(msg.encode('utf-8'),addr)



# 正则表达式
# 匹配文件中的字符串
# 自己写的正则表达式对于python来说python是不认识的
# 需要将正则表达式转换成python能够识别的正则表式
# 贪婪模式：尽可能多的去匹配符合条件的内容
# 非贪婪模式：尽可能少的去匹配符合条件的内容（？）
import re
#将字符串转换成正则表达式
# f=open('b.txt','r',encoding='utf-8')
# ff=f.read()
#a='wqqw123weq11123wssss123wwww11'
# compile将自己写的正则表达式编译成python能够识别的正则语言
# b=re.compile('[0-9]+') 匹配字符串中的数字
# b=re.compile('[^0-9]+')  匹配字符串中的数字外的其他
# . 匹配任意一个字符 除了换行符之外的  加上拥有匹配换行符在内的功能 re.S
# re.I让正则表达式不区分大小写
# a='sdas231dsdadsa，,21231wwqeq，weqs1231asda'
# b=re.compile('sda(.*?)da',re.S) #小括号只查看中间的字符
# c=b.findall(a)
# print(c)
# findall拿着编译之后的正则到字符串中去查找
# 是查找所有符号条件的字符   结果是一个列表
# findall 除了查找 本身就具有编译的能力
# c=b.findall(a)
#c=re.findall('sda.*da',a) 替换
#将字符串中的某些字符替换为其他的
# for i in a:
#     #第一个参数：通过正则过滤出被替换的字符
#     #第二个参数：替换成的字符
#     #第三个参数：要被替换的字符
#     c=re.sub('[0-9]+','abc',i)
#     print(c)



import  os
#重命名
# os.rename(r'aaa.xls',r'bbb.xls')

# python的函数
# print(hex(123)) # 10进制转16进制
# print(oct(234)) #10进制8进制
# print(bin(173))  #10进制转2进制
# print(int(173))  #任何进制 转换成10进制

# chr将数字转化成ascill表中对应的字符
# a=[chr(i) for i in  range(97,103)]
# print(a)
# print(chr(45))

# ord将asill表中的字符转换成对应的数字
#print(ord('a'))

# a=[123,2,3,2313]
# print(max(a))
# print(min(a))
# print(sum(a))

# #整除求余
# a,b=divmod(11222,16)
# print(a,b)



import day3
# 面向对象 优点 ：可扩展 易维护  可重复使用
# 将函数进行分类和封装，使开发更高效
# 面向过程 优点：性能好
#  通过代码和逻辑一步一步实现要达到的目的
# 100函数
# 便于查找 便于管理
from  day3 import  *
# 1 定义一个类 class 类名：
#    属性 方法(函数)
#   将同一类函数放在一起
#   默认首字母大写
#    调用  类名().函数名()
# 2 类的实例(对象)
# # 将类名()赋值给了一个对象
# sh叫类的实例（对象）(是方便在类的外部调用函数)
#  self不是函数的参数
#  self 是类的实例  方面在类的内部方便调用其他的函数
#  self=Shuxue()
# 3 继承
# 括号中是要哦立即类继承会的类中得所有函数、
# 新的类会记继承酒类中的所有函数
# 多继承
# 一个继承可以继承多个类
# 4 多态  方法重写
# 继承的类中的某个函数不满足需求  本类中自定义一个跟继承的类中函数名相同的函数
# 5 私有方法(函数)
#    不可被继承的 不能在类的外部调用的
#     只能在内部被调用
#    在函数名左边加俩个下划线
# 6 类的专有方法
#     函数名左右有两个下划线的
#     专有方法是python内部固定的
#   只要是各类，具有所有的专有方法
#     专有方法是不需要调用 会自动执行的
#   属性：一个类中所有的函数都具有的特点
#   _init_(self)#初始化属性
# class Shuxue():
#     def  paixu(self):
#          a=[1232,421,4512,52131,5211]
#          b=sorted(a)
#          b.reverse()
#          print(b )
#     def  __zdlw(self):
#          a=[10,23,452,52,888,231,21,52,666]
#          a.sort()
#          print(a[-2::])
#          self
    # def  a=int(a(self))
    #      a=[1,2,3,4,5,6,7,8,9]
    #      a.append('3')
    #      a.sort()
    #      print(a)

# sh=Shuxue()
# sh.zdlw()


# class liux():
#      def __init__(self,name,nianling):
#          self.name=name
#          self.nianling=nianling
#      def wunianhou(self,x,y):
#          self.nianling+=5
#          print('{},{}岁,{}岁结婚,{}岁生了个小孩'.format(self.name,self.nianling,x,y))
#      def wunianhouguale(self):
#          self.nianling+=5
#          print('{}'.format(self.name, self.nianling))
# q=liux('xx',3)
# q.wunianhou(10,12)
# q.wunianhouguale()
