
import random

from dotlife.util import *


import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE


class Pixel(Mode):
    
    
    def run(self,x,y,invert,**params):
        info("start pixel {:d}/{:d}".format(x,y))

        mask = self.fluepdot.buffer.read()
        
        pxl = self.fluepdot.pixel.read(x,y)
        if pxl:
            log("pixel {:d}/{:d} ⬛︎ bright".format(x,y))
        else:
            log("pixel {:d}/{:d} ⬜︎ dark".format(x,y))
        
        
        if not invert and not pxl:
            log("pixel {:d}/{:d} flip bright: ⬛︎".format(x,y))
            self.fluepdot.pixel.flip(x,y,True)
            
        if invert and pxl:
            log("pixel {:d}/{:d} flip dark: ⬜︎".format(x,y))
            self.fluepdot.pixel.flip(x,y,False)

        mask = self.fluepdot.buffer.read()
        log(str(mask))        
        return False
        
    
    flags = [
        Mode.FLAG["x"],
        Mode.FLAG["y"],
        Mode.FLAG["invert"],
    ]