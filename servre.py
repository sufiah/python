#!/usr/bin/python
# -*- coding: UTF-8 -*-
# server.py

import socket


s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(2)

while True:
    c, addr = s.accept()
    print '链接地址：', addr #打印获取到的客户端ip，端口号
    c.send("Hello World")  #发送到客户端
    c.close()






