#!/usr/bin/env python3
# client
import socket
import sys

HOST = 'localhost'  # The target IP address
PORT = 50007  # The target port as used by the server
DATA = open('C:\\Users\\ido giat\\Desktop\\PyCharmProjects\\progect1\\hello.py', 'r')
BDATA = DATA.read().encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.send(BDATA)  # Put the pattern you want to send here.
s.close()