
import random

from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer, pixel

from fliplife import rendering

class Grow(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start grow")
        mask = self.draw(**params)
        
#        rendering.GetMode(self.address)
        rendering.SetMode(self.address,rendering.Differential)
        
        return True
        
    
    def draw(self,invert,**params):
        cx = int(FRAMEWIDTH/2)
        cy = int(FRAMEHEIGHT/2)
        
        r0 = random.gauss(0.,1.)
        r1 = random.gauss(0.,1.)

        x = cx + int(r0*(cx/4.))
        y = cy + int(r1*(cy/4.))


        pxl = pixel.Read(self.address,x,y)
        
        mask = fliplife.mask.Mask()
        if invert:

            if pxl:
                pixel.Flip(self.address,x,y,False)
                mask = framebuffer.Read(self.address)
                log("pixel {:d}/{:d} flip ⬜︎ off".format(x,y))
                log(str(mask))


        else:
                
            if not pxl:
                pixel.Flip(self.address,x,y,True)
                mask = framebuffer.Read(self.address)
                log("pixel {:d}/{:d} flip ⬛︎ on".format(x,y))
                log(str(mask))
        

        return mask
