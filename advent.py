import datetime
from multiprocessing import Process
import sys
import os
import time
import platform
import serial
from serial.serialutil import Timeout

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
elif platform.system() == "Windows":
    port = serial.Serial("COM15", baudrate=115200, timeout=3.0)
pass

def advent():
    day = datetime.date.today()
    port.write(str.encode("out1on#"))
    time.sleep(.5)
    port.write(str.encode("out3on#"))
    time.sleep(.5)
    port.write(str.encode("out5on#"))
    time.sleep(.5)
    port.write(str.encode("out7on#"))
    time.sleep(.5)
    port.write(str.encode("out2on#"))
    time.sleep(.5)
    port.write(str.encode("out4on#"))
    time.sleep(.5)
    port.write(str.encode("out6on#"))
    time.sleep(.5)
    port.write(str.encode("out8on#"))
    time.sleep(.5)
    for i in range(50, -1, -1):
        port.write(str.encode(f"0,{i},0,100,0#"))
        port.write(str.encode("show#"))
        time.sleep(.07)
    day = int(day.strftime("%d")) * 2
    for i in range(0, day, 2):
        port.write(str.encode(f"2,{i},0,0,100#"))
        port.write(str.encode("show2#"))
        time.sleep(.1)
        port.write(str.encode(f"3,{i},0,0,100#"))
        port.write(str.encode("show3#"))
        time.sleep(.1)
        port.write(str.encode(f"4,{i},0,0,100#"))
        port.write(str.encode("show4#"))
        time.sleep(.1)
        port.write(str.encode(f"5,{i},0,0,100#"))
        port.write(str.encode("show5#"))
        time.sleep(.1)
    
    for i in range(24):
        port.write(str.encode(f"1,{i},200,200,200#"))
        port.write(str.encode("show1#"))
        time.sleep(.07)


def runAdvent():
    p = Process(target=advent, args=())
    p.start()