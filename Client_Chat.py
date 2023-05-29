from socket import *
from tkinter import *
from threading import *


def recieve(client):
    while True:
        message = client.recv(2048).decode('utf-8')
        chat_text.insert(END, message + "\n")


def enter_username():
    global username
    username = username_entry.get()


def send_message(client):
    message = message_entry.get()
    message = username + ":" + message
    chat_text.insert(END, message + "\n")
    message_entry.delete(0, END)
    client.send(message.encode('utf-8'))


window = Tk()
window.title("client")
window.geometry("850x450")
left_frame = Frame(window)
right_frame = Frame(window, )
bottom_frame = Frame(window)
s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9001

s.connect((host, port))

# Grid layout for frames
left_frame.grid(row=0, column=0, rowspan=3, columnspan=1, sticky=S + E + W)
right_frame.grid(row=0, column=1, rowspan=5, columnspan=3, sticky=S + E + W)
bottom_frame.grid(row=5, column=1, rowspan=1, columnspan=3, sticky=S + E + W)

# Grid layout for left frame
username_label = Label(left_frame, text="Username: ")
username_label.grid(row=0, column=0)
username_entry = Entry(left_frame)
username_entry.grid(row=0, column=1)
username_button = Button(left_frame, text="Enter", command=enter_username)
username_button.grid(row=1, columnspan=2)

# Grid layout for right frame
chat_text = Text(right_frame)
chat_text.pack(side="left")

# Grid layout for bottom frame
message_entry = Entry(bottom_frame)
message_entry.pack(side="left", expand=1, fill="both")
message_button = Button(bottom_frame, text="Send", width=15, height=1, command=lambda : send_message(s))
message_button.pack(side="right", )


username = ''
recieve_thread = Thread(target=recieve, args=(s,))
recieve_thread.start()
window.mainloop()
