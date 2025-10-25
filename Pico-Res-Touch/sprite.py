def Scroll(x, y):
    x += x
    y += y
    return [x,y]

def rgbconvert(hex): #Transforms hexadecimal to rgb
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

class Spritesheet:
    def __init__(self, dev, path):
        self.dev = dev
        sprites = File(path)
        self.spritesheet = sprites.readSpritesheet()
    
    def getCharacter(self, character):
        elements = []
        for char in self.spritesheet:
            if char >= character*64 and char <= ((character+1)*64)-1:
                elements.append(self.spritesheet[char])
        return elements #Should return up to 64 elements in a list
    
    def drawCharacter(self, character, palette, x = 0, y = 0):
        x_index = x-x #creates an index for a matrix loop
        y_index = y-y #creates an index for a matrix loop
        pixel = 0 #Counter for the function. It also tells the Pico which pixel is to be filled
        colorkeys = {v: k for k, v in palette.items()}
        for y_index in range(8): #For the y_coordinate
            for x_index in range(8): #For the x-coordinate
                color = palette.get(self.getCharacter(character)[pixel]) #Fetches the specified color from the palette
                colorkey = colorkeys.get(self.getCharacter(character)[pixel]) #Fetches the specified color from the palette
                if color != 0: #Make color 0 transparent
                    if isinstance(color, int) == True:
                        if 0 <= color <= 15: #If the color from the palette returns a default color, perform no calculations
                            self.dev.pixel((x+x_index), (y+y_index), color) #Plot the pixel based on all prescripted instructions
                        else: #if the read color is a number that is not a default color
                            color = hex(color) #Turn the color into a hexadecimal value
                            color = str(color)
                            color = color.replace("0x", "")
                            color = rgbconvert(color)
                            self.dev.pixel((x+x_index), (y+y_index), self.dev.rgb(color[0], color[1], color[2])) #Plot the pixel based on all prescripted instructions
                    elif isinstance(color, tuple) == True: #If the read color is a tuple
                        self.dev.pixel((x+x_index), (y+y_index), self.dev.rgb(color[0], color[1], color[2]))
                    else:
                        color = str(color)
                        color = color.replace("0x", "")
                        color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
                        self.dev.pixel((x+x_index), (y+y_index), self.dev.rgb(color[0], color[1], color[2])) #Plot the pixel based on all prescripted instructions
                if 0 <= pixel + 1 < len(self.getCharacter(character)): #Ignore pixel if the array is finished
                    pixel +=1 #Increase the counter
        return self #Return the character
        #This function will not draw the character but only calculate it based on all previous instructions.
    
    def drawSpritesheet(self, palette, character = 0, x = 0, y = 0, nrow = 4, ncol = 16): #Displays all elements of the spritesheet on the screen
        x_index = x-x #Index for loop
        y_index = y-y #Index for loop
        charcounter = character #Charcounter starts at the given character
        for y_index in range(nrow):
            for x_index in range(ncol):
                if (0 <= character < int(round(len(self.spritesheet)/64))) and (charcounter == character):
                    self.drawCharacter(character, palette, x+(x_index*8), y+(y_index*8))
                    character +=1
                    charcounter +=1
                else:
                    character = 0
        self.dev.show()

class Sprite:
    def __init__(self, dev, path, xorigin, yorigin, palette, character): #dev = ssd
        self.x = xorigin
        self.y = yorigin
        self.palette = palette
        self.character = character
        self.dev = dev
        s = Spritesheet(dev, path)
        
    def drawSprite(self):
        s.drawCharacter(self.character, self.palette, self.x, self.y)

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
        f = open(self.path).read()
        f = str(f) #Turn the read data into a string
        f = f.split('\n') #If there is separate lines, put them into one line as a list. (This could be useful but its mostly for error handling)
        f = str(f) #Turn the list into a string
        f = f.replace(',', '')
        f = f.replace('[', '')
        f = f.replace(']', '')
        f = f.replace('"', '')
        f = f.replace('\\r', '')
        f = f.replace("'", '') #Remove all garbage data in the string.
        f = f.split(' ') #Turn the string into a list
        f = list(filter(None, f)) #Remove all blank whitespace remaining from the list
        f = {int(f[i]): int(f[i + 1]) for i in range(0, len(f), 2)}#Turn the list into a dictionary
        return f #Return a dictionary of elements
     
#[{0:5}, {1:1}