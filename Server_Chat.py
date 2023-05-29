from socket import *
from threading import *


def receive(client):
    while True:
        message = client.recv(2048)
        for client in clients:
            client.send(message)


s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9001
s.bind((host, port))
s.listen(5)
clients = []
while True:
    client, address = s.accept()
    clients.append(client)
    print(f"Connected to {str(address)}")
    recieve_thread = Thread(target=receive, args=(client,))
    recieve_thread.start()
