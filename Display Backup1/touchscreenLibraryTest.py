from touchscreen import *

t = localTouchscreen()

while True:
    if t.tap() == True:
        print ("Touched!")