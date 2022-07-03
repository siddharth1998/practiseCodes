import socket 

echoSocket=socket.socket()

echoSocket.bind(("127.0.0.1",5555))

echoSocket.listen()

while(True):

    (clientSocket,ClientAddress)=echoSocket.accept()
    with clientSocket:
        while(True):
            data=clientSocket.recv(1024)
            print("At server: %s"%data)

            if(data!=b''):
                clientSocket.send(data)
                