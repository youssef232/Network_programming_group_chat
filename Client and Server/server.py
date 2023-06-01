from socket import *


s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.bind((host, port))
s.listen(5)
c, ad = s.accept()
print("Connection from", ad[0])
try:
    while True:
        x = c.recv(2048)
        print("Client:", x.decode('utf-8'))
        c.send((input("Server:")).encode('utf-8'))

except error as e:
    print(e)
except KeyboardInterrupt:
    print("OK")
    s.close()
