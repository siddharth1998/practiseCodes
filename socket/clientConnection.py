import socket

connection=socket.socket()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:


    connection.connect(("127.0.0.1",5555))

    while (True):
        connection.send(input().encode())

        msg=connection.recv(1024)

        print("At Client : %s"%msg.decode())