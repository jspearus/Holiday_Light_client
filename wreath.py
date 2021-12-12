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


def wreath():
    port.write(str.encode("0,11,0,100,0#"))
    port.write(str.encode("0,13,0,100,0#"))
    port.write(str.encode("0,18,0,100,0#"))
    port.write(str.encode("0,19,0,100,0#"))
    port.write(str.encode("0,20,0,100,0#"))
    port.write(str.encode("0,21,0,100,0#"))
    port.write(str.encode("0,26,0,100,0#"))
    port.write(str.encode("0,30,0,100,0#"))
    port.write(str.encode("0,31,0,100,0#"))
    port.write(str.encode("0,32,0,100,0#"))
    port.write(str.encode("0,33,0,100,0#"))
    port.write(str.encode("0,37,0,100,0#"))
    port.write(str.encode("0,38,0,100,0#"))
    port.write(str.encode("0,41,0,100,0#"))
    port.write(str.encode("0,42,0,100,0#"))
    port.write(str.encode("0,47,0,100,0#"))
    port.write(str.encode("0,49,0,100,0#"))
    port.write(str.encode("0,50,0,100,0#"))
    port.write(str.encode("0,51,0,100,0#"))
    port.write(str.encode("0,52,0,100,0#"))
    port.write(str.encode("0,59,0,100,0#"))
    port.write(str.encode("0,60,0,100,0#"))
    port.write(str.encode("0,12,100,0,0#"))
    port.write(str.encode("0,17,100,0,0#"))
    port.write(str.encode("0,25,100,0,0#"))
    port.write(str.encode("0,46,100,0,0#"))
    port.write(str.encode("0,53,100,0,0#"))
    port.write(str.encode("0,61,100,0,0#"))

    port.write(str.encode("show#"))

    time.sleep(10)

    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))



def runWreath():
    tProc = Process(target=wreath, args=())
    tProc.start()