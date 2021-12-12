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


def pumpkin():
    port.write(str.encode("0,2,252,69,3#"))
    port.write(str.encode("0,3,252,69,3#"))
    port.write(str.encode("0,4,252,69,3#"))
    port.write(str.encode("0,5,252,69,3#"))
    port.write(str.encode("0,9,252,69,3#"))
    port.write(str.encode("0,14,252,69,3#"))
    port.write(str.encode("0,16,252,69,3#"))
    port.write(str.encode("0,23,252,69,3#"))
    port.write(str.encode("0,24,252,69,3#"))
    port.write(str.encode("0,31,252,69,3#"))
    port.write(str.encode("0,32,252,69,3#"))
    port.write(str.encode("0,39,252,69,3#"))
    port.write(str.encode("0,41,252,69,3#"))
    port.write(str.encode("0,42,252,69,3#"))
    port.write(str.encode("0,43,252,69,3#"))
    port.write(str.encode("0,44,252,69,3#"))
    port.write(str.encode("0,45,252,69,3#"))
    port.write(str.encode("0,46,252,69,3#"))

    port.write(str.encode("0,52,0,20,0#"))
    port.write(str.encode("0,58,0,20,0#"))
   

    port.write(str.encode("show#"))
    
    time.sleep(10)

    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))



def runPumpkin():
    tProc = Process(target=pumpkin, args=())
    tProc.start()