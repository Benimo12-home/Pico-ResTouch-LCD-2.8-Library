import os
import uasyncio as asyncio
from lowres.display import *
from touchscreen import *

path = os.getcwd()
UI = Screen()
T = localTouchscreen()

class Button:
    def __init__(self, dialogue, xorigin, yorigin, length, width, textcolor,fgcolor, bdcolor, show = True):
        self.show = show
        self.x = xorigin 
        self.y = yorigin
        self.dialogue = dialogue
        if self.show == True:
            UI.fillRectangle(xorigin, yorigin, length, width, fgcolor)
            UI.displayText(dialogue, textcolor, xorigin, yorigin+1)
            UI.drawRectangle(xorigin, yorigin, length, width, bdcolor)
            T.defineTouchRegion(xorigin, xorigin + length, yorigin, yorigin + width)
            UI.update()
    
    def pressed(self, textcolor = None, fgcolor = None, bdcolor = None):
        if self.show == True:
            if T.touched() == True:
                UI.fillRectangle(self.x, self.y, length, width, fgcolor)
                UI.displayText(self.dialogue, textcolor, xorigin, yorigin)
                UI.drawRectangle(self.x, self.y, length, width, bdcolor)
                UI.update()
                return True
            else:
                return False

class Window:
    def __init__(self, dialogue = path, xorigin = 0, yorigin = 0, length = 320, width = 8, show = True):
        self.show = show
        if show == True:
            UI.fillRectangle(xorigin, yorigin, length, width, TEAL)
            UI.displayText(dialogue, CYAN, xorigin, yorigin)
            CancelButton = Button("x",length - width, yorigin, width, width, WHITE, RED, BLACK)
            while True:
                if CancelButton.pressed(WHITE, ORANGE, RED) == True:
                    UI.clear()
                    UI.update()
            UI.update()
            
banner = Window()