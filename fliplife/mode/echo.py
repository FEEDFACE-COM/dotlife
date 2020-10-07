
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.font import Font

class Echo(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,font,rem=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        self.randomize = randomize
        
        self.font = Font.Font(font)
        log(str(self.font))
        
        self.msg = "hello, world."
        if type(rem) == type([]):
            self.msg = " ".join(rem)
        elif type(rem) == type("") and rem != "":
            self.msg = rem

        info("start echo: {:s}".format(self.msg))
        

        self.buf = self.font.render(self.msg)
        log(str(self.buf))
        
        self.mask = self.draw(x,y,**params)
        log(str(self.mask))
        return True
    

    def draw(self,x,y,**params):
        pos = Position(x,y)
        if self.randomize:
            w = FRAMESIZE.w - self.buf.size().w
            h = FRAMESIZE.h - self.buf.size().h
            pos.x = random.randint(0,w-1)
            pos.y = random.randint(0,h-1)


        self.mask = Mask() #self.fluepdot.buffer.read()
        self.mask.mask(self.buf,pos=pos)
        ret = self.fluepdot.buffer.write(self.mask)
        return ret 
        
