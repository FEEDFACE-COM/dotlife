
import random

from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer, pixel

from fliplife.rendering import Rendering

class Grow(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start grow")

        self.fluepdot.rendering.setMode(Rendering.Mode.Diff)
        mask = self.draw(**params)
        return True
        
    
    def draw(self,invert,**params):
        cx = int(FRAMEWIDTH/2)
        cy = int(FRAMEHEIGHT/2)
        
        r0 = random.gauss(0.,1.)
        r1 = random.gauss(0.,1.)

        x = cx + int(r0*(cx/4.))
        y = cy + int(r1*(cy/4.))


        pxl = self.fluepdot.pixel.read(x,y)
        
        mask = fliplife.mask.Mask()
        if invert:

            if pxl:
                self.fluepdot.pixel.flip(x,y,False)
                mask = self.fluepdot.buffer.read()
                log("pixel {:d}/{:d} flip ⬜︎ off".format(x,y))
                log(str(mask))


        else:
                
            if not pxl:
                self.fluepdot.pixel.flip(x,y,True)
                mask = self.fluepdot.buffer.read()
                log("pixel {:d}/{:d} flip ⬛︎ on".format(x,y))
                log(str(mask))
        

        return mask
