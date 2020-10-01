
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
        
        rendering.GetMode(self.address)
        
        rendering.PutMode(self.address,rendering.Differential)
#        return False
        
        return True
        
    
    def draw(self,invert,**params):
        cx = int(FRAMEWIDTH/2)
        cy = int(FRAMEHEIGHT/2)
        
        r0 = random.gauss(0.,1.)
        r1 = random.gauss(0.,1.)

        x = cx + int(r0*(cx/4.))
        y = cy + int(r1*(cy/4.))


        pxl = pixel.Get(self.address,x,y)
        
        mask = fliplife.mask.Mask()
        if invert:

            if pxl:
                pixel.Delete(self.address,x,y)
                mask = framebuffer.Get(self.address)
                log("pixel {:d}/{:d} flip ⬜︎ off".format(x,y))
                log(str(mask))


        else:
                
            if not pxl:
                pixel.Post(self.address,x,y)
                mask = framebuffer.Get(self.address)
                log("pixel {:d}/{:d} flip ⬛︎ on".format(x,y))
                log(str(mask))
        

        return mask
