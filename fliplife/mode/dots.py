
import random

from dotlife.util import *
from dotlife import math


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer, pixel

from fliplife.rendering import Rendering

class Dots(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start dots")
        self.count = 0
        
        
        self.fluepdot.rendering.setMode(Rendering.Mode.Diff)
        
        self.mask = self.fluepdot.buffer.read()
        self.mask= self.draw(**params)
        
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


        self.fluepdot.pixel.flipDelta(prev, self.mask)

        log(str(self.mask))
        return self.mask
    
