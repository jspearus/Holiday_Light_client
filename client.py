import socket
import datetime
import threading
import sys
import os
import time

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "holidayctrl.ddns.net"
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
    print('listening...')
    while connected:
        DataIn = client.recv(2048).decode(FORMAT)
        if not DataIn:
            break
        print(DataIn)
    #########################    COMMANDS ########################
        print("enter msg (q to close): ")
        if DataIn == 'play':
            file = "/home/pi/Videos/Grinch.mp4"
            os.system("vlc " + file)

        elif DataIn == 'snow':
            file = "/home/pi/Videos/snow.mp4"
            os.system("vlc " + file)
    #####################################################################

        elif DataIn == 'Halloween':
            os.system("pcmanfm --set-wallpaper /home/pi/Pictures/halloween.jpg")
        
        elif DataIn == 'Thanksgiving':
            os.system("pcmanfm --set-wallpaper /home/pi/Pictures/thanksgiving.jpg")
        
        elif DataIn == 'Christmas Day':
            os.system("pcmanfm --set-wallpaper /home/pi/Pictures/christmas.jpg")

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

while connected:
    # smsg = input("enter msg: \n")
    # smsg = '#'
    time.sleep(.2)
    # send(smsg)
