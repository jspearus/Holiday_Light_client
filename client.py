import socket
import datetime
import threading
import time
import os

import platform
import serial
from serial.serialutil import Timeout

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "dgscore.ddns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
DataIn = ''

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
elif platform.system() == "Windows":
    port = serial.Serial("COM15", baudrate=115200, timeout=3.0)
    pass

port.write(str.encode("0,1,0,0,150#"))
port.write(str.encode("0,2,0,0,150#"))
port.write(str.encode("0,3,0,0,150#"))
port.write(str.encode("0,4,0,0,150#"))
port.write(str.encode("show#"))
time.sleep(2)
port.write(str.encode("clear#"))
port.write(str.encode("show#"))


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
    while True:
        if client.recv(2048).decode(FORMAT) != '':
            DataIn = client.recv(2048).decode(FORMAT)
            print(DataIn)
            DataIn = ''


SockThread = threading.Thread(target=SocketIn, args=())
SockThread.setDaemon(True)
SockThread.start()

send("Light")

#todo input hangs up the DataIn var to be displayed
while True:
    # smsg = input("enter msg: \n")
    smsg = ' '
    time.sleep(.2)
    if smsg == 'q':
        break
    send(smsg)
send(DISCONNECT_MESSAGE)
