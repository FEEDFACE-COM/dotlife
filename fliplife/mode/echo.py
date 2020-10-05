
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask
from fliplife.rendering import Rendering

from dotlife.font import Font

class Echo(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,rem=None,**params):
        self.fluepdot.rendering.setMode(Rendering.Mode.Full)
#        self.fluepdot.rendering.setMode(Rendering.Mode.Diff)
        self.randomize = randomize
        
        self.font = Font.Font3x5()
        log(str(self.font))
        
        self.msg = "hello, world."
        if type(rem) == type([]):
            self.msg = " ".join(rem)
        elif type(rem) == type("") and rem != "":
            self.msg = rem

        info("start echo: {:s}".format(self.msg))
        

        msk = self.font.render(self.msg)
        log(str(msk))
        
        self.mask = self.fluepdot.buffer.read()
        self.mask = self.draw(x,y,**params)
        log(str(self.mask))
        return True
    

    def draw(self,x,y,**params):

        txt = self.font.render(self.msg)
        
        if self.randomize:
            w = FRAMEWIDTH - txt.size().w
            h = FRAMEHEIGHT - txt.size().h
            x = random.randint(0,w-1)
            y = random.randint(0,h-1)

        mask = Mask()
        mask.mask(txt,pos=Position(x,y))
        mask = self.fluepdot.buffer.write(mask)
        return mask
        
