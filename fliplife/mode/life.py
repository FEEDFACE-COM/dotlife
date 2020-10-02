
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer, pixel
from fliplife.mask import Mask
from fliplife import rendering

class Life(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start life")
        rendering.SetMode(self.address,rendering.Differential)

        self.life = life.Life(size=FRAMESIZE)
        
        self.prev = Mask(mask=self.life.board)

        
        
        self.life.addGlider()
        self.life.addGlider(pos=(40,4),step=2,direction=Direction.NorthEast)
        self.life.addGlider(pos=(100,8),step=3,direction=Direction.SouthEast)



        
        return True
        
    
    def draw(self,invert,**params):

        
        self.life.step()
        
        mask = Mask(mask=self.life.board)

        brights = mask.deltaBright(self.prev)
        darks = mask.deltaDark(self.prev)
        
        for (x,y) in brights:
            log("dot {:d}/{:d} flip on: ⬛︎".format(x,y))
            pixel.Flip(self.address,x,y,True)


        for (x,y) in darks:
            log("dot {:d}/{:d} flip off: ⬜︎".format(x,y))
            pixel.Flip(self.address,x,y,True)


        log(str(mask))
        self.prev = mask
        return mask
    
