from spriteDisplay.display import *
#from display import *
from sprite import *

S = Screen()
#Spritesheets need an actual existing file to be referenced.
s = Spritesheet(ssd, "SystemSprites.txt")
print(s.getCharacter(0))
print(s.getCharacter(1))
print(s.getCharacter(2))
S.bgFill((128,0,255))
S.displayText()
#ssd.fill(90)
#ssd.show()
#Palettes can be an actual file or they can use a dictionary.
s.drawSpritesheet({0:0, 1:WHITE, 2:RED, 3:YELLOW, 4:GREEN, 5:BLUE, 6:MAGENTA, 7:GREY},0)