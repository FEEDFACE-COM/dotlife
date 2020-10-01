
import random

from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer



class Exec(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,font,msg,**params):
        
        info("start exec {:s}".format(" ".join(msg)))
        self.randomize = randomize
        mask = self.draw(x,y,font,msg,**params)
        return True
    

    def draw(self,x,y,font,msg,**params):
        data = " ".join(msg)
        if self.randomize:
            font = 'fixed_5x8'
            w = FRAMEWIDTH - (6*len(data))
            h = FRAMEHEIGHT - (8*1)
            x = int(random.random() * float(w))
            y = int(random.random() * float(h))
        
        
        self.mask = framebuffer.Text(self.address,x,y,font,msg)
        log(str(self.mask))
        return self.mask
