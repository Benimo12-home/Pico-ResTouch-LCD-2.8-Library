from sprite import *
#from display import Screen, Textbox
from drivers.st7789.st7789_8bit import *
import gc
from machine import Pin, SPI, PWM

SSD = ST7789
spi = SPI(1, 60_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))

pdc = Pin(8, Pin.OUT, value=0)
pcs = Pin(9, Pin.OUT, value=1)
prst = Pin(15, Pin.OUT, value=1)
pbl = Pin(13, Pin.OUT, value=1)

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


