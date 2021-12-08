#Master Branch
import socket
import select
import datetime
import threading
import sys
import time, sched, datetime
import os
import platform

from general import runTest1, runTestTop, runTreeOff
from advent import runAdvent
from events import runSnow, runRain

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "dgscore.ddns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.setblocking(0)

DataIn = ''
connected = True
weather = "none"
today = datetime.datetime.now()
mode = "off"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))


#todo update this fucntion every 15 mins
def getHoliday():
    global connected
    global name
    global today
    global weather
    while connected:
        time.sleep(200) #############
        if today.day < datetime.datetime.now().day:
            today = datetime.datetime.now() 
            send(f"{name}, holiday")
            runAdvent()
        if weather == "snow":
            runSnow()
        elif weather == "rain":
            runRain()

            
    


def SocketIn():
    global DataIn
    global connected
    global weather
    print('listening...')
    while connected:
        ready = select.select([client], [], [], 30)
        if ready[0]:
            DataIn = client.recv(2048).decode(FORMAT)
            print(DataIn)
        else:
            # code here to handle lost conection from server
            pass
            

        ####################### COMMANDS ##################
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
        ##########################################################################################
        elif DataIn == "test":
            runTest1()

        elif DataIn == "advent":
            runAdvent()

        elif DataIn == "snow":
            weather = DataIn
            runSnow()

        elif DataIn == "SNOW":
            send("ctrl, snow")
            weather = "snow"
            runSnow()
        
        elif DataIn == "rain":
            weather = DataIn
            runRain()

        elif DataIn == "cloudy":
            weather = DataIn

        elif DataIn == "clear":
            weather = DataIn

        elif DataIn == "off":
            runTreeOff()

        ############################################################################################
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

timeThead = threading.Thread(target=getHoliday, args=())
timeThead.setDaemon(True)
timeThead.start()

#todo input hangs up the DataIn var to be displayed
while connected:
    time.sleep(1)
    today = datetime.datetime.now()
    if today.hour > 3 and mode != "advent":
        mode = "advent"
        runAdvent()

    if today.hour > 22 and mode != "off":
        mode = "off"
        runTreeOff()