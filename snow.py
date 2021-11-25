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


def snow():
    time.sleep(5.1)
    port.write(str.encode("0,1,150,150,150#"))
    port.write(str.encode("0,2,150,150,150#"))
    port.write(str.encode("0,3,150,150,150#"))
    port.write(str.encode("0,4,150,150,150#"))
    port.write(str.encode("0,5,150,150,150#"))
    port.write(str.encode("0,6,150,150,150#"))
    port.write(str.encode("0,9,150,150,150#"))
    port.write(str.encode("0,10,150,150,150#"))
    port.write(str.encode("0,11,150,150,150#"))
    port.write(str.encode("0,12,150,150,150#"))
    port.write(str.encode("0,13,150,150,150#"))
    port.write(str.encode("0,14,150,150,150#"))
    port.write(str.encode("0,17,150,150,150#"))
    port.write(str.encode("0,18,150,150,150#"))
    port.write(str.encode("0,19,150,150,150#"))
    port.write(str.encode("0,20,150,150,150#"))
    port.write(str.encode("0,21,150,150,150#"))
    port.write(str.encode("0,22,150,150,150#"))
    port.write(str.encode("0,26,150,150,150#"))
    port.write(str.encode("0,27,150,150,150#"))
    port.write(str.encode("0,28,150,150,150#"))
    port.write(str.encode("0,29,150,150,150#"))
    port.write(str.encode("0,34,150,150,150#"))
    port.write(str.encode("0,35,150,150,150#"))
    port.write(str.encode("0,36,150,150,150#"))
    port.write(str.encode("0,37,150,150,150#"))
    port.write(str.encode("0,42,150,150,150#"))
    port.write(str.encode("0,43,150,150,150#"))
    port.write(str.encode("0,44,150,150,150#"))
    port.write(str.encode("0,45,150,150,150#"))
    port.write(str.encode("0,51,150,150,150#"))
    port.write(str.encode("0,52,150,150,150#"))
    port.write(str.encode("0,59,150,150,150#"))
    port.write(str.encode("0,60,150,150,150#"))
    port.write(str.encode("show#"))
    time.sleep(2.5)
    port.write(str.encode("0,51,0,0,0#"))
    port.write(str.encode("0,52,0,0,0#"))
    port.write(str.encode("0,59,0,0,0#"))
    port.write(str.encode("0,60,0,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(2)
    port.write(str.encode("0,26,0,0,0#"))
    port.write(str.encode("0,27,0,0,0#"))
    port.write(str.encode("0,28,0,0,0#"))
    port.write(str.encode("0,29,0,0,0#"))
    port.write(str.encode("0,34,0,0,0#"))
    port.write(str.encode("0,35,0,0,0#"))
    port.write(str.encode("0,36,0,0,0#"))
    port.write(str.encode("0,37,0,0,0#"))
    port.write(str.encode("0,42,0,0,0#"))
    port.write(str.encode("0,43,0,0,0#"))
    port.write(str.encode("0,44,0,0,0#"))
    port.write(str.encode("0,45,0,0,0#"))
    port.write(str.encode("show#"))
    time.sleep(4.25)
    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))
    

def runSnow():
    p = Process(target=snow, args=())
    p.start()



    

     