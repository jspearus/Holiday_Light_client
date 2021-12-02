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
    port.write(str.encode("out1on#"))
    time.sleep(1)
    port.write(str.encode("out3on#"))
    time.sleep(1)
    port.write(str.encode("out5on#"))
    time.sleep(1)
    port.write(str.encode("out7on#"))
    time.sleep(1)
    port.write(str.encode("out2on#"))
    time.sleep(1)
    port.write(str.encode("out4on#"))
    time.sleep(1)
    port.write(str.encode("out6on#"))
    time.sleep(1)
    port.write(str.encode("out8on#"))
    time.sleep(2)
    for i in range(50):
        port.write(str.encode(f"2,{i},100,0,0#"))
        port.write(str.encode("show#"))
        time.sleep(.1)
    time.sleep(1)
    for i in range(50):
        port.write(str.encode(f"3,{i},0,100,0#"))
        port.write(str.encode("show#"))
        time.sleep(.1)
    time.sleep(1)
    for i in range(50):
        port.write(str.encode(f"4,{i},0,0,100#"))
        port.write(str.encode("show#"))
        time.sleep(.1)
    time.sleep(1)
    for i in range(50):
        port.write(str.encode(f"5,{i},50,50,50#"))
        port.write(str.encode("show#"))
        time.sleep(.1)
    testTop()

def treeOff():
    for i in range(24):
        port.write(str.encode(f"1,{i},200,0,0#"))
        port.write(str.encode("show1#"))
        time.sleep(.07)
    for i in range(50, -1, -1):
        port.write(str.encode(f"0,{i},0,0,0#"))
        port.write(str.encode("show#"))
        time.sleep(.1)
    port.write(str.encode("out1off#"))
    time.sleep(.5)
    port.write(str.encode("out2off#"))
    time.sleep(.5)
    port.write(str.encode("out3off#"))
    time.sleep(.5)
    port.write(str.encode("out4off#"))
    time.sleep(.5)
    port.write(str.encode("out5off#"))
    time.sleep(.5)
    port.write(str.encode("out6off#"))
    time.sleep(.5)
    port.write(str.encode("out7off#"))
    time.sleep(.5)
    port.write(str.encode("out8off#"))
    for i in range(24):
        port.write(str.encode(f"1,{i},0,0,0#"))
        port.write(str.encode("show1#"))
        time.sleep(.07)

def testTop():
    for i in range(24):
        port.write(str.encode(f"1,{i},100,0,0#"))
        port.write(str.encode("show1#"))
        time.sleep(.2)
    time.sleep(5)
    for i in range(24):
        port.write(str.encode(f"1,{i},0,100,0#"))
        port.write(str.encode("show1#"))
        time.sleep(.2)
    time.sleep(5)
    for i in range(24):
        port.write(str.encode(f"1,{i},0,0,100#"))
        port.write(str.encode("show1#"))
        time.sleep(.2)
    time.sleep(5)
    port.write(str.encode("clear1#"))
    port.write(str.encode("show1#"))


def runTestTop():
    tProc = Process(target=testTop, args=())
    tProc.start()

def runTest1():
    tProc = Process(target=test1, args=())
    tProc.start()

def runTreeOff():
    tProc = Process(target=treeOff, args=())
    tProc.start()