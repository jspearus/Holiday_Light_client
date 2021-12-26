import datetime
from multiprocessing import Process
import sys
import os
import time
import platform
import serial
from serial.serialutil import Timeout
from advent import runAdvent
from newyear import runNewYear

if platform.system() == "Linux":
    port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
elif platform.system() == "Windows":
    port = serial.Serial("COM15", baudrate=115200, timeout=3.0)
pass

def snow():
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
    for i in range(24):
        port.write(str.encode(f"1,{i},200,200,200#"))
        port.write(str.encode("show1#"))
        time.sleep(.01)

    for i in range(50, -2, -1):
        port.write(str.encode(f"2,{i+1},0,0,0#"))
        port.write(str.encode(f"2,{i},100,100,100#"))
        port.write(str.encode(f"3,{i+1},0,0,0#"))
        port.write(str.encode(f"3,{i},100,100,100#"))
        port.write(str.encode(f"4,{i+1},0,0,0#"))
        port.write(str.encode(f"4,{i},100,100,200#"))
        port.write(str.encode(f"5,{i+1},0,0,0#"))
        port.write(str.encode(f"5,{i},100,100,100#"))
        port.write(str.encode("show#"))
        time.sleep(.2)
    for i in range(50, -2, -1):
        port.write(str.encode(f"2,{i+1},0,0,0#"))
        port.write(str.encode(f"2,{i},100,100,100#"))
        port.write(str.encode(f"3,{i+1},0,0,0#"))
        port.write(str.encode(f"3,{i},100,100,100#"))
        port.write(str.encode(f"4,{i+1},0,0,0#"))
        port.write(str.encode(f"4,{i},100,100,200#"))
        port.write(str.encode(f"5,{i+1},0,0,0#"))
        port.write(str.encode(f"5,{i},100,100,100#"))
        port.write(str.encode("show#"))
        time.sleep(.2)
    for i in range(50, -2, -1):
        port.write(str.encode(f"2,{i+1},0,0,0#"))
        port.write(str.encode(f"2,{i},100,100,100#"))
        port.write(str.encode(f"3,{i+1},0,0,0#"))
        port.write(str.encode(f"3,{i},100,100,100#"))
        port.write(str.encode(f"4,{i+1},0,0,0#"))
        port.write(str.encode(f"4,{i},100,100,200#"))
        port.write(str.encode(f"5,{i+1},0,0,0#"))
        port.write(str.encode(f"5,{i},100,100,100#"))
        port.write(str.encode("show#"))
        time.sleep(.2)
    time.sleep(2)
    runNewYear()

def runSnow():
    p = Process(target=snow, args=())
    p.start()

def rain():
    day = datetime.date.today()
    port.write(str.encode("out1off#"))
    port.write(str.encode("out3off#"))
    port.write(str.encode("out5off#"))
    port.write(str.encode("out7off#"))
    time.sleep(.5)
    port.write(str.encode("out2on#"))
    time.sleep(.5)
    port.write(str.encode("out4on#"))
    time.sleep(.5)
    port.write(str.encode("out6on#"))
    time.sleep(.5)
    port.write(str.encode("out8on#"))
    time.sleep(.5)
    for i in range(24):
        port.write(str.encode(f"1,{i},0,0,200#"))
        port.write(str.encode("show1#"))
        time.sleep(.01)

    for i in range(50, -2, -1):
        port.write(str.encode(f"2,{i+1},0,0,0#"))
        port.write(str.encode(f"2,{i},0,0,150#"))
        port.write(str.encode(f"3,{i+1},0,0,0#"))
        port.write(str.encode(f"3,{i},0,0,150#"))
        port.write(str.encode(f"4,{i+1},0,0,0#"))
        port.write(str.encode(f"4,{i},0,0,150#"))
        port.write(str.encode(f"5,{i+1},0,0,0#"))
        port.write(str.encode(f"5,{i},0,0,150#"))
        port.write(str.encode("show#"))
        time.sleep(.2)
    time.sleep(2)
    for i in range(50, -2, -1):
        port.write(str.encode(f"2,{i+1},0,0,0#"))
        port.write(str.encode(f"2,{i},0,0,150#"))
        port.write(str.encode(f"3,{i+1},0,0,0#"))
        port.write(str.encode(f"3,{i},0,0,150#"))
        port.write(str.encode(f"4,{i+1},0,0,0#"))
        port.write(str.encode(f"4,{i},0,0,150#"))
        port.write(str.encode(f"5,{i+1},0,0,0#"))
        port.write(str.encode(f"5,{i},0,0,150#"))
        port.write(str.encode("show#"))
        time.sleep(.2)
    time.sleep(2)
    for i in range(50, -2, -1):
        port.write(str.encode(f"2,{i+1},0,0,0#"))
        port.write(str.encode(f"2,{i},0,0,150#"))
        port.write(str.encode(f"3,{i+1},0,0,0#"))
        port.write(str.encode(f"3,{i},0,0,150#"))
        port.write(str.encode(f"4,{i+1},0,0,0#"))
        port.write(str.encode(f"4,{i},0,0,150#"))
        port.write(str.encode(f"5,{i+1},0,0,0#"))
        port.write(str.encode(f"5,{i},0,0,150#"))
        port.write(str.encode("show#"))
        time.sleep(.2)
    time.sleep(2)
    runNewYear()

def runRain():
    p = Process(target=rain, args=())
    p.start()