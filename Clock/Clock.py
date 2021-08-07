import os
import time
import datetime

from face import *
from hour import *


def split(frame):
    return [char for char in frame]

while True:   
    clockchar = ""
    clockstring = ""
    display = ""
   
    clockstring = setface()
    clockchar = split(clockstring)

    ctime = datetime.datetime.now()
    hours = int(ctime.strftime("%H"))
    minutes = int(ctime.strftime("%M"))
    seconds = int(ctime.strftime("%S"))
    #minute = int(ctime.strftime("%H:%M:%S"))

    clockchar = sethour(hours, clockchar)

    for val in clockchar: 
        display += val 

    print(display)
    print(hours)
    print(minutes)
    print(seconds)
    #print(clockchar[5])



    time.sleep(1)
    print("\033[H\033[J") 
    os.system("cls")

