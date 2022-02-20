#LV-HTPC Branch
import socket
import datetime
import threading
import sys
import time, sched, datetime
import os

import platform
import serial
from serial.serialutil import Timeout

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
elif platform.system() == "Windows":
    port = serial.Serial("COM8", baudrate=115200, timeout=3.0)
pass

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "synapse.viewdns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
DataIn = ''
connected = True

panPos = 1000
tiltPos = 1000
speed = 50


def moveCam():
    global panPos
    global tiltPos
    port.write(str.encode(f"{panPos}-{tiltPos}#"))


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
    global panPos
    global tiltPos
    global speed
    print('listening...')
    while connected:
        DataIn = client.recv(2048).decode(FORMAT)
        if not DataIn:
            break
        print(DataIn)
        if DataIn == 'left':
            panPos = panPos - speed
            if (panPos < 500):
                panPos = 500
            moveCam()

        elif DataIn == 'right':
            panPos = panPos + speed
            if (panPos > 2000):
                panPos = 2000
            moveCam()

        elif DataIn == 'up':
            tiltPos = tiltPos - speed
            if(tiltPos < 750):
                tiltPos = 750
            moveCam()

        elif DataIn == 'down':
            tiltPos = tiltPos + speed
            if(tiltPos > 2000):
                tiltPos = 2000
            moveCam()

        elif DataIn == 'low':
            speed = 50
        
        elif DataIn == 'med':
            speed = 100

        elif DataIn == 'hi':
            speed = 250
        
        elif DataIn == 'window':
            panPos = 1100;
            tiltPos = 1400;
            port.write(str.encode(f"{panPos}-{tiltPos}#"))
        
        elif DataIn == 'couch':
            panPos = 1700;
            tiltPos = 1300;
            port.write(str.encode(f"{panPos}-{tiltPos}#"))

        elif DataIn == 'fire':
            panPos = 2000;
            tiltPos = 1200;
            port.write(str.encode(f"{panPos}-{tiltPos}#"))

        elif DataIn == 'on':
            port.write(str.encode(f"on-{tiltPos}#"))

        elif DataIn == 'off':
            port.write(str.encode(f"off-{tiltPos}#")) 

        print(f"{panPos}-{tiltPos}#")
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
    port.write(str.encode(f"on-{tiltPos}#")) 
    while connected:
        smsg = input("enter msg (q to close): ")
        if smsg == 'q':
            port.write(str.encode(f"off-{tiltPos}#")) 
            time.sleep(1)
            send(DISCONNECT_MESSAGE)
            time.sleep(1)
            connected = False
        else:
            send(smsg)
            time.sleep(.3)


SockThread = threading.Thread(target=SocketIn, args=())
SockThread.start()

inputThead = threading.Thread(target=useInput, args=())
inputThead.start()

send(name)

#todo input hangs up the DataIn var to be displayed
while connected:
    # smsg = input("enter msg: \n")
    # smsg = '#'
    time.sleep(.2)
    # send(smsg)
