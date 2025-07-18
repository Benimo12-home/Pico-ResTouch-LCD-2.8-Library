import os
from lowres.display import *
from touchscreen import *
from sprite import *
from touch_setup import *

g = Screen()
#Initializes the screen as landscape
#t = localTouchscreen()

#Default palette configurations in case palette file is missing or damaged
defpalette0 = {0:BLACK, 1:WHITE, 2:RED, 3:YELLOW, 4:GREEN, 5:BLUE, 6:MAGENTA, 7:GREY}
defpalette1 = {0:BLACK, 1:WHITE, 2:GREY, 3:BLACK, 4:LIGHTRED, 5:CYAN, 6:LIGHTGREEN, 7:DARKBLUE}
defpalette2 = {0:BLACK, 1:YELLOW, 2:LIGHTRED, 3:RED, 4:DARKBLUE, 5:DARKGREEN, 6:LIGHTGREEN, 7:MAGENTA}
defpalette3 = {0:BLACK, 1:BLACK, 2:GREY, 3:WHITE, 4:0xFFFF, 5:0xBE5103, 6:0xCCCC, 7:0x12C675}
defpalette4 = {0:BLACK, 1:BLACK, 2:GREY, 3:WHITE, 4:BLACK, 5:BLACK, 6:BLACK, 7:BLACK}
defpalette5 = {0:BLACK, 1:BLACK, 2:GREY, 3:WHITE, 4:BLACK, 5:BLACK, 6:BLACK, 7:BLACK}
defpalette6 = {0:BLACK, 1:BLACK, 2:GREY, 3:WHITE, 4:BLACK, 5:BLACK, 6:BLACK, 7:BLACK}
defpalette7 = {0:BLACK, 1:BLACK, 2:GREY, 3:WHITE, 4:BLACK, 5:BLACK, 6:BLACK, 7:BLACK}

def testLayout():
    g.bgFill(LIGHTGREY)
    g.fillRectangle(16,16, 64, 64, BLACK)#Exact coordinates to be used for actual sprite display box later
    g.update()
    for i in range(9): #Exact coordinates to be used for actual sprite display box later
        g.drawVerticalLine(16+(i*8), 16, 64, RED)
        g.drawHorizontalLine(16, 16+(i*8), 64, RED)
        g.update()
    
    g.fillRectangle(16, 96, 288, 128, BLACK) #Exact coordinates to be used for spritesheet display box
    g.fillRectangle(88, 16, 8, 64, BLACK) #Exact coordinates to be used for Palette Display Box
    g.update()

def getPalette(path = "palette.txt"):
    f = File(path)
    g.fillRectangle(88, 16, 8, 64, BLACK)
    try:
        h = open(path, "r")
        palettesheet = f.readPaletteFile()
    except  OSError:
        print("File", path, "could not be opened")
        print("Creating", path,"...")
        f.writePaletteFile(defpalette0, defpalette1, defpalette2, defpalette3, defpalette4, defpalette5, defpalette6, defpalette7)
        getPalette(path)
        palettesheet = f.readPaletteFile()
    except:
        if h == None:
            print("Writing into", path, "...")
            f.writePaletteFile(defpalette0, defpalette1, defpalette2, defpalette3, defpalette4, defpalette5, defpalette6, defpalette7)
            palettesheet = f.readPaletteFile()
    else:
        print ("Checking", path, "...")
        f.readPaletteFile()
        #print(f.readPaletteFile())
        palettesheet = f.readPaletteFile()
    return palettesheet

def displayPalette(palettesheet):
    bufPalette0 = palettesheet[0]
    bufPalette1 = palettesheet[1]
    bufPalette2 = palettesheet[2]
    bufPalette3 = palettesheet[3]
    bufPalette4 = palettesheet[4]
    bufPalette5 = palettesheet[5]
    bufPalette6 = palettesheet[6]
    bufPalette7 = palettesheet[7]
    bufPaletteList = palettesheet
    i = 0
    if i == 0:
        for color in bufPalette0:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette0.get(color))
            g.update()
    elif i == 1:
        for color in bufPalette1:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette1.get(color))
            g.update()
    elif i == 2:
        for color in bufPalette2:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette2.get(color))
            g.update()
    elif i == 3:
        for color in bufPalette3:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette3.get(color))
            g.update()
    elif i == 4:
        for color in bufPalette4:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette4.get(color))
            g.update()
    elif i == 5:
        for color in bufPalette5:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette5.get(color))
            g.update()
    elif i == 6:
        for color in bufPalette6:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette6.get(color))
            g.update()
    elif i == 7:
        for color in bufPalette7:
            g.fillRectangle(88, 16 + ((color)*8), 8, 8, bufPalette7.get(color))
            g.update()
            
testLayout()
displayPalette(getPalette("palette.txt"))
