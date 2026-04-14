#from SystemUI import Button
from lowres.display import *

g = Screen()
g.bgFill()
B = Button("PRESS", 100, 100, 64, 32, BLACK, LIGHTGREY, GREY, True)

while True:
    if B.pressed(WHITE, BLUE, BLACK) == True:
        print("WORKS!")