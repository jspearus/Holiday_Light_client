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

def test1():
    time.sleep(2)
    for i in range(50):
        port.write(str.encode(f"0,{i},100,0,0#"))
        port.write(str.encode("show#"))
        time.sleep(.01)
    port.write(str.encode("out1on#"))
    port.write(str.encode("out3on#"))
    port.write(str.encode("out5on#"))
    port.write(str.encode("out6on#"))
    time.sleep(.1)
    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))
    for i in range(50):
        port.write(str.encode(f"0,{i},0,100,0#"))
        port.write(str.encode("show#"))
        time.sleep(.01)
    port.write(str.encode("out1off#"))
    port.write(str.encode("out3off#"))
    port.write(str.encode("out5off#"))
    port.write(str.encode("out6off#"))
    port.write(str.encode("out2on#"))
    port.write(str.encode("out4on#"))
    port.write(str.encode("out6on#"))
    port.write(str.encode("out8on#"))
    time.sleep(.1)
    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))
    for i in range(50):
        port.write(str.encode(f"0,{i},0,0,100#"))
        port.write(str.encode("show#"))
        time.sleep(.01)
    port.write(str.encode("out1off#"))
    port.write(str.encode("out2off#"))
    port.write(str.encode("out3off#"))
    port.write(str.encode("out4off#"))
    port.write(str.encode("out5off#"))
    port.write(str.encode("out6off#"))
    port.write(str.encode("out7off#"))
    port.write(str.encode("out8off#"))
    time.sleep(.1)
    port.write(str.encode("clear#"))
    port.write(str.encode("show#"))

def runtest1():
    tProc = Process(target=test1, args=())
    tProc.start()