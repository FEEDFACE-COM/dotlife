
import random

from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer,pixel


class Pixel(fliplife.mode.Mode):
    
    
    def run(self,x,y,invert,**params):
        info("start pixel {:d}/{:d}".format(x,y))

        mask = framebuffer.Read(self.address)
        
        pxl = pixel.Read(self.address,x,y)
        if pxl:
            log("pixel {:d}/{:d} ⬛︎ on".format(x,y))
        else:
            log("pixel {:d}/{:d} ⬜︎ off".format(x,y))
        
        
        if not invert and not pxl:
            log("pixel {:d}/{:d} flip ⬛︎ on".format(x,y))
            pixel.Flip(self.address,x,y,True)
            
        if invert and pxl:
            log("pixel {:d}/{:d} flip ⬜︎ off".format(x,y))
            pixel.Flip(self.address,x,y,True)

        mask = framebuffer.Read(self.address)
        log(str(mask))        
        return False
        
    
