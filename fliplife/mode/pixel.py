
import random

from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer,pixel


class Pixel(fliplife.mode.Mode):
    
    
    def run(self,x,y,invert,**params):
        info("start pixel {:d}/{:d}".format(x,y))

        mask = framebuffer.Get(self.address)
        
        pxl = pixel.Get(self.address,x,y)
        if pxl:
            log("pixel {:d}/{:d} ⬛︎ on".format(x,y))
        else:
            log("pixel {:d}/{:d} ⬜︎ off".format(x,y))
        
        
        if not invert and not pxl:
            log("pixel {:d}/{:d} flip ⬛︎ on".format(x,y))
            pixel.Post(self.address,x,y)
            
        if invert and pxl:
            log("pixel {:d}/{:d} flip ⬜︎ off".format(x,y))
            pixel.Delete(self.address,x,y)

        mask = framebuffer.Get(self.address)
        log(str(mask))        
        return False
        
    
