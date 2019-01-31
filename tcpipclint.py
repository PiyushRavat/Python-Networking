import socket

s = socket.socket()

s.connect(("localhost",8000))

msg = s.recv(1024)

while msg:
    print("Received: ",msg.decode())
    msg = s.recv(1024)

s.close()