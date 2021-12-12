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


def ball():
    port.write(str.encode("0,2,100,0,0#"))
    port.write(str.encode("0,3,100,0,0#"))
    port.write(str.encode("0,4,100,0,0#"))
    port.write(str.encode("0,5,100,0,0#"))
    port.write(str.encode("0,9,100,0,0#"))
    port.write(str.encode("0,14,100,0,0#"))
    port.write(str.encode("0,16,100,0,0#"))
    port.write(str.encode("0,23,100,0,0#"))
    port.write(str.encode("0,24,100,0,0#"))
    port.write(str.encode("0,31,100,0,0#"))
    port.write(str.encode("0,32,100,0,0#"))
    port.write(str.encode("0,39,100,0,0#"))
    port.write(str.encode("0,41,100,0,0#"))
    port.write(str.encode("0,46,100,0,0#"))
    port.write(str.encode("0,50,100,0,0#"))
    port.write(str.encode("0,51,100,0,0#"))
    port.write(str.encode("0,52,100,0,0#"))
    port.write(str.encode("0,53,100,0,0#"))
    port.write(str.encode("0,59,20,20,20#"))
    port.write(str.encode("0,60,20,20,20#"))
   
   

    port.write(str.encode("show#"))
    
    time.sleep(10)

    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))



def runBall():
    tProc = Process(target=ball, args=())
    tProc.start()