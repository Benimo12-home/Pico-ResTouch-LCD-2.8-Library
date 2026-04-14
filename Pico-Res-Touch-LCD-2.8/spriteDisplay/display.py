#Libraries to be used for colors
from machine import Pin, SPI
from drivers.st7789.st7789_8bit import *
from nanoguilib.colors import *
from sprite import *

from nanoguilib.nanogui import refresh

#import image display functions
import bmp_file_reader as bmpr
from sprite import *

#SSD definitions because other SSDs are incompatible with this one
pdc = Pin(8, Pin.OUT, value=0)
pcs = Pin(9, Pin.OUT, value=1)
prst = Pin(15, Pin.OUT, value=1)
pbl = Pin(13, Pin.OUT, value=1)

SSD = ST7789
spi = SPI(1, 60_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))

ssd = SSD(spi, height=320, width=240, disp_mode=0, dc=pdc, cs=pcs, rst=prst)

def colorconvert(color): #Converts between rgb tuples and rgb hexadecimals
    if isinstance(color, tuple): # Convert tuple to hexadecimal
        color = ("0x{:02x}{:02x}{:02x}".format(color[0],color[1],color[2]))
        return color
    else: # Convert into tuple
        color = str(color)
        color = color.replace("0x", "")
        return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

#Color definitions for compatibility purposes
BLACK = colorconvert((0, 0, 0))
GREEN = colorconvert((0, 255, 0))
RED = colorconvert((255, 0, 0))
LIGHTRED = colorconvert((140, 0, 0))
BLUE = colorconvert((0, 0, 255))
YELLOW = colorconvert((255, 255, 0))
GREY = colorconvert((100, 100, 100))
MAGENTA = colorconvert((255, 0, 255))
CYAN = colorconvert((0, 255, 255))
LIGHTGREEN = colorconvert((0, 100, 0))
DARKGREEN = colorconvert((0, 80, 0))
DARKBLUE = colorconvert((0, 0, 80))
TEAL = colorconvert((0, 128, 128))
WHITE = colorconvert((255, 255, 255))
LIGHTGREY = colorconvert((211, 211, 211))

if hasattr(SSD, 'lut'):
    BLACK = create_color(0, 0, 0, 0)
    GREEN = create_color(1, 0, 255, 0)
    RED = create_color(2, 255, 0, 0)
    LIGHTRED = create_color(3, 140, 0, 0)
    BLUE = create_color(4, 0, 0, 255)
    YELLOW = create_color(5, 255, 255, 0)
    GREY = create_color(6, 100, 100, 100)
    MAGENTA = create_color(7, 255, 0, 255)
    CYAN = create_color(8, 0, 255, 255)
    LIGHTGREEN = create_color(9, 0, 100, 0)
    DARKGREEN = create_color(10, 0, 80, 0)
    DARKBLUE = create_color(11, 0, 0, 90)
    ORANGE = create_color(12, 255, 165, 0)
    TEAL = create_color(13, 0, 128, 128)
    LIGHTGREY = create_color(14, 211, 211, 211)
    # 12, 13, 14 free for user definition
    WHITE = create_color(15, 255, 255, 255)
 
class Screen():
    def __init__(self, orientation = 0): #0 for portrait, 1 for mirror mode portrait, 2 for down portrait, 3 for down portrait mirror mode, etc.
        gc.collect() 
        self.ssd = ssd
        self.orientation = orientation
        self.orientation = orientation
        self.lcd_display = self.ssd
            
    def clear(self): #Clears the screen when run
        refresh(ssd, True)
    
    'Shape functions'
    def drawRectangle(self, x = 0, y = 0, width = 50, length = 50, color = BLUE): #Draws the outline of a rectangle
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.rect(x, y, width, length, self.ssd.rgb(color[0],color[1],color[2]))
        
    def fillRectangle(self, x = 0, y = 0, width = 60, length = 50, color = YELLOW): #Draws a filled rectangle
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.fill_rect(x, y, width, length, self.ssd.rgb(color[0],color[1],color[2]))
        
    def drawCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws the outline of a circle with origin at the diagonal of a box
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        circle(self.lcd_display, x+radius, y+radius, radius, self.ssd.rgb(color[0],color[1],color[2]))
        
    def fillCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws a filled circle with origin at the diagonal of a box
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.fillcircle(self.lcd_display, x+radius, y+radius, radius, self.ssd.rgb(color[0],color[1],color[2]))
        
    def drawCenterCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws the outline of a circle with origin at the radius
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        circle(self.lcd_display, x, y, radius, self.ssd.rgb(color[0],color[1],color[2]))
        
    def fillCenterCircle(self, x = 0, y = 0, radius = 7, color = GREEN): #Draws a filled circle with origin at the radius
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        fillcircle(self.lcd_display, x, y, radius, self.ssd.rgb(color[0],color[1],color[2]))
        
    def drawLine(self, xorigin = 60, yorigin = 90, xend = 320, yend = 240, color = BLACK): #Draws a line from point a to point b (from origin point to end point)
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.line(xorigin, yorigin, xend, yend, self.ssd.rgb(color[0],color[1],color[2]))
    
    def drawHorizontalLine(self, xorigin = 0, y = 90, xend = 320, color = GREEN):
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.hline(xorigin, y, xend, self.ssd.rgb(color[0],color[1],color[2]))
        
    def drawVerticalLine(self, x = 60, yorigin = 90, yend = 150, color = BLUE):
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.vline(x, yorigin, yend, self.ssd.rgb(color[0],color[1],color[2]))
    
    'Image functions'
    def to_color(self,red, green, blue, brightness = 1.0): #Color correction for image
        # Convert from 8-bit colors for red, green, and blue to 5-bit for blue and red and 6-bit for green.
        b = int((blue/255.0) * (2 ** 4 - 1) * brightness)
        r = int((red/255.0) * (2 ** 4 - 1) * brightness)
        g = int((green/255.0) * (2 ** 6 - 1) * brightness)
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
    
    'Miscellaneous Functions'
    def displayText(self, string = 'Insert Text Here',color = BLACK, x = 90, y = 70): #Displays Text in specified area
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.text(str(string), x, y, self.ssd.rgb(color[0],color[1],color[2]))
        
    def bgFill(self, color = WHITE): #Fills the screen with the specified color
        if isinstance(color, tuple) == False:
            color = colorconvert(color)
        self.ssd.fill(self.ssd.rgb(color[0],color[1],color[2]))
        
    def update(self): #Shows all changes made to the screen
        self.ssd.show()
