
import random

from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer



class Echo(fliplife.mode.Mode):
        
    
    def run(self,randomize,msg,font,x,y,**params):
        self.randomize = randomize
        self.msg = ""
        if type(msg) == type([]):
            self.msg = " ".join(msg)
        elif type(msg) == type(""):
            self.msg = msg

        info("start echo '{:s}'".format(self.msg))
        return True
    

    def draw(self,x,y,font,**params):
        if self.randomize:
            font = 'fixed_5x8'
            w = FRAMEWIDTH - (6*len(self.msg))
            h = FRAMEHEIGHT - (8*1)
            x = int(random.random() * float(w))
            y = int(random.random() * float(h))
        
        
        self.mask = framebuffer.Text(self.address,x,y,font,self.msg)
        log(str(self.mask))
        return self.mask
