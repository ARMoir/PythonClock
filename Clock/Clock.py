import os
import time
import datetime

from face import *


def split(frame):
    return [char for char in frame]

while True:   
    clockchar = ""
    clockstring = ""
    display = ""
   
    clockstring = setface()
    clockchar = split(clockstring)

    ctime = datetime.datetime.now()
    hours = ctime.strftime("%H")
    minutes = ctime.strftime("%M")
    seconds = ctime.strftime("%S")
    minute = ctime.strftime("%H:%M:%S")

    print(clockstring)
    print(hours)
    print(minutes)
    print(seconds)
    #print(clockchar[5])

    time.sleep(1)
    print("\033[H\033[J") 
    os.system("cls")

