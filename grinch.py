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


def grinch():
    time.sleep(2.2)
    #trunk
    port.write(str.encode("0,4,32,10,4#"))
    #tree
    port.write(str.encode("0,9,0,120,0#"))
    port.write(str.encode("0,10,0,120,0#"))
    port.write(str.encode("0,11,150,0,0#"))#
    port.write(str.encode("0,12,0,150,0#"))
    port.write(str.encode("0,13,0,150,0#"))
    port.write(str.encode("0,18,0,150,0#"))
    port.write(str.encode("0,19,0,150,0#"))
    port.write(str.encode("0,20,0,150,0#"))
    port.write(str.encode("0,21,150,0,0#"))#
    port.write(str.encode("0,22,0,150,0#"))
    port.write(str.encode("0,26,0,150,0#"))
    port.write(str.encode("0,27,150,0,0#"))#
    port.write(str.encode("0,28,0,150,0#"))
    port.write(str.encode("0,35,150,0,0#"))#
    port.write(str.encode("0,36,0,150,0#"))
    port.write(str.encode("0,37,0,150,0#"))
    port.write(str.encode("0,43,0,150,0#"))
    #top
    port.write(str.encode("0,52,150,0,0#")) #
    port.write(str.encode("show#"))

    time.sleep(5)

    port.write(str.encode("0,52,0,150,0#"))
    port.write(str.encode("show#"))
    time.sleep(.5)
    port.write(str.encode("0,35,0,150,0#"))
    port.write(str.encode("show#"))
    time.sleep(.5)
    port.write(str.encode("0,27,0,150,0#"))
    port.write(str.encode("show#"))
    time.sleep(.5)
    port.write(str.encode("0,21,0,150,0#"))
    port.write(str.encode("show#"))
    time.sleep(.5)
    port.write(str.encode("0,11,0,150,0#"))
    port.write(str.encode("show#"))
    time.sleep(2)
    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))   

def runGrinch():
    p = Process(target=grinch, args=())
    p.start()



    

     