#Master Branch
import socket
import datetime
import threading
import sys
import time, sched, datetime
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
s = sched.scheduler(time.time, time.sleep)
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


#todo update this fucntion every hour???
def getDay():
    send(f"{name}, holiday")


def SocketIn():
    global DataIn
    global connected
    print('listening...')
    while connected:
        DataIn = client.recv(2048).decode(FORMAT)
        if not DataIn:
            break
        print(DataIn)
        if DataIn == 'Halloween':
            os.system(
                "pcmanfm --set-wallpaper /home/pi/Pictures/halloween.jpg")

        elif DataIn == 'Thanksgiving':
            os.system(
                "pcmanfm --set-wallpaper /home/pi/Pictures/thanksgiving.jpg")

        elif DataIn == 'Christmas Day':
            os.system(
                "pcmanfm --set-wallpaper /home/pi/Pictures/christmas.jpg")

        elif DataIn == "New Year's Day":
            os.system("pcmanfm --set-wallpaper /home/pi/Pictures/newyear.jpg")
        DataIn = ''
        time.sleep(.5)


#todo EDIT NAME.TXT TO THE NAME OF DEVICE
with open('name.txt') as f:
    name = f.readline()
    send(name)
    print(f"Connected as: {name}")
    send('site, devices')


def useInput():
    global connected
    while connected:
        smsg = input("enter msg (q to close): ")
        if smsg == 'q':
            os.system("pcmanfm --set-wallpaper /home/pi/Pictures/base.jpg")
            send(DISCONNECT_MESSAGE)
            time.sleep(1)
            connected = False
        else:
            send(smsg)
            time.sleep(.3)


SockThread = threading.Thread(target=SocketIn, args=())
SockThread.setDaemon(True)
SockThread.start()
inputThead = threading.Thread(target=useInput, args=())
inputThead.setDaemon(True)
inputThead.start()

send(name)
s.enter(5, 1, getDay(), argument=())
s.run()
#todo input hangs up the DataIn var to be displayed
while connected:
    # smsg = input("enter msg: \n")
    # smsg = '#'
    time.sleep(.2)
    # send(smsg)
