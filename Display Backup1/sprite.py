import os

def Scroll(x, y):
    x += x
    y += y
    return [x,y]

class Spritesheet:
    def __init__(self, path):
        sprites = File(path)

class Sprite:
    def __init__(self, dev, path, xorigin, yorigin, palette, size, character): #dev = ssd
        self.x = xorigin
        self.y = yorigin
        self.size = size
        self.palette = palette
        self.character = (character+1)*(8**2) #Might change to modulo notation
        self.dev = dev
        
    def drawSprite(self, palettecolor): #Properly define palette color
        for y in range(8*(self.size+1)):
            for x in range(8*(self.size+1)):
                color = self.palette.get(palettecolor)
                self.dev.pixel((self.x +x) -1, (self.y +y) -1, color)

class Palette:
    def __init__(self, Colour0, Colour1, Colour2, Colour3, Colour4, Colour5, Colour6, Colour7): #defines the palette
        self.color0
        self.color1
        self.color2
        self.color3
        self.color4
        self.color5
        self.color6
        self.color7
        self.palette = {0:self.color0, 1:self.color1, 2:self.color2, 3:self.color3, 4:self.color4, 5:self.color5, 6:self.color6, 7:self.color7}
        #palette is a dictionary that holds 8 colors at once
    
    def getPalette(self):
        return self.palette
    
    def getColor(self, color = 0):
        return self.palette.get(color)

class Cell:
    def __init__(self, dev, xorigin, yorigin, palette, size, character):
        print("Hello World")
    
class CellMap:
    def __init__(self, size, xlimit, ylimit):
        print("Hello World")

class File:
    def __init__(self, path):
        self.path = path
    
    def readPaletteFile(self): #This read the palette file as a string from the given file destination and converts it into a list of dictionaries for use in the program
        f = open(self.path).read()
        #Split the file into 8 palette lists
        f = f.split('\n')
        #Restore each individual palette as a string to deal with whitespace
        f0 = str(f[0])
        f1 = str(f[1])
        f2 = str(f[2])
        f3 = str(f[3])
        f4 = str(f[4])
        f5 = str(f[5])
        f6 = str(f[6])
        f7 = str(f[7])
        
        #Remove the whitespace to turn the strings into lists
        f0 = f0.split(' ')
        f1 = f1.split(' ')
        f2 = f2.split(' ')
        f3 = f3.split(' ')
        f4 = f4.split(' ')
        f5 = f5.split(' ')
        f6 = f6.split(' ')
        f7 = f7.split(' ')
        
        #Turn the lists into dictionaries of integers
        f0 = {int(f0[i]): int(f0[i + 1]) for i in range(0, len(f0), 2)}
        f1 = {int(f1[i]): int(f1[i + 1]) for i in range(0, len(f1), 2)}
        f2 = {int(f2[i]): int(f2[i + 1]) for i in range(0, len(f2), 2)}
        f3 = {int(f3[i]): int(f3[i + 1]) for i in range(0, len(f3), 2)}
        f4 = {int(f4[i]): int(f4[i + 1]) for i in range(0, len(f4), 2)}
        f5 = {int(f5[i]): int(f5[i + 1]) for i in range(0, len(f5), 2)}
        f6 = {int(f6[i]): int(f6[i + 1]) for i in range(0, len(f6), 2)}
        f7 = {int(f7[i]): int(f7[i + 1]) for i in range(0, len(f7), 2)}
        
        #Recompile all dictionaries into a list of dictionaries which can then be read by the GFX Editor as palettes
        f = [f0, f1, f2, f3, f4, f5, f6, f7]
        return f
    
    def writePaletteFile(self, palette0, palette1, palette2, palette3, palette4, palette5, palette6, palette7): #This 
        f = open(self.path, "w")
        
        #Collect all given palette dictionaries and collect them into a list
        string = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (palette0, palette1, palette2, palette3, palette4, palette5, palette6, palette7)
        
        #Remove all special characters, but keep the whitespace
        string = string.replace('{', '')
        string = string.replace(':', '')
        string = string.replace('}', '')
        string = string.replace(',', '')
        f.write(string)
        f.close()
    
    def writeSpritesheet(self, spritesheet):
        f = open(self.path, "w")
        
        #Write the spritesheet as a string
        string = str(spritesheet)
        
        string = string.replace('{', '')
        string = string.replace(':', '')
        string = string.replace('}', '')
        string = string.replace(',', '')
        string = string.replace('[', '')
        string = string.replace(']', '')
        f.write(string)
        f.close()
    
    def readSpritesheet(self):
        f = open(self.path, "r")
        f = f.split('\n') #In case separate lines exist in the spritesheet file even though it should not exist in this file

#[{0:5}, {1:1}