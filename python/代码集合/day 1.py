# !/usr/bin/python #定义一个解释器
#-*- coding:utf-8 -*- 定义编码方式

# 1。输出（打印） 等同于echo
#print("hello")
#a=3
#b=4
#print(4)
#a='qwewerqsd'
#print(a[2::3])
#属于字符串的函数
# 1.将所有的小写变成大写  upper（）
# 2. 2
#b=a.upper()
#print(b)
#b=a.replace('we','12',1)
#print(b)
#b=a.split('w')
#print(b)
# 4.去除左右的空格
#a='ewrq23dqwre'
#b=a.rstrip()
#print(b)
#b=a.replace(' ','')
#print(b)
#b=a.startswith('2')
#print(b)
#b=a.endswith('w')
#print(b)
#a='user{n}use{s}'
#b=a.format(n=21,s=22)
#print(b)
#a='hello%s,我今年%d岁'
#b=a%('小红',18)
#print(b)
#a='qweqwr'
#b=a.index('w')
#b=a.count('w')
#print(len(a))
#bowen=[1,4,2,3]
#bowen.append('多')

#bowen.insert(2,'大')
#bowen.remove('100')
#a=bowen
#b=sorted(a)
#print(b)
#bowen=[1,2,4,5,'大','小','多','大','小','多']
#f=bowen.count('大')
#print(f)
#a = [ 12,32,'1','asd',]
#a.append(b)
#print(a)
# a=[1,3,2,42,33]
#a.insert(0,'l') 添加指定位置
#a.remove(231) 删除
#a.pop(2)
#a[1]=11111
# a.sort()
# a.reverse()
# print(a)
#a.index(1
#a.clear()
#print(a)
# import copy
# c=[4,5,6]
# a=[12,31,c,111]
# ff=copy.deepcopy(a)
# c.append(110)
# a.append(666)
# print(ff)
#a=[12,143,4,'wer','dsf']
#print(len(a))
#a={'name':'小明','age':'20'}
#b={'sex':'男'}
#a['name']='nan'
#a.pop('age')  删除某个键对
#a.popitem()   默认删除最后一个键对
#b=a.keys()    获取所有的键
#a.update(b)
#print(a)
#a={12,13,15,'wer'}
#b={12,11,33,'aaa'}

#print(a-b)

#b=a.upper()
#a.replace('s','1')
#print(a[:4])
# i=[1,2,3,4,5,6,7,8,9]
# j=[1,2,3,4,5,6,7,8,9]
# print('%d*%d=%d'%(i,j,i*j))
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()
#a="adsdsadsad"
#a=set(a)
#b=a.split('d')
#print(b
# a=input('>>>')
# a=int(a)
# if a>4:
#     print('hello')
# elif a<4:
#     print('www')
#     #print('sss')3
# a=input('输入成绩')
# a=int(a)
# if a>90:
#     print('优秀')
# elif  90>a>80:
#     print('良好')
# elif   80>a>70:
#     print('中等')
# if a%2==0:
#     if a%3==0:
#        print('hello world')
#     else:
#        print('hello')
# if  a%2!=0:
#     if a%3==0:
#        print('world')
# else:
#     print('123')
#a = [12,14,15,'231']
# a=101
# sum=0
# for  i in  range(a) :
#     sum=sum+i
# print(sum)
# a=100
# sum=0
# for i in  range(1,100,2):
#     sum=sum+i
# num=0
# for a in  range(2,100,2):
#     num=num+a
# b=sum-num
# print(b)
#循环嵌套
# for i in  range(10):
#       if i>5:
#           print(i)
#       elif i>3:
#           print(0)
#       else:
#           print(2)
# for i in range(10):
#     # if i==7:
#     #     continue
#     if i>7:
#         break
#     print(i)
# import  random
# a=random.randrange(1,22)
# c='小了小了 还有{}次机会'
# d='大了大了 还有{}次机会'
#
# for i in range(3):
#     i = input()
#     i = int(i)
#     if i==a:
#         print('恭喜')
#         break
#     elif i>a:
#         print(c.format(3-i))
#
#     elif i<a:
#         print(d.format(3-i))
#
# else:
#     print('菜')
#九九乘法表
# for i in  range(1,10):
#     for j in  range(1,10):
#
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#         if i==j:
#             break
#     print('')
#质数之和
# sum=0
# for i in  range(2,100):
#    for j in  range(2,i):
#         if (i%j==0):
#            break
#    else:
#      sum+=i
# print(sum)
#质数之和
# sum=0
# for i in range(2,100):
#     for j in range (2,i):
#         if (i%j==0):
#             break
#     else:
#       sum=sum+i
# print(sum)
#水仙花数
# for i in range(2,1000):
#     sum=0
#     for j in  range(1,1000):
#       if j<i:
#         if i%j==0:
#           sum=sum+j
#     if i==sum:
#          print(i)

# for i in  range(1,10):
#     for j in  range(1,10):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#         if i==j:
#           break
#     print()
# sam=0
# for i in range(2,100):
#     for j in range(2,i):
#       if (i%j==0):
#        break
#     else:
#      sam=sam+i
# print(sam)
#有四个数字 1,2,3,4  能组成多少个互不相同且无重复的三位数
# for i  in  range(1,5):
#     for j in  range(1,5):
#         for a in  range(1,5):
#             if i!=j!=a:
#
#              print(i,j,a)
# sam=0
# for i in range(2,100):
#    for  j  in  range(2,i):
#         if (i%j==0):
#             break
#    else:
#             sam=sam+i
# print(sam)
# for i in range(2,1000):
#     sum=0
#     for  j   in  range(1,1000):
#         if j<i:
#           if  (i%j==0):
#             sum=sum+i
#     if i==sum:
#      print(sum)
#是否是一个字符串
# s = input('请输入一个字符串：')
# if not s:
#     print('请不要输入空字符串！')
#     s = input('请重新输入一个字符串：')
#
# a = len(s)
# i = 0
# count = 1
# while i <= (a/2):
#     if s[i] == s[a-i-1]:
#         count = 1
#         i += 1
#     else:
#         count = 0
#         break
#
# if count == 1:
#     print('您所输入的字符串是回文')
# else:
#     print('您所输入的字符串不是回文')
# 是否是一个字符串
# a= input('请输入一个字符串:')
# if a==a[::-1]:
#     print('是一个回文')
# else:
#     print('不是一个回文')
# a=3
# while a>2:
#     print('hello')
#     a
# i=1
# j=0
# while  i<101:
#     print(i)
#     j=j+i
#     i=i+1
#
#  print(j)
# while True:
#  a='-1'
#  a=input('输入学生成绩')
#  a=a.split(',')
#  a=[int(i) for i in a]
#  b=sum(a) / len(a)
#  if a[0]<0:
#  a[i] = int(j)
#  b=sum(a)//len(a)
#  print('平均数为{}'.format(b))
#  (for k in a  if  k<b   print('低于平均数的有{}'.format(k))):
#     elif k<0:
#         break
# b=[i**2]
#去重
# a = [1,4,3,3,4,2,3,4,5,6,1]
# for i in a:
#     b=a.count(i)
#     if b>1:
#         for j in range(b-1):
#             a.remove(i)
# print(a)
#去重
# a = [1,4,3,3,4,2,3,4,5,6,1]
# b = []
# for i in a :
#     if i not in b:
#        b.append(i)
# b.sort()
# print(b)
# f=open(r'c:\Users\Administrator\Desktop\a.txt','w',encoding='utf-8')
# f=open('a.txt','r',encoding='utf-8')
# for i in range(1, 10):
#     for j in  range(1,i+1):
#        f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')
# b=f.readline()
# c=f.readline()
# d=f.readline()
# print(b,c,d)
# f=open('a.txt','r',encoding='utf-8')
# for i in f:
#     a=f.readlines()
#    if b=a.startwith('abc'):
#  print(b)
#	任意4个数字，组成不相同的三位数
# for i in  range(1,5):
#     for j in  range(1,5):
#         for k in  range(1,5):
#           if  i!=j!=k:
#   print(i,j,k)
# sum=0
# a=1
# for i in range (1,4):
#     a=a*i
#     sum=sum+i
#     print(sum)
#无限循环的阶乘之和
# n = int(input())
# jie = 1
# sum = 0
# i = 1
# for i  in range():
#     if  n >= i:
#     jie = jie * i
#     sum = sum + jie
#     i = i + 1
#     print(sum)
#阶乘之和
# a = 1
# n = 6
# for i in range(1,n+1):
#     a = a * i
# print(a)
# 判断是否是个三角形
# x=int(input('输入一个数'))
# y=int(input('输入一个数'))
# z=int(input('输入一个数'))
# if  x+y>z and x+z>y and y+z>x:
#   print('这是三角形')
# else:
#     print('no')
#公鸡  母鸡 小鸡
# for x in  range(1,100):
#     for y in  range(1,100):
#         z=100-x-y
#                #  2*x+y+y/2=100:
#         if (2*x + y + z/2==100):
#          print(x,y,z)
# for x in range(1,100):
#     for y in range(1,100):
#         z = 100 -x-y
#         if (5*x+3*y+z/3==100) and z%3==0:
#             print(x,y,z)
# a=str(input('请输入一个字符串'))
# if a==a[-1]:
#     print('这是一个回文')
# else:
#     print('这不是一个回文')
#十进制转换成十六进制15.	十进制转换成十六进制
# a=input('输入一个数字')
# while :
#     a%16
#     i%
# sum=0
# for i  in range(1,10):
#     for j  in range(1,10):
#             if    i%j==0:
#                   sum=sum+i
# print(sum)
# a=input()
# f=open('abc.jpg','rb')
# b=f.read()
# ff=open('abc2.jpg','ab')
# ff.write(b)
# print(b)
# f.close()
# def a():
#     b=0
#     for i  in  range(101):
#         b+=i
#     print(b)
# a()
# len()
# 打印列表上最大的两位数
# a=[10,23,452,52,888,231,21,52,666,888]
# a.sort()
# print(a[-2::])
# a=int(a)
# a=[1,2,3,4,5,6,7,8,9]
# a.append('3')
# a.sort()
# print(a)
#
# a='123'
# c=0
# # b=a[::-1] #'321'
# for i,j in  range(len(a)):
#     for c in  range(10):
#         if str(c)==a[i]:
#             c+=j**10**(len(a)-1-i)
# print(c)
#\
# sum=0
# for i in  range(2,100):
#     for  j  in   range(2,i):
#         if   (i%j==0):
#             break
#     else:
#           sum=sum+i
# print(sum)
# #
# for i  in   range(2,1000):
#     sum=0
#     for j  in  range(1,1000):
#         if i>j:
#         if i%j==0:
#     else:
# def a(x,y):
#     #x=sum(range(x))
#     print(x,y)
#     print('hello')
# a(y=123,x=21)
# def asd(b=18):
#     a=0
#     for i in  range(b+1):
#         a+=i
#     print(a)
# asd(233)
# def zs(x,y):
#     sum=0
#     for i in range(x,y+1):
#         for j in range (2,i):
#            if (i%j==0):
#             break
#         else:
#            sum=sum+i
#     print(sum)
#     return sum
# c=zs(2,100)-111
# print(c)
# def ad(*b):
#     print(b)
# ad(11,23,421,1,'qweqerq',21)
# def asd(a,b=10,*args):
#     print(a,b,*args)
# asd(22,4444,523,1111)
# def asd(b):
#     a=0
#     for i in  range(1,b+1):
#         a+=i
#     return a
# for i in  range(10,41,10):
#     c=asd(i)+2
#     print(c)
# # print(c)
# a=int(input())
# b=int(input())
# for i in  range(1,10):
#     a+b==sum
#     print(sum)
# x = int(input("first:"))
# o = input("operator:")
# y = int(input("second:"))

# operator = {
#             '+':x+y,
#             '-':x-y,
#             '*':x*y,
#             '/':x/y,
#             }
#
# result = operator.get(o,'please input+|-|*|/')
# print(result)
# a=lambda x,y:x+y
# b=lambda x,y:x-y
# c=lambda x,y:x/y
# d=lambda x,y:x*y
# while True:
#    s=input('..')
#    elif '+'in s:
#       d=s.split('+')
#        print(b(int(d[0]),int(d[1])))
#    elif  '-' in s:
#        d = s.split('-')
#        print(a(int(d[0]), int(d[1])))
#    elif  '*'in s:
#        d = s.split('*')
#        print(c(int(d[0]), int(d[1])))
#    elif  '/' in s:
#        d = s.split('/')
#        print(d(int(d[0]), int(d[1])))
# else:


#自定义一个函数 给这个函数三个参数  第一个参数是字符串 第二个参数和第三个都是数字
# def  asd(x,y,c):
#      x=list(x)
#
#      if  y+c>len(x):
#          y+c==len(x)
#      for i  in  range(y,y+c):
#          x.pop(y)
#      x=str(x)
#      b=''.join(x)
#      print(b)
# asd('123141675',3,5)
# a=[2,3,5,6,1]
# for i in range(a):##左移
#     A.insert(len(a),A[0])
#     A.remove(A[0])
#	将列表中的元素向左挪一wei
# a=[1,2,3,4,5,6]
# b=(a[0])
# a.remove(a[0])
# a.append(b)
# prin t(a)
#将列表中最大的放到最后一位 最小的放在第一位
# a=[1232,421,4512,52131,5211]
# b=sorted(a)
# b.reverse()
# print(b )
#十进制转十六进制
# a=1000
# ff=[str(i) for i in range(10)]+['a','b','c','d','e','f']
# #print(ff)
# c=''
# while True:
#     b=a%16
#     c=c+ff[b]
#     a=a//16
#      if a==0:
#         break
# print(c[::-1])
#



# def bubbleSort(nums):
#     for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
#         for j in range(len(nums)-i-1):  # ｊ为列表下标
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#         print(nums)
#     return nums
#
# nums = [5,2,45,6,8,2,1]





# c={}
# x=('goods[0:4]')
# qian=int(input('输入资产'))
# jiage={'0:1999,1:10,2:20,3:998'}
# goods=[
#     {'name':'电脑','price':1999},
#     {'name':'鼠标','price':10},
#     {'name':'游艇','price':20},
#     {'name':'美女','price':998},
# ]
# print('0：电脑,1：鼠标,2：游艇,3：美女')
# #qian.goods=int(input('请输入序列号'))
# for i in  goods:
#   print(i['name'],i['price'])
#   # qian=int(input('输入资产'))
#
# while True:
#     a=input('请输入商品名''按y结算')
#     #a=(goods[0:4],'请输入商品号,按y结算')
#     c={a}
#     print(c,'加入购物车')
#
#     if  a=='y' or a=='Y':
#          break
#
# # sum=0
# while True :
#         for j in goods:
#             asd=j['price']
#         if  asd < qian:
#             # sum=qian-jiage
#             print('购买成功')
#             break
#         else:
#             print('余额不足,购买失败,请充值')
#             chongzhi = eval(input('您的余额不足！请充值：'))
#             qian=chongzhi+qian
#             print('充值成功')
#             if asd < qian:
#                 print('购买成功')
#                 break


# num=eval(input('请输入金额：'))#只能输入数字
# goods=[
#        {'name':"电脑",'price':1999},
#        {'name':"鼠标",'price':10},
#        {'name':"游艇",'price':20},
#        {'name':"美女",'price':998},
#        ]
# print('请输入要购买的商品：')
# print('0：电脑\n1：鼠标\n2：游艇\n3：美女')
# num_goods=eval(input('请输入序号：'))#只能输入多个，输入多个时中间用逗号隔开
# sum=0
# if isinstance(num_goods,int):
#     sum+=goods[num_goods]['price']
# else:
#     for i in range(len(num_goods)):
#         if num_goods[i]>4:
#             print('请输入0~3中的数字，该商品无效，已删除')
#         else:
#             sum+=goods[num_goods[i]]['price']
#
# if num>sum:
#     flag=input('确认购物吗？，请输入y or n：')
#     if flag =='y':
#         remained=num-sum
#         print('购物成功！剩余金钱为:',remained)
#     else:
#         print('请继续购物或删除商品！')
# else:
#     while(num<sum):
#         chongzhi=eval(input('您的余额不足！请充值：'))
#         num=chongzhi+num
#         print('充值成功！')
#     flag=input('确认购物吗？，请输入y or n：')
#     if flag =='y':
#         remained=num-sum
#         print('购物成功！剩余金钱为:',remained)
# a=5
# if __name__ == '__main__':
#
#     for i in range(10):
#         print(i)
# f=open('a.txt','r',encoding= 'utf-8')