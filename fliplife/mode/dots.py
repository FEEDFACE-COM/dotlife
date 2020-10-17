
import random

from dotlife.util import *
from dotlife import math



from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE

from fliplife.fluepdot import Fluepdot



class Dots(Mode):
    
    
    def start(self,**params):
        info("start dots")
        self.count = 0
        
        
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        
        self.mask = self.fluepdot.buffer.read()
        self.mask= self.draw(**params)
        
        return True
        
    
    def draw(self,invert,**params):
    
        cx = int(FRAMESIZE.w/2)
        cy = int(FRAMESIZE.h/2)
        
        r0 = random.gauss(0.,1.5)
        r1 = random.gauss(0.,2.)

        x = cx + int(r0*(cx/4.))
        y = cy + int(r1*(cy/4.))


        prev = Mask(mask=self.mask)
        
        self.mask[x,y] ^= True
        self.mask[x,y-1] ^= True
        self.mask[x+1,y] ^= True
        self.mask[x,y+1] ^= True
        self.mask[x-1,y] ^= True


        self.fluepdot.pixel.flip(x,y,    self.mask[x,y])
        self.fluepdot.pixel.flip(x,y-1,  self.mask[x,y-1])
        self.fluepdot.pixel.flip(x-1,y,  self.mask[x-1,y])
        self.fluepdot.pixel.flip(x+1,y,  self.mask[x+1,y])
        self.fluepdot.pixel.flip(x,y+1,  self.mask[x,y+1])


        log(str(self.mask))
        return self.mask
    
    flags = [
        Mode.FLAG("invert"),
    ]
