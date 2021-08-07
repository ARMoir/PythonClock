import os
import colorama
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def setface():
    clockstring = ""
    clockstring = clockstring + "   ~-------------~    " + chr(10) 
    clockstring = clockstring + " ('..'11..12..1'..')  " + chr(10)
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :10            2: | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :9      @      3: | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + "| :8             4: | " + chr(10);
    clockstring = clockstring + "| :               : | " + chr(10);
    clockstring = clockstring + " ('..'7...6...5'..')  " + chr(10);
    clockstring = clockstring + "   ~-------------~    " + chr(10);
    return clockstring

def split(word):
    return [char for char in word]

while 1 == 1:
    clockstring = setface()
    clockchar = split(clockstring)
    print(clockstring)
    print(clockchar[5])

# sleep for 2 seconds after printing output
    sleep(2)
    print("\033[H\033[J") 

