"Ben Onime"
"Touchscreen class and test"
"Library for touchscreen functions"
'from touchscreen import *'
't = localTouchscreen()'

import usb.device
import nanoguilib
import time
from usb.device.mouse import MouseInterface #Mouse library
#from main_2inch8 import LCD_2inch8 as lcd
from touch_setup import *
from touch.touch import *
from gui.core.tgui import touch as t
#from touch.check import *
#from nanoguilib.color_setup import ssd as lcd #LCD class which will be used to enable touchscreen functionality

m = MouseInterface()
#t = ABCTouch(ssd, tpad)

class localTouchscreen: #Defines the touchscreen to only be used by the microcontroller and not as a USB-HID device
    def __init__(self):
        print("Touchscreen enabled") #A message to tell you that the object works as intended and as filler so that this program doesn't stop.
    
    def touch_x(self): #Returns the x pixel position on the screen
        return t.col
    
    def touch_y(self): #Returns the y pixel position on the screen
        return t.row

    def defineTouchRegion(self ,xorigin, xend, yorigin, yend): #This function was intended as a definition for button instances but it is currently useless.
        t.init(xend - xorigin, yend - yorigin, xorigin, yorigin, xend, yend, 0, xend - xorigin, yend - yorigin)
        if t.poll() == True:
            if xorigin >= t._x >= xend and yorigin  >= y._x >= yend:
                return True
            else:
                return False
        
    def touched(self): #Checks if the screen has been touched but the function is written as a loop
        while t.poll() == True:
            return True
        return False
    
    def tap(self): #Checks if the screen has been touched but the function is written as a conditional
        if t.poll() == True:
            return True
        else:
            return False

class USBTouchscreen:
    def __init__(self):
        usb.device.get().init(m, builtin_driver=True) #This is for a USB-CDC repl. Comment out this line if false
        while not m.is_open():
            print("Null")
            time.sleep_ms(100)
        
    def touch_x(self): #returns x coordinate of where is touched and moves the mouse accordingly
        while t.poll() != False:
            m.move_by(t._x, 0)
            return t._x
        
    def touch_y(self): #returns y coordinate of where is touched and moves the mouse accordingly
        while t.poll() != False:
            m.move_by(0, t._y)
            return t._y
        
    def touch_array(self): #moves the mouse to the specified area that is touched and returns the coordinates as an array
        while t.poll() != False:
            m.move_by(t._x, t._y)
            return t._x, t._y
    
    def tap(self): #right-clicks the mouse upon the screen being tapped
        if t.poll() == True:
            m.click_right(True)
            time.sleep_ms(200)
            return True
        else:
            m.click_right(False)
            return False
        
    def hold(self): #holds the right-click button as the screen is being held
        while t.poll() != False:
            m.click_right(True)
            return self.touch
        m.click_right(False)
    
    def swipe(self): #right-clicks and moves the mouse simultaneously as the screen is being touched
        while t.poll() != False:
            m.move_by(self.touch[0], self.touch)
            m.click_right(True)
            return self.touch[0] and self.touch[1]
        m.click_right(False)
        
    def select(self): #holds the left-click button as the screen is being held
        while t.poll() != False:
            m.click_left(True)
        m.click_left(False)