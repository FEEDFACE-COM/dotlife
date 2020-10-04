
import random

from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask



class Echo(fliplife.mode.Mode):
        
    
    def run(self,randomize,font,x,y,rem=None,**params):
        self.randomize = randomize
        self.msg = ""
        if type(rem) == type([]):
            self.msg = " ".join(rem)
        elif type(msg) == type(""):
            self.msg = rem

        info("start echo: {:s}".format(self.msg))
        
        self.mask = Mask()
        self.mask = self.draw(x,y,font,**params)
        log(str(self.mask))
        return False
    

    def draw(self,x,y,font,**params):
        if self.randomize:
            font = 'fixed_5x8'
            w = FRAMEWIDTH - (6*len(self.msg))
            h = FRAMEHEIGHT - (8*1)
            x = int(random.random() * float(w))
            y = int(random.random() * float(h))
        
        mask = self.framebuffer.text(x,y,font,self.msg)
        return mask
