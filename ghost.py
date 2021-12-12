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


def ghost():
    port.write(str.encode("0,2,20,20,20#"))
    port.write(str.encode("0,4,20,20,20#"))
    port.write(str.encode("0,6,20,20,20#"))
    port.write(str.encode("0,9,20,20,20#"))
    port.write(str.encode("0,10,20,20,20#"))
    port.write(str.encode("0,12,20,20,20#"))
    port.write(str.encode("0,14,20,20,20#"))
    port.write(str.encode("0,17,20,20,20#"))
    port.write(str.encode("0,22,20,20,20#"))
    port.write(str.encode("0,25,20,20,20#"))
    port.write(str.encode("0,30,20,20,20#"))
    port.write(str.encode("0,33,20,20,20#"))
    port.write(str.encode("0,38,20,20,20#"))
    port.write(str.encode("0,41,20,20,20#"))
    port.write(str.encode("0,46,20,20,20#"))
    port.write(str.encode("0,50,20,20,20#"))
    port.write(str.encode("0,51,20,20,20#"))
    port.write(str.encode("0,52,20,20,20#"))
    port.write(str.encode("0,53,20,20,20#"))

    port.write(str.encode("0,42,20,0,0#"))
    port.write(str.encode("0,45,20,0,0#"))
   

    port.write(str.encode("show#"))
    
    time.sleep(10)

    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))



def runGhost():
    tProc = Process(target=ghost, args=())
    tProc.start()