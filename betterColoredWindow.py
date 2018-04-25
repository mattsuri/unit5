#Matthew Suriawinata
#4/23/18
#betterColoredWindow.py - color window changer

from random import randint
from ggame import *

#ffffd9	(255,255,217)
#176a90	(23,106,144)
#00122e	(0,18,46)
#969281	(150,146,129)
#bf5449	(191,84,73)





def mouseClick(event):
    
    colors = [0x176a90, 0xffffd9, 0x00122e, 0x969281, 0xbf5449]
    
    color = colors[randint(0,4)]
    
    red = Color(color, 1)
    redRect = RectangleAsset(1000, 1000, LineStyle(1, red), red)
    Sprite(redRect)
    

        
App().listenMouseEvent("click", mouseClick)
App().run()
