#Matthew Suriawinata
#4/23/18
#betterColoredWindow.py - color window changer

from random import randint
from ggame import *



def mouseClick(event):
    
    colors = [0xFF0000, 0xFFF000, 0xFFFF00, 0xFFFFF0, 0xFFFFFF]
    
    color = colors[randint(0,4)]
    
    red = Color(color, 1)
    redRect = RectangleAsset(1000, 1000, LineStyle(1, red), red)
    Sprite(redRect)
    

        
App().listenMouseEvent("click", mouseClick)
App().run()
