from socket import *

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.connect((host, port))
try:
    while True:
        s.send((input("Client:")).encode('utf-8'))
        x = s.recv(2048)
        print("Server:", x.decode('utf-8'))
except KeyboardInterrupt:
    s.close()
