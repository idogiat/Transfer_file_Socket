#!/usr/bin/env python3
# server
import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

count = 0
while (1):
    s.listen(1)
    # print type(s.accept())
    conn, addr = s.accept()
    print('Connected by', addr)

    tst = open('text' + str(count) + '.txt', 'w') # create new file
    count = count + 1
    while 1:
        data = conn.recv(1024)
        if data:
            tst.write(data.decode()) # write to file
        else:
            conn.close()
            tst.close()
            break