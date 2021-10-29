import socket
import datetime
import threading
import sys
import time

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "dgscore.ddns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
DataIn = ''
connected = True


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))


def SocketIn():
    global DataIn
    global connected
    while connected:
        if client.recv(2048).decode(FORMAT):
            DataIn = client.recv(2048).decode(FORMAT)
            print(DataIn)
            DataIn = ''


#todo EDIT NAME.TXT TO THE NAME OF DEVICE
with open('name.txt') as f:
    name = f.readline()
    send(name)
    print(f"Connected as: {name}")


def useInput():
    global connected
    while connected:
        smsg = input("enter msg (q to close): ")
        if smsg == 'q':
            send(DISCONNECT_MESSAGE)
            time.sleep(1)
            connected = False
        else:
            send(smsg)
            time.sleep(.3)
            send(smsg)


SockThread = threading.Thread(target=SocketIn, args=())
inputThead = threading.Thread(target=useInput, args=())
inputThead.setDaemon(True)
SockThread.setDaemon(True)
SockThread.start()
inputThead.start()

while connected:
    time.sleep(.2)
