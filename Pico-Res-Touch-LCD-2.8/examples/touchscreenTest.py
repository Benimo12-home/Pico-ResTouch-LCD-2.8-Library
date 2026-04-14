#from touch_setup import *
#from touch.touch import *
from lowres.display import *

t = ABCTouch(ssd, tpad)
g = Screen()
g.bgFill()
while True:
    if t.poll() == True:
        g.bgFill()
        g.displayText("Touched!")
        print("Touched!")
    else:
        g.bgFill()
        g.displayText("No Fingers?")
    g.update()
#Touching the screen prints "Touched!" in the shell
#The entire screen acts as a touch panel