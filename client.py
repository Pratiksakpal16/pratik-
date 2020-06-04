import socket
s=socket.socket()
s.connect(("127.0.0.1",3438))
print("connection successful")
while(1):
    print(s.recv(1024).decode())
    b=input("enter mesage:")
    s.send(b.encode())
