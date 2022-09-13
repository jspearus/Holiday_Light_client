#Master Branch
import socket
import datetime
import threading
import sys
import time, sched, datetime
import os, json
from pathlib import Path
import platform
import serial
from serial.serialutil import Timeout
from colorama import Fore, Back, Style

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
        
        time.sleep(.5)
        if DataIn == 'Halloween':

            os.system(
                "gsettings set org.gnome.desktop.background picture-uri file:////home/jeff/Pictures/halloween.jpg")

        elif DataIn == 'Thanksgiving':
            os.system(
                "gsettings set org.gnome.desktop.background picture-uri file:////home/jeff/Pictures/thanksgiving.jpg")

        elif DataIn == 'Christmas Day':
            os.system(
                "gsettings set org.gnome.desktop.background picture-uri file:////home/jeff/Pictures/christmas.jpg")

        elif DataIn == "New Year's Day":
            os.system("gsettings set org.gnome.desktop.background picture-uri file:////home/jeff/Pictures/newyear.jpg")
        elif DataIn == "snow":
            file = "/home/jeff/Videos/snow.mp4"
            os.system("vlc  " + file)
            # os.system("sudo amixer cset numid=3 0%")

        DataIn = ''


#todo EDIT NAME.TXT TO THE NAME OF DEVICE
f = Path('name.json')
if f.is_file():
    f = open('name.json')
    data = json.load(f)
    name = data['client'] ['deviceName']
else:
    val = input("Enter Client Device Name: ")
    data = {"client": {"deviceName": val}}
    with open('name.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    name = name = data['client'] ['deviceName']
    f.close()
    print(Fore.RED + "RESTART CLIENT FOR NAME TO BE RECOGNIZED!!!!")
    print(Style.RESET_ALL)
    #todo figure out why the client needs to be restarted when name is assigned
#########################################################################
send(name)
print(f"Connected as: {name}")
send('site, devices')


def useInput():
    global connected
    while connected:
        smsg = input("enter msg (q to close): ")
        if smsg == 'q':
            send(DISCONNECT_MESSAGE)
            os.system(
                "gsettings set org.gnome.desktop.background picture-uri file:////home/jeff/Pictures/default.jpg")
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


#todo input hangs up the DataIn var to be displayed
while connected:
    # smsg = input("enter msg: \n")
    # smsg = '#'
    time.sleep(.2)
    # send(smsg)
