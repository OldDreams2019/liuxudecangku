import pygame
import random
# # 初始化
# pygame.init()
#
# SIZE = (1000, 500)
# screen = pygame.display.set_mode(SIZE)
# pygame.display.set_caption('旭哥哥出品')
# # 加载位图
# background = pygame.image.load('snow.jpg')
#
# # 定义一个雪花列表
# snow = []
# # 初始化雪花
# for i in range(300):
#     x = random.randrange(0, SIZE[0])
#     y = random.randrange(0, SIZE[1])
#     speedx = random.randint(-1, 2)
#     speedy = random.randint(3 ,8)
#     snow.append([x, y, speedx, speedy])
#
# done = False
# while not done:
#     # 消息事件循环，判断退出
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     # 绘制位图
#     screen.blit(background, (0 ,0))
#
#     # 雪花列表循环
#     for i in range(len(snow)):
#         # 绘制雪花，颜色、位置、大小
#         pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])
#
#         # 移动雪花位置（下一次循环起效）
#         snow[i][0] += snow[i][2]
#         snow[i][1] += snow[i][3]
#
#         # 如果雪花落出屏幕，重设位置
#         if snow[i][1] > SIZE[1]:
#             snow[i][1] = random.randrange(-50, -10)
#             snow[i][0] = random.randrange(0, SIZE[0])
#
#     pygame.display.flip()
#     # clock.tick(20)
#
# pygame.quit()

#查看列表中第一个和第二大的数
# a=input('>>.')
# b=a.split(',')
# b=[int(i) for i in b]
# b.sort()
# o=[]
# f=b.count(b[-1])
# for k in range(1,f+1):
#     o.append(b[-1])
#     b.remove(b[-1])
# d=b.count(b[-1])
# for j in range(1,d+1):
#     o.append(b[-1])
# print(o)



# def  a(x,y):
#     for i in  range(x):
#         for j in range(x):





import socket
#  客户端
# #创建一个套接字
# while True:
#    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器
#    sock.connect(('192.168.0.81',3000))
# # 将qq当做请求发送给服务器
#    qq=input('<<<')
#    sock.send(qq.encode('utf-8'))
# # 接收响应
#    ww=sock.recv(1024)
#    print(ww.decode('utf-8'))
#    so



#udp客户端
import socket
# while True:
#     s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     host=(('192.168.0.90',3000))
#     msg=input('<<<')
#     s.sendto(msg.encode('utf-8'),host)
#     #接收响应
#     reg=s.recv(1024)
#     print(reg.decode('utf-8'))


import  time


def a(x):
    num=0
    for i in range(x+1):
        num+=i
    return num
print(a(100))