from socket import *
from _thread import *
import threading


def thread_receive(connection):
    while True:
        x = connection.recv(2048)
        print(x.decode('UTF-8'))


def thread_send(connection):
    while True:
        connection.send(input("Server:").encode("UTF-8"))


def client_thread(connection):
    receive = threading.Thread(target=thread_receive, args=(connection,))
    receive.start()
    send = threading.Thread(target=thread_send, args=(connection,))
    send.start()


s = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7000
s.bind((host, port))
s.listen(5)
try:
    while True:
        # establish connection with client 
        connection, addr = s.accept()

        print('Connected to :', addr[0])

        # Start a new thread and return its identifier 
        start_new_thread(client_thread, (connection,))
except KeyboardInterrupt:
    s.close()
