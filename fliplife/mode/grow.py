
import random

from dotlife.util import *


import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE

from fliplife.fluepdot import Fluepdot

class Grow(Mode):
    
    
    def run(self,**params):
        info("start grow")

        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        self.mask = self.draw(**params)
        return True
        
    
    def draw(self,invert,**params):
        cx = int(FRAMESIZE.w/2)
        cy = int(FRAMESIZE.h/2)
        
        r0 = random.gauss(0.,1.)
        r1 = random.gauss(0.,1.)

        x = cx + int(r0*(cx/4.))
        y = cy + int(r1*(cy/4.))


        pxl = self.fluepdot.pixel.read(x,y)
        
        
        if invert:

            if pxl:
                self.fluepdot.pixel.flip(x,y,False)
                self.mask = self.fluepdot.buffer.read()
                log(str(self.mask))


        else:
                
            if not pxl:
                self.fluepdot.pixel.flip(x,y,True)
                self.mask = self.fluepdot.buffer.read()
                log(str(self.mask))
        

        return self.mask


    flags = [
        Mode.FLAG("invert"),
    ]
