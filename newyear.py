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

def newYear():
    day = datetime.date.today()
    port.write(str.encode("out2off#"))
    port.write(str.encode("out4off#"))
    port.write(str.encode("out6off#"))
    port.write(str.encode("out8off#"))
    time.sleep(.5)
    port.write(str.encode("out1on#"))
    time.sleep(.5)
    port.write(str.encode("out3on#"))
    time.sleep(.5)
    port.write(str.encode("out5on#"))
    time.sleep(.5)
    port.write(str.encode("out7on#"))
    time.sleep(.5)
    for i in range(50, -1, -1):
        port.write(str.encode(f"0,{i},100,0,0#"))
        port.write(str.encode("show#"))
        time.sleep(.07)
    
    for i in range(24):
        port.write(str.encode(f"1,{i},128,80,32#"))
        port.write(str.encode("show1#"))
        time.sleep(.07)


def runNewYear():
    p = Process(target=newYear, args=())
    p.start()