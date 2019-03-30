#coding:utf-8
__author__ = 'sn'
"""socket 客户端"""

import socket
import datetime

HOST = '127.0.0.1'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connect to %s:%d OK" %(HOST, PORT))
data = s.recv(1024)
print("recevied:", data)
input("按任意键回车后退出！")
s.close()

