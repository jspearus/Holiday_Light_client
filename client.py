#Hoiday_controller Branch
import socket
import datetime
import threading
import sys
import os
import time
import platform
import serial
from serial.serialutil import Timeout
from grinch import runGrinch
from snow import runSnow
from general import runTree, runtest1,  runInit, runCloak, runLoad

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
if platform.system() == "Linux":
    xBee = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)
    xBee.write(str.encode("Remote_Online#\r"))


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
    print(platform.system())
    while connected:
        DataIn = client.recv(2048).decode(FORMAT)
        if not DataIn:
            break
        print(DataIn)
        #########################    COMMANDS ########################

        if DataIn == 'play':
            file = "/home/pi/Videos/Grinch.mp4"
            runGrinch()
            os.system("vlc  " + file)

        elif DataIn == 'snow':
            file = "/home/pi/Videos/snow.mp4"
            runSnow()
            os.system("vlc  " + file)

    #####################################################################

        elif DataIn == 'Halloween':
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

        elif DataIn == "test":
            file = "/home/pi/Videos/bootup.mp4"
            runtest1()
            os.system("vlc  " + file)

        elif DataIn == "stealth":
            file = "/home/pi/Music/018Cloak.mp3"
            runCloak()
            os.system("vlc  " + file)
            os.system("sudo amixer cset numid=3 0%")
        
        elif DataIn == "loud":
            os.system("sudo amixer cset numid=3 100%")
            file = "/home/pi/Music/003CoreFunction.mp3"
            runLoad()
            os.system("vlc  " + file)
            

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
    smsg = ''
    runInit()
    while connected:
        try:
            smsg = input("enter msg (q to close): ")
        except EOFError as e:
            time.sleep(2)
            pass
        if smsg == 'q':
            os.system("pcmanfm --set-wallpaper /home/pi/Pictures/base.jpg")
            send(DISCONNECT_MESSAGE)
            time.sleep(1)
            connected = False
        else:
            send(smsg)
            time.sleep(.3)


def serialRead():
    global connected
    print("Listening to xBee...")
    while connected:
        Data = xBee.readline()
        Data = str(Data, 'UTF-8')
        data = Data.split(',')
        # serLabel.config(text=data[0])
        if 'snowman' in data[0]:
            file = "/home/pi/Videos/snow.mp4"
            runSnow()
            os.system("vlc  " + file)

        elif 'grinch' in data[0]:
            file = "/home/pi/Videos/Grinch.mp4"
            runGrinch()
            os.system("vlc  " + file)

        elif 'init' in data[0]:
            file = "/home/pi/Videos/bootup.mp4"
            runtest1()
            os.system("vlc  " + file)
        
        elif 'stealth' in data[0]:
            file = "/home/pi/Music/018Cloak.mp3"
            runCloak()
            os.system("vlc  " + file)
            os.system("sudo amixer cset numid=3 0%")

        elif 'loud' in data[0]:
            os.system("sudo amixer cset numid=3 100%")
            file = "/home/pi/Music/003CoreFunction.mp3"
            runLoad()
            os.system("vlc  " + file)

        data = ''
        time.sleep(.2)


SockThread = threading.Thread(target=SocketIn, args=())
SockThread.setDaemon(True)
SockThread.start()

inputThead = threading.Thread(target=useInput, args=())
inputThead.setDaemon(True)
inputThead.start()

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

while connected:
    # smsg = input("enter msg: \n")
    # smsg = '#'
    time.sleep(.2)
    # send(smsg)
