
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
    
    
    def run(self,count,**params):
        info("start life")
        rendering.SetMode(self.address,rendering.Differential)

        mask = framebuffer.Read(self.address)

        self.life = life.Life(mask=mask)
        
        self.draw(**params)
        
        return True
        
    
    def draw(self,invert,**params):
        
        prev = Mask(mask=self.life.board)
        self.life.step()
        mask = Mask(mask=self.life.board)


        if False:
            framebuffer.Write(self.address,mask)
            log(str(mask))
            return mask

        if False:
            log(str(self.life))
            return mask
            
        if True:
            pixel.WriteDelta(self.address,prev,mask)
            log(str(mask))
            return mask
        
        
        for y in range(FRAMEHEIGHT):
            for x in range(FRAMEWIDTH):
                if mask[x,y] and not prev[x,y]:
                    pixel.Flip(self.address,x,y,True)
                if not mask[x,y] and prev[x,y]:
                    log("dot {:d}/{:d} flip off: ⬜︎".format(x,y))
                    pixel.Flip(self.address,x,y,False)
        
        info(str(mask))
        return mask
    
