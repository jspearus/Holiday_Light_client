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

def ring():
    port.write(str.encode("1,2,0,0,0#"))
    port.write(str.encode("1,3,150,0,0#"))
    port.write(str.encode("2,5,0,0,0#"))
    port.write(str.encode("2,4,150,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(.2)
    port.write(str.encode("1,3,0,0,0#"))
    port.write(str.encode("1,4,150,0,0#"))
    port.write(str.encode("2,4,0,0,0#"))
    port.write(str.encode("2,3,150,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(.2)
    port.write(str.encode("1,4,0,0,0#"))
    port.write(str.encode("1,5,150,0,0#"))
    port.write(str.encode("2,3,0,0,0#"))
    port.write(str.encode("2,2,150,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(1)
    port.write(str.encode("1,5,0,0,0#"))
    port.write(str.encode("1,4,150,0,0#"))
    port.write(str.encode("2,2,0,0,0#"))
    port.write(str.encode("2,3,150,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(.2)
    port.write(str.encode("1,4,0,0,0#"))
    port.write(str.encode("1,3,150,0,0#"))
    port.write(str.encode("2,3,0,0,0#"))
    port.write(str.encode("2,4,150,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(.2)
    port.write(str.encode("1,3,0,0,0#"))
    port.write(str.encode("1,2,150,0,0#"))
    port.write(str.encode("2,4,0,0,0#"))
    port.write(str.encode("2,5,150,0,0#"))
    port.write(str.encode("show#"))


def bells():
    time.sleep(2.0)
    port.write(str.encode("0,8,20,20,20#"))
    port.write(str.encode("0,9,20,20,20#"))
    port.write(str.encode("0,10,20,20,20#"))
    port.write(str.encode("0,11,20,20,20#"))
    port.write(str.encode("0,12,20,20,20#"))
    port.write(str.encode("0,13,20,20,20#"))
    port.write(str.encode("0,14,20,20,20#"))
    port.write(str.encode("0,15,20,20,20#"))
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
    port.write(str.encode("0,59,15,15,15#"))
    port.write(str.encode("0,60,15,15,15#"))
    port.write(str.encode("1,2,150,0,0#"))
    port.write(str.encode("2,5,150,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(1)
    ring()
    time.sleep(1)
    ring()
    time.sleep(1)
    ring()
    time.sleep(1)
    ring()
    time.sleep(1)
    ring()
    time.sleep(1)
    ring()
    time.sleep(1)
    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))   

def runBells():
    p = Process(target=bells, args=())
    p.start()



    

     