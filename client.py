#Hoiday_controller Branch
import socket
import select
import datetime
import threading
import sys
import os
import time
import platform
import serial
from numpy import random
from tkinter import *
from serial.serialutil import Timeout
from grinch import runGrinch
from wreath import runWreath
from ball import runBall
from pumpkin import runPumpkin
from ghost import runGhost
from snow import runSnowman, runSnow, runSnowflake
from bells import runBells
from general import runTree, runtest1, runInit, runCloak, runLoad

root = Tk()


def on_closing():
    os.system("pcmanfm --set-wallpaper /home/pi/Pictures/base.jpg")
    send(DISCONNECT_MESSAGE)
    time.sleep(1)
    connected = False
    root.destroy()


root.configure(background='black')
root.config(cursor="none")
root.title("Holiday Remote")
root.geometry('175x620+820+20')

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "holidayctrl.ddns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.setblocking(0)
DataIn = ''
connected = True
auto_mode = False
name = ''
smsg = ''
mode = "none"
today = datetime.datetime.now()
pre_time = today
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
    runLoad()
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

def med():
    os.system("sudo amixer cset numid=3 50%")
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

def polar1():
    file = "/home/pi/Videos/polar1.mp4"
    runSnowflake()
    runSnow()
    runSnow()
    os.system("vlc  " + file)

def polar2():
    file = "/home/pi/Videos/polar2.mp4"
    runSnow()
    runSnowflake()
    runSnow()
    os.system("vlc  " + file)

def what1():
    file = "/home/pi/Videos/wahtsthis1.mp4"
    runSnow()
    os.system("vlc  " + file)

def randomEvent():
    event = random.randint(6, size=(1))
    print(event)
    if event == 0:
        snowman1()
    elif event == 1:
        grinch()
    elif event == 2:
        carol1()
    elif event == 3:
        randomWhatsThis()
    elif event == 4:
        randomPolar()
    elif event == 5:
        snow()

def randomWhatsThis():
    event = random.randint(3, size=(1))
    print(event)
    if event == 0:
        file = "/home/pi/Videos/wahtsthis1.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 1:
        file = "/home/pi/Videos/wahtsthis2.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 2:
        file = "/home/pi/Videos/wahtsthis3.mp4"
        runSnow()
        os.system("vlc  " + file)

def randomPolar():
    event = random.randint(2, size=(1))
    print(event)
    if event == 0:
        file = "/home/pi/Videos/polar1.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 1:
        file = "/home/pi/Videos/polar2.mp4"
        runSnow()
        os.system("vlc  " + file)

def randomClaws():
    event = random.randint(6, size=(1))
    print(event)
    if event == 0:
        file = "/home/pi/Videos/sandyclaws1.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 1:
        file = "/home/pi/Videos/sandyclaws2.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 2:
        file = "/home/pi/Videos/sandyclaws3.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 3:
        file = "/home/pi/Videos/sandyclaws4.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 4:
        file = "/home/pi/Videos/sandyclaws5.mp4"
        runSnow()
        os.system("vlc  " + file)
    elif event == 5:
        file = "/home/pi/Videos/sandyclaws6.mp4"
        runSnow()
        os.system("vlc  " + file)


###########################################################
def SocketIn():
    global DataIn
    global connected
    global auto_mode
    global smsg
    print('listening...')
    while connected:
        ready = select.select([client], [], [], 30)
        if ready[0]:
            DataIn = client.recv(2048).decode(FORMAT)
            if DataIn != 'ping':
                print(DataIn)
        else:
            pass
            
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
        
        elif DataIn == 'claws':
            randomClaws()
        
        elif DataIn == 'polar':
            randomPolar()
        
        elif DataIn == 'what':
            randomWhatsThis()

        elif DataIn == "init":
            init()

        elif DataIn == "stealth":
            mute()

        elif DataIn == "loud":
            loud()

        elif DataIn == "close":
            killswitch()

        elif DataIn == "wreath":
            runWreath()
        elif DataIn == "ball":
            runBall()
        elif DataIn == "ghost":
            runGhost()
        elif DataIn == "snowflake":
            runSnowflake()
        elif DataIn == "pumpkin":
            runPumpkin()
        
        elif DataIn == "aOn":
            randomEvent()
            auto_mode = True
        
        elif DataIn == "aOff":
            auto_mode = False

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
            root.destroy()
        else:
            send(smsg)
            time.sleep(.3)


def serialRead():
    global connected
    global auto_mode
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
        
        elif 'wreath' in data[0]:
            runWreath()
        elif 'ball' in data[0]:
            runBall()
        elif 'ghost' in data[0]:
            runGhost()
        elif 'snowflake' in data[0]:
            runSnowflake()
        elif 'pumpkin' in data[0]:
            runPumpkin()
        elif 'aOn' in data[0]:
            randomEvent()
            auto_mode = True
        elif 'aOff' in data[0]:
            auto_mode = False

        data = ''
        time.sleep(.2)


def fromUI(data):
    if data == "init":
        init()

    elif data == "stealth":
        mute()

    elif data == "loud":
        loud()

    elif data == "med":
        med()

    elif data == "grinch":
        grinch()

    elif data == "snowman":
        snowman1()

    elif data == "vader":
        carol1()
        
    elif data == "polar":
        randomPolar()
    
    elif data == "what":
        randomWhatsThis()
    
    elif data == "wreath":
        runWreath()

    elif data == "ball":
        runBall()

    elif data == "ghost":
        runGhost()

    elif data == "snowflake":
        runSnowflake()

    elif data == "pumpkin":
        runPumpkin()
    

    elif data == "video":
        controlPanel.place_forget()
        Videos.place(x=10, y=5)

    elif data == "icon":
        controlPanel.place_forget()
        Icons.place(x=10, y=5)

    elif data == "settings":
        controlPanel.place_forget()
        Settings.place(x=10, y=5)

    elif data == "back":
        Videos.place_forget()
        Icons.place_forget()
        Settings.place_forget()
        controlPanel.place(x=10, y=5)


def runUi():
    global DataIn
    global mode
    global name
    global pre_time
    global auto_mode
    print("timer Running")
    while connected:
        today = datetime.datetime.now()
        if today.hour > 12 and mode != "loud":
            mode = "loud"
            loud()

        elif today.hour > 5 and today.hour < 13 and mode != "silent":
            mode = "silent"
            mute()
            
        elif today.hour < 6 and mode != "init":
            mode = "init"
            init()
        if auto_mode:
            if today.minute >= pre_time.minute + 20 or today.minute < 1:
                randomEvent()
                pre_time = today

        time.sleep(20)
    


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


############################# USER INTERFACE ###################################
controlPanel = LabelFrame(
    root,
    text="Holiday_Remote",
    bg="black",
    highlightcolor="red",
    fg="red",
    bd=5,
    width=150,
    height=600,
)
controlPanel.place(x=10, y=5)

VidBtn = Button(controlPanel,
                 text="Videos",
                 height=2,
                 width=8,
                 bg="green",
                 fg="black",
                 font=("Arial", 10),
                 command=lambda: fromUI("video"))
VidBtn.place(x=25, y=20)

IconBtn = Button(controlPanel,
                 text="Icons",
                 height=2,
                 width=8,
                 bg="green",
                 fg="black",
                 font=("Arial", 10),
                 command=lambda: fromUI("icon"))
IconBtn.place(x=25, y=110)

setBtn = Button(controlPanel,
                 text="Settings",
                 height=2,
                 width=8,
                 bg="green",
                 fg="black",
                 font=("Arial", 10),
                 command=lambda: fromUI("settings"))
setBtn.place(x=25, y=210)

Videos = LabelFrame(
    root,
    text="Videos",
    bg="black",
    highlightcolor="red",
    fg="red",
    bd=5,
    width=150,
    height=600,
)
grinchBtn = Button(Videos,
                   text="Grinch",
                   height=2,
                   width=8,
                   bg="green",
                   fg="black",
                   font=("Arial", 10),
                   command=lambda: fromUI("grinch"))
grinchBtn.place(x=25, y=20)

snowmanBtn = Button(Videos,
                    text="Snowman",
                    height=2,
                    width=8,
                    bg="green",
                    fg="black",
                    font=("Arial", 10),
                    command=lambda: fromUI("snowman"))
snowmanBtn.place(x=25, y=110)

vaderBtn = Button(Videos,
                  text="Vader",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("vader"))
vaderBtn.place(x=25, y=210)

polarBtn = Button(Videos,
                  text="Polar",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("polar"))
polarBtn.place(x=25, y=310)

whatBtn = Button(Videos,
                  text="Whats This",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("what"))
whatBtn.place(x=25, y=410)

backBtn = Button(Videos,
                  text="Back",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("back"))
backBtn.place(x=25, y=510)

Settings = LabelFrame(
    root,
    text="Settings",
    bg="black",
    highlightcolor="red",
    fg="red",
    bd=5,
    width=150,
    height=600,
)

initBtn = Button(Settings,
                 text="Init",
                 height=2,
                 width=8,
                 bg="green",
                 fg="black",
                 font=("Arial", 10),
                 command=lambda: fromUI("init"))
initBtn.place(x=25, y=20)

loudBtn = Button(Settings,
                 text="Loud",
                 height=2,
                 width=8,
                 bg="green",
                 fg="black",
                 font=("Arial", 10),
                 command=lambda: fromUI("loud"))
loudBtn.place(x=25, y=110)

muteBtn = Button(Settings,
                 text="Mute",
                 height=2,
                 width=8,
                 bg="green",
                 fg="black",
                 font=("Arial", 10),
                 command=lambda: fromUI("stealth"))
muteBtn.place(x=25, y=210)
backBtn = Button(Settings,
                  text="Back",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("back"))
backBtn.place(x=25, y=510)

Icons = LabelFrame(
    root,
    text="Icons",
    bg="black",
    highlightcolor="red",
    fg="red",
    bd=5,
    width=150,
    height=600,
)
wreathBtn = Button(Icons,
                   text="Wreath",
                   height=2,
                   width=8,
                   bg="green",
                   fg="black",
                   font=("Arial", 10),
                   command=lambda: fromUI("wreath"))
wreathBtn.place(x=25, y=20)

ballBtn = Button(Icons,
                    text="Ball",
                    height=2,
                    width=8,
                    bg="green",
                    fg="black",
                    font=("Arial", 10),
                    command=lambda: fromUI("ball"))
ballBtn.place(x=25, y=110)

snowFlakeBtn = Button(Icons,
                  text="Snowflake",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("snowflake"))
snowFlakeBtn.place(x=25, y=210)

ghostBtn = Button(Icons,
                  text="Ghost",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("ghost"))
ghostBtn.place(x=25, y=310)

pumpkinBtn = Button(Icons,
                  text="Pumpkin",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("pumpkin"))
pumpkinBtn.place(x=25, y=410)

backBtn = Button(Icons,
                  text="Back",
                  height=2,
                  width=8,
                  bg="green",
                  fg="black",
                  font=("Arial", 10),
                  command=lambda: fromUI("back"))
backBtn.place(x=25, y=510)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
