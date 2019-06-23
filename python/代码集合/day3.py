import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python_test')
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# c=[]
# for i in a:
#         b=i.split(',')
#         c=['{},{},{},{}'.format(b[0],b[1],b[2],b[3]) ]
#         print(c)
#         # sheet.write()
# for x in range(len(a)):
#     for y in range(len(a)):



import smtplib
import email.mime.multipart as mul
import email.mime.text as text
# message=mul.MIMEMultipart()
# message['subject']='python_test'
# message['From']='15660513120@163.com'
# message['To']='316986133@qq.com'
# txt=""""sssss"""
# tet=text.MIMEText(txt)
# message.attach(tet)
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# att1=text.MIMEText(open('ddd.jpg','rb').read(),'base64','utf-8')
# att1['content-Type']='attachment/octet-stream'
# att1["content-Disposition"]='attachment;filename="奖杯"'
# message.attach(att1)
# smtp123.login('15660513120@163.com','A123456')
# smtp123.sendmail('15660513120@163.com','316986133@qq.com',message.as_string())
# smtp123.close

#
# def asd(i):
#      a=0
#      i=1
#      while  i<101:
#             a=a+i
#             i+=1
#      print(a)
#      return i
# asd(200)

# def asd(b):
#     a=0
#     for i in range(1,b+1):
#         a+=i
#         return a
# asd(100)

import xlrd
import  re
# a='vasv3q5jbj5b23j1233bkj2b675sda2323242dsdg2313we2222222323sdsa'
# b=re.compile('[0-9][0-9]+')
# c=b.findall(a)
# print(c)
# print(len(c))



# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# print(a)
# for i in a:



# 爬虫：模仿浏览器，根据自己指定的规则去批量下载指定的资源
# 分类：聚焦爬虫，搜索爬虫，
# 聚焦爬虫：只针对某个网站进行爬取
# 搜索爬虫：针对全网络进行爬取(搜索引擎)
# 模仿浏览器的模块：request，urllib，urllib2,3,  scrapy
# 过滤网页资源：正则表达式(re)，Beautifulsoup,xpath
# 爬虫第一步：分析网址
# 爬虫第二步：找到想要的资源并过滤
# 爬虫第三步：保存
# 对服务器进行请求 将得到的响应数据过滤并保存
# 对服务器造成太大的压力
# 开发人员：反爬：防止反爬程序 批量下载资源
# 常见的反爬机制
#     1 通过headers判断
#     2 ip地址被封  频繁的更换公网ip（西刺代理）
#     3 验证码
#     4 数据混淆
#     5 行为分析
#  爬虫本身不违法，做商业活动就违法了
#  当我的成本和你的付出是一样时  不阻止你爬


import requests
import re

# class freeBuf_():
#     def send_请求(self,):
#         url='https://www.freebuf.com/clipped?pg=1'
#         # 伪装
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
#         #发送请求
#         res=requests.get(url,headers=head)
#         #读取结果  1.text以文本的方式接收，结果是字符串
#         #          2.content 以字节的方式接收，结果是字节
#         hh=res.content.decode('utf-8')
#         return (hh)
#     def guolv(self,x):
#         title=[]
#         patt=re.compile('<div class="news-img">(.*?)<dd>',re.S)
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
# fr=freeBuf_()
# hh=fr.send_请求()
# y=fr.guolv(hh)
# fr.save(y)



# url='https://www.maigoo.com/top/390242.html'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# res=requests.get(url,headers=head)
# html=res.content.decode('utf-8')
# patt=re.compile(r'<img src="https://image3.cnpp.cn/upload/images/(.*?).jpg" />')
# items=patt.findall(html)
# a=0
# for i in items:
#     j=r"https://image3.cnpp.cn/upload/images/{}.jpg".format(i)
#     print(j)
#     # #保存图片 先对图片链接请求 以字节的方式保存
#     msg=requests.get(j,headers=head)
#     hh =msg.content
#     with open(r'E:\表情包/{}.jpg'.format(a),'wb') as f:
#         f.write(hh)
#         a=a+1

# f.save(r'C:\Users\Administrator\Desktop')

#
# url='https://www.maigoo.com/top/383592.html'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# res=requests.get(url,headers=head)
# html=res.content.decode('utf-8')
# patt=re.compile(r'<img src="https://image3.cnpp.cn/upload/images/(.*?).jpg" />')
# items = patt.findall(html)
# print(items)
# a=0
# for i in items:
#     j='http://image3.cnpp.cn/upload/images/{}.jpg" />'.format(i)
#     print(j)
#     #保存图片 先对图片链接请求 以字节的方式保存
#     msg=requests.get(j,headers=head)
#     hh =msg.content
#     with open('{}.png'.format(a),'wb') as f:
#         f.write(hh)
#     a+=1




# url='http://movie.douban.com/top250'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.get(url,headers=head)
# p=res.content.decode('utf-8')
# # print(p)
# #过滤
# patt=re.compile(r'<img width="100" alt="(.*?)" src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">')
# c=patt.findall(p)
# print(c)
# a=0
# for i in c:
#     b=i[1]
#     j='https://src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/'+ i[2] + '.jpg"'
#     print(j)


#
#
# url='http://movie.douban.com/top250'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.get(url,headers=head)
# p=res.content.decode('utf-8')
# patt=re.compile(r'<img width="100" alt="(.*?)" src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">')
# c=patt.findall(p)
# print(c)
# # a=0
# # for i in c:
# #     j='https://src="https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg"'.format(i[1],i[2])
# #     print(j)
# #     msg = requests.post(j,headers=head)
#     hh = msg.content
#     with open('{}.jpg'.format(i[0]),'wb') as f:
#         f.write(hh)
#     a=a+1



# 网页：静态网页：所有的资源都在html文件上
#      动态网页：资源不在html文件上
# ajax        JavaScript(js)
#  json：是一种轻量级的数据传输格式
#
#
# import json
# import requests
# url=''
# res=requests.get(url)
# hhh=res.content.decode('utf-8')
# #将字符串格式转化为字典
# qqq=json.loads(hhh)
# print(qqq.['data']['results'][1]['company']['name'])
# #将字典转换为字符串
# uuu=json.dumps(qqq)
# print(uuu)
#
# a=[12,32,123]#连接
# b=['a','b','c']
# aaa=zip(a,b)#将多个列表一一对应



# import  socket
# while True:
#    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    sock.connect(('192.168.0.74',3000))
#    qq=input('<<<')
#    sock.send(qq.encode('utf-8'))
#    ww=sock.recv(1024)
#    print(ww.decode('utf-8'))
5