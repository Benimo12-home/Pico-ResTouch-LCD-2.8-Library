import os
from display.display import *
from machine import UART
import sys

g = Screen(ssd) #Setup screen instance
uart = UART(1, baudrate=9600) #Setup UART communication
t = Textbox() #Textbox object for the screen
t.defineTextbox(1,1,237,30, BLACK,GREY,WHITE, arial10) #Extra definition for the textbox
os.dupterm(uart, 0) #redirects output stream to uart

def serialInput(): #Displays input into the shell on the screen
    data = sys.stdin.read(1) # Reads the serial stream one character at a time
    t.append(data) #
    return data

def serialOutput(): #Displays output from the shell on the screen
    data = sys.stdout.read(1)
    t.append(data)

while True:
    serialInput()
    #serialOutput()
    g.update()