#Hoiday_controller Branch
import socket
import datetime
import threading
import sys
import os
import time
import platform
import serial
from tkinter import *
from serial.serialutil import Timeout
from grinch import runGrinch
from snow import runSnowman, runSnow
from bells import runBells
from general import runTree, runtest1,  runInit, runCloak, runLoad

root = Tk()

def on_closing():
    os.system("pcmanfm --set-wallpaper /home/pi/Pictures/base.jpg")
    send(DISCONNECT_MESSAGE)
    time.sleep(1)
    connected = False
    root.destroy()

root.configure(background='black')
root.title("Holiday Remote")
root.geometry('150x620+850+20')

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
smsg = ''
mode = "loud"
today = datetime.datetime.now()
print(f'OS detected: {platform.system()}')
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

############  COMMAND FUNCTIONS ##################

def init():
    file = "/home/pi/Videos/bootup.mp4"
    runtest1()
    os.system("vlc  " + file)

def killswitch():
    file = "/home/pi/Music/012SystemImpared.mp3"
    os.system("pcmanfm --set-wallpaper /home/pi/Pictures/base.jpg")
    os.system("vlc  " + file)
    send(DISCONNECT_MESSAGE)
    time.sleep(1)
    connected = False
    root.destroy()

def mute():
    file = "/home/pi/Music/the_division_pulse.mp3"
    runCloak()
    os.system("vlc  " + file)
    os.system("sudo amixer cset numid=3 0%")

def loud():
    os.system("sudo amixer cset numid=3 100%")
    file = "/home/pi/Music/division_completed.mp3"
    runLoad()
    os.system("vlc  " + file)

def grinch():
    file = "/home/pi/Videos/Grinch.mp4"
    runGrinch()
    os.system("vlc  " + file)

def snowman1():
    file = "/home/pi/Videos/snowman.mp4"
    runSnowman()
    os.system("vlc  " + file)

def snowman2():
    file = "/home/pi/Videos/snowman2.mp4"
    runSnowman()
    os.system("vlc  " + file)

def snow():
    file = "/home/pi/Videos/snowing.mp4"
    runSnow()
    os.system("vlc  " + file)

def carol1():
    file = "/home/pi/Videos/CarolofTheBellsVader.mp4"
    runBells()
    os.system("vlc  " + file)

def carol2():
    file = "/home/pi/Videos/CarolofTheBellsMedel.mp4"
    runBells()
    os.system("vlc  " + file)

###########################################################
def SocketIn():
    global DataIn
    global connected
    global smsg
    print('listening...')
    while connected:
        DataIn = client.recv(2048).decode(FORMAT)
        if not DataIn:
            break
        print(DataIn)
        #########################    COMMANDS ########################

        if DataIn == 'grinch':
            grinch()

        elif DataIn == 'snowman':
            snowman1()

        elif DataIn == 'snowman2':
            snowman2()
        
        elif DataIn == 'snow':
            snow()

        elif DataIn == 'carol1':
            carol1()

        elif DataIn == 'carol2':
            carol2()
        
        elif DataIn == "init":
            init()

        elif DataIn == "stealth":
            mute()
        
        elif DataIn == "loud":
            loud()

        elif DataIn == "close":
            killswitch()
            
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
    global smsg
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
    print("xBee Listening...")
    while connected:
        Data = xBee.readline()
        Data = str(Data, 'UTF-8')
        data = Data.split(',')
        # serLabel.config(text=data[0])
        if 'snowman' in data[0]:
            snowman1()

        elif 'grinch' in data[0]:
            grinch()

        elif 'init' in data[0]:
            init()

        elif 'stealth' in data[0]:
            mute()

        elif 'loud' in data[0]:
            loud()

        data = ''
        time.sleep(.2)

def fromUI(data):
    if data == "init":
        init()

    elif data == "stealth":
        mute()

    elif data == "loud":
        loud()

    elif data == "grinch":
        grinch()

    elif data == "snowman":
        snowman1()

    elif data == "vader":
        carol1()


def runUi():
    global DataIn
    global mode
    print("timer")
    while connected:
        time.sleep(.2)
        today = datetime.datetime.now()
        if today.hour > 5 and today.hour < 12 and mode != "silent":
            mode = "silent"
            mute()

        if today.hour > 12 and mode != "loud":
            mode = "loud"
            loud()



SockThread = threading.Thread(target=SocketIn, args=())
SockThread.setDaemon(True)
SockThread.start()

inputThead = threading.Thread(target=useInput, args=())
inputThead.setDaemon(True)
inputThead.start()

serial = threading.Thread(target=serialRead, args=())
serial.setDaemon(True)
serial.start()

UiThread = threading.Thread(target=runUi, args=())
UiThread.setDaemon(True)
UiThread.start()

controlPanel = LabelFrame(root, text="Ctrlpanel", bg="black", highlightcolor="red", fg="red", bd=5, width=125, height=600,)
controlPanel.place(x=10, y=5)

initBtn = Button(controlPanel, text="Init", height=2,
                 width=5, bg="green", fg="black", font=("Arial", 10), command=lambda: fromUI("init"))
initBtn.place(x=25, y=20)

loudBtn = Button(controlPanel, text="Loud", height=2,
                 width=5, bg="green", fg="black", font=("Arial", 10), command=lambda: fromUI("loud"))
loudBtn.place(x=25, y=110)

muteBtn = Button(controlPanel, text="Mute", height=2,
                 width=5, bg="green", fg="black", font=("Arial", 10), command=lambda: fromUI("stealth"))
muteBtn.place(x=25, y=210)

grinchBtn = Button(controlPanel, text="Grinch", height=2,
                 width=5, bg="green", fg="black", font=("Arial", 10), command=lambda: fromUI("grinch"))
grinchBtn.place(x=25, y=310)

snowmanBtn = Button(controlPanel, text="Snowman", height=2,
                 width=5, bg="green", fg="black", font=("Arial", 10), command=lambda: fromUI("snowman"))
snowmanBtn.place(x=25, y=410)

vaderBtn = Button(controlPanel, text="Vader", height=2,
                 width=5, bg="green", fg="black", font=("Arial", 10), command=lambda: fromUI("vader"))
vaderBtn.place(x=25, y=510)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

