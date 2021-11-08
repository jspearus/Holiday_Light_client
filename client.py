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
today = datetime.date.today()

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))


#todo update this fucntion every hour???
def getHoliday():
    global name
    global today
    global connected
    while connected:
        time.sleep(900)# 15 mins
        if today < datetime.date.today():
            today = datetime.date.today()
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

timeThead = threading.Thread(target=getHoliday, args=())
timeThead.setDaemon(True)
timeThead.start()
#todo input hangs up the DataIn var to be displayed
while connected:
    # smsg = input("enter msg: \n")
    # smsg = '#'
    time.sleep(.2)
    # send(smsg)
