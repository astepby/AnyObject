# coding: utf-8
import socket
import sys, os
sys.path.append(os.pardir)  
import xmlParse


print("anyObject ver.1 started.")

while True:
    print(">> Waiting for the input data from the client........")

    HOST='' #호스트를 지정하지 않으면 가능한 모든 인터페이스를 의미한다.
    PORT=8765 #포트지정

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    s.listen(100) #접속이 있을때까지 기다림
    conn, addr=s.accept() #접속 승인
    print('>> Connected by',addr)

    data=conn.recv(1024) #바이트 data 길이 확인
    print(">> Echo client message: ",data)

    data=data.decode('ascii')
    data="[anyObject msg]: "+data
    data=data.encode(encoding='utf-8', errors='strict')
    print(type(data))



    conn.send(data)
    conn.close()