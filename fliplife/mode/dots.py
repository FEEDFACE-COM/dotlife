
import random

from dotlife.util import *
from dotlife import math


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer, pixel

from fliplife import rendering

class Dots(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start dots")
        self.count = 0
        
        
        
        self.mask = framebuffer.Read(self.address)
        rendering.SetMode(self.address,rendering.Differential)
        log(str(self.mask))        
        return True
        
    
    def draw(self,invert,**params):
    
        cx = int(FRAMEWIDTH/2)
        cy = int(FRAMEHEIGHT/2)
        
        r0 = random.gauss(0.,1.5)
        r1 = random.gauss(0.,2.)

        x = cx + int(r0*(cx/4.))
        y = cy + int(r1*(cy/4.))


        prev = mask.Mask(mask=self.mask)
        
        self.mask[x,y-1] ^= True
        self.mask[x-1,y] ^= True
        self.mask[x,y] ^= True
        self.mask[x+1,y] ^= True
        self.mask[x,y+1] ^= True

        brights = self.mask.deltaBright(prev)
        darks = self.mask.deltaDark(prev)
        
        for (x,y) in brights:
            log("dot {:d}/{:d} flip on: ⬛︎".format(x,y))
            pixel.Flip(self.address,x,y,True)


        for (x,y) in darks:
            log("dot {:d}/{:d} flip off: ⬜︎".format(x,y))
            pixel.Flip(self.address,x,y,False)


        log(str(prev))
        log(str(self.mask))
        return self.mask
    
