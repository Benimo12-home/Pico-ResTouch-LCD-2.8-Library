'Ben Onime'
'Display library'
'from display import *'
't = Textbox()'
's = Screen()'

#import system functions from micropython
import os
import nanoguilib
import gc
from machine import Pin, SPI, PWM

#import basic LCD functions
from nanoguilib.color_setup import ssd # Create a display instance
from nanoguilib.nanogui import refresh, DObject, circle, fillcircle
from nanoguilib.writer import CWriter

import uasyncio as asyncio

#import colors
from nanoguilib.colors import *

#import fonts
import nanoguilib.arial10 as arial10
import nanoguilib.freesans20 as freesans20
import nanoguilib.courier20 as courier20
import nanoguilib.font6 as font6

#import GUI items
from nanoguilib.label import Label
from nanoguilib.textbox import Textbox as Text
from nanoguilib.dial import Dial, Pointer
from nanoguilib.meter import Meter

#import image display functions
import bmp_file_reader as bmpr
from sprite import *

#BL = 13
#DC = 8
#RST = 12
#MOSI = 11
#SCK = 10
#CS = 9

pdc = Pin(8, Pin.OUT, value=0)
pcs = Pin(9, Pin.OUT, value=1)
prst = Pin(15, Pin.OUT, value=1)
pbl = Pin(13, Pin.OUT, value=1)

BLACK = BLACK
GREEN = GREEN
RED = RED
LIGHTRED = LIGHTRED
BLUE = BLUE
YELLOW = YELLOW
GREY = GREY
MAGENTA = MAGENTA
CYAN = CYAN
LIGHTGREEN = LIGHTGREEN
DARKGREEN = DARKGREEN
DARKBLUE = DARKBLUE
WHITE = WHITE
#This imports when import * is called on this file.
#Prevents having to re-import nanoguilib.colors

arial10 = arial10
font6 = font6
freesans20 = freesans20
courier20 = courier20
#imports fonts to other programs when import * is called
#prevents having to re-import each individual font

gc.collect()  # Precaution before instantiating framebuf
# Max baudrate produced by Pico is 31_250_000. ST7789 datasheet allows <= 62.5MHz.
# Note non-standard MISO pin. This works, verified by SD card.
spi = SPI(1, 60_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))

#pwm = PWM(Pin(BL))
#pwm.freq(1000)
#pwm.duty_u16(32768)#max 65535
        
class Textbox:
    def __init__(self, string = '', scroll_speed = 0, orientation = 0): #initial configurations. Can be changed with below functions.
        self.nrow = 2
        self.ncol = 2
        self.width = 128
        self.nlines = 7
        self.posArg = (self.nrow, self.ncol, self.width, self.nlines)
        self.fgcolor = YELLOW
        self.bdcolor = RED
        self.bgcolor = DARKGREEN
        self.textboxArg = {'fgcolor' : self.fgcolor,
          'bdcolor' : self.bdcolor,
          'bgcolor' : self.bgcolor,
         }
        self.font = arial10
        self.wri = CWriter(ssd, self.font, verbose=False)
        self.wri.set_clip(True, True, False)
        #tb = Text(self.posArg)
        self.s = str(string)
        self.ss = str(string)
        refresh(ssd)
        if scroll_speed == None:
            scroll_speed = 0
        self.speed = scroll_speed

    def setup(self): #Legacy function meant to setup the textbox
        refresh(ssd, True)  # Initialise and clear display.
        CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
        self.wri = CWriter(ssd, self.font, verbose=False)
        self.wri.set_clip(True, True, False)
        #asyncio.run(self.main(self.s))
        #This function is not needed
    
    def defineTextbox(self, nrow=2, ncol=2, width=128, nlines=7, fgcolor=YELLOW, bdcolor=RED, bgcolor=DARKGREEN, font=arial10): #Custom definition for textbox
        self.posArg = (nrow, ncol, width, nlines)
        self.textboxArg = {'fgcolor' : fgcolor,
          'bdcolor' : bdcolor,
          'bgcolor' : bgcolor,
         }
        self.wri = CWriter(ssd, font, verbose=False)
        self.wri.set_clip(True, True, False)
        
    def displayText(self): #Given text wraps around, is displayed in textbox.
        tb = Text(self.wri, *self.posArg, clip=False, **self.textboxArg )
        tb.append(self.s, ntrim = 100, line = 0)
        refresh(ssd)
        while True:
            await asyncio.sleep(self.speed)
            if not tb.scroll(1):
                break
            refresh(ssd)
        #Legacy function, call update() instead
            
    def append(self, s = ""):
        s = str(s)
        self.s += s
        self.update()
        
    def appendLine(self, s = ""):
        s = str(s)
        self.s += "\n"+s
        self.update()
    
    def displayTextTest(self): #Function that tests the textbox capabilities
        s = 'Musings of a Madman are the things that we convince ourselves are true but really arent. The quick brown fox will always jump over the lazy dog because it happened once, it will happen again. I am so sorry!'
        tb = Text(self.wri, *self.posArg, clip=False, **self.textboxArg)
        tb.append(s, ntrim = 100, line = 0)
        refresh(ssd)
        while True:
            await asyncio.sleep(self.speed)
            if not tb.scroll(1):
                break
            refresh(ssd)
        #Legacy function, call updateTest() instead
            
    def displayTextClip(self): #Given text clips away
        tb = Text(self.wri, *self.posArg, clip=True, **self.textboxArg )
        tb.append(self.ss, ntrim = 100)
        refresh(ssd)
        while True:
            await asyncio.sleep(self.speed)
            if not tb.scroll(1):
                break
            refresh(ssd)
        #Legacy function, call updateClip() instead
        
    def displayLen(self):
        tb = Text(self.wri, *self.posArg, clip=True, **self.textboxArg )
        #tb.append(self.ss, ntrim = 100)
        refresh(ssd)
        for s in self.ss:
            tb.append(s, ntrim = 100) # Default line=None scrolls to show most recent
            refresh(ssd)
            await asyncio.sleep(self.speed)
        return len(self.ss)
        #Legacy function, call updateLen() instead
                
    def main(self): #main function for displayText
        await self.displayText()

    def mainClip(self): #main function for displayTextClip
        await self.displayTextClip()
        
    def mainTest(self): #main function for displayTextTest
        await self.displayTextTest()
        
    def mainLen(self): #main function for displayLen
        await self.displayLen()
        
    def update(self): #call to display text in textbox, wrapped
        asyncio.run(self.main())
        
    def updateClip(self): #call to display text in textbox, clipped
        asyncio.run(self.mainClip())
    
    def updateTest(self): #call to display test text
        asyncio.run(self.mainTest())
        
    def updateLen(self): #call to display text with all letters written in separate lines
        asyncio.run(self.mainLen())
 
class Screen():
    def __init__(self, orientation = 0): #0 for portrait, 1 for mirror mode portrait, 2 for down portrait, 3 for down portrait mirror mode, etc.
        gc.collect()
        self.ssd = ssd
        if orientation == 0: #Portrait
            self.ssd = SSD(spi, height=320, width=240, disp_mode=0, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 1: #Mirror portrait
            self.ssd = SSD(spi, height=320, width=240, disp_mode=1, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 2: #Down Portrait
            self.ssd = SSD(spi, height=320, width=240, disp_mode=2, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 3: #Mirror Down Portrait
            self.ssd = SSD(spi, height=320, width=240, disp_mode=3, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 4: #Landscape
            self.ssd = SSD(spi, height=240, width=320, disp_mode=4, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 5: #Mirror Landscape
            self.ssd = SSD(spi, height=240, width=320, disp_mode=5, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 6: #Down Landscape
            self.ssd = SSD(spi, height=240, width=320, disp_mode=6, dc=pdc, cs=pcs, rst=prst)
        elif orientation == 7: #Mirror Down Landscape
            self.ssd = SSD(spi, height=240, width=320, disp_mode=7, dc=pdc, cs=pcs, rst=prst)
        else: #Null case
            self.ssd = SSD(spi, height=320, width=240, disp_mode=0, dc=pdc, cs=pcs, rst=prst)
        self.orientation = orientation
        self.orientation = orientation
        self.lcd_display = ssd
        self.font = arial10
        self.wri = CWriter(ssd, self.font, verbose=False)
        self.wri.set_clip(True, True, False)
            
    def clear(self): #Clears the screen when run
        refresh(ssd, True)
    
    'Shape functions'
    def drawRectangle(self, x = 0, y = 0, width = 50, length = 50, color = BLUE): #Draws the outline of a rectangle
        ssd.rect(x, y, width, length, color)
        
    def fillRectangle(self, x = 0, y = 0, width = 60, length = 50, color = YELLOW): #Draws a filled rectangle
        ssd.fill_rect(x, y, width, length, color)
        
    def drawCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws the outline of a circle with origin at the diagonal of a box
        circle(self.lcd_display, x+radius, y+radius, radius, color)
        
    def fillCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws a filled circle with origin at the diagonal of a box
        fillcircle(self.lcd_display, x+radius, y+radius, radius, color)
        
    def drawCenterCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws the outline of a circle with origin at the radius
        circle(self.lcd_display, x, y, radius, color)
        
    def fillCenterCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws a filled circle with origin at the radius
        fillcircle(self.lcd_display, x, y, radius, color)
        
    def drawLine(self, xorigin = 60, yorigin = 90, xend = 320, yend = 240, color = BLACK): #Draws a line from point a to point b (from origin point to end point)
        ssd.line(xorigin, yorigin, xend, yend, color)
    
    def drawHorizontalLine(self, xorigin = 0, y = 90, xend = 320, color = GREEN):
        ssd.hline(xorigin, y, xend, color)
        
    def drawVerticalLine(self, x = 60, yorigin = 90, yend = 150, color = BLUE):
        ssd.vline(x, yorigin, yend, color)
    
    'Image functions'
    def to_color(self,red, green, blue, brightness = 1.0): #Color correction for image
        # Convert from 8-bit colors for red, green, and blue to 5-bit for blue and red and 6-bit for green.
        b = int((blue/255.0) * (2 ** 2 - 1) * brightness)
        r = int((red/255.0) * (2 ** 4 - 1) * brightness)
        g = int((green/255.0) * (2 ** 7 - 1) * brightness)
        #b = int(BLUE * (2 ** 5 - 1) * brightness)
        #r = int(RED * (2 ** 5 - 1) * brightness)
        #g = int(GREEN * (2 ** 8 - 1) * brightness)
    
        # Shift the 5-bit blue and red to take the correct bit positions in the final color value
        bs = b << 8
        rs = r << 3
    
        # Shift the 6-bit green value, properly handling the 3 bits that overlflow to the beginning of the value
        g_high = g >> 3
        g_low = (g & 0b000111) << 13
        gs = g_high + g_low
    
        # Combine together the red, green, and blue values into a single color value
        color = bs + rs + gs
    
        return color
    
    def read_bmp_to_buffer(self, lcd_display, file_handle): #reads the .bmp data to the buffer, using ALL available processing power
        reader = bmpr.BMPFileReader(file_handle)
    
        for row_i in range(0, reader.get_height()):
            row = reader.get_row(row_i)
            for col_i, color in enumerate(row):
                #lcd_display.pixel(col_i, row_i, self.to_color(color.red, color.green, color.blue))
                lcd_display.pixel(col_i, row_i, self.to_color(color.red, color.green, color.blue))
                
    def displayImage(self, path = ""):  #Displays image from the given path
        with open(path, "rb") as input_stream:
            self.read_bmp_to_buffer(self.lcd_display, input_stream)
        #self.clear() must be called before using this function
    
    'GUI functions'
    def defineGUI(self, nrow = 2, ncol = 2, width = 128, nlines = 7, font = arial10): #Defines all proceeding GUI functions
        self.posArg = (nrow, ncol, width, nlines)
        self.wri = CWriter(self.ssd, font, verbose=False)
        self.wri.set_clip(True, True, False)
        #Must be called or else GUI functions will not be displayed
            
    def drawDial(self, string = "Dial", x = 2, y = 2): #Draws a dial object with the below specifications
        dial = Dial(self.wri, x, y, height = 75, ticks = 12, bdcolor = None, label=120, pip=False)
        dial.text(str(string))
        dial.show()
        return dial
    
    def drawCompassDial(self, string = "Compass", x = 2, y= 2): #Draws a compass dial object with the below specifications
        dial = Dial(self.wri, x, y, height = 75, ticks = 720, bdcolor = None, label=120, pip=False)
        dial.text(str(string))
        dial.show()
        return dial
    
    def drawPointer(self):
        pointer = Pointer(dial)
    
    def drawLabel(self, row = 2, col = 2, string = 'Insert Text Here', fgcolor=None, bgcolor=None, bdcolor=False): #Draws a label object
        label = Label(self.wri, row, col, str(string), False, fgcolor, bgcolor, bdcolor)
    
    'Miscellaneous Functions'
    def displayText(self, string = 'Insert Text Here',color = BLACK, x = 90, y = 70): #Displays Text in specified area
        ssd.text(str(string), x, y, color)
        
    def bgFill(self, color = WHITE): #Fills the screen with the specified color
        ssd.fill(color)
        
    def update(self): #Shows all changes made to the screen
        ssd.show()