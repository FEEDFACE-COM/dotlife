
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.font import Font

class Pipe(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,font,rem=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)

        self.font = Font.Font(font)
        log(str(self.font))
        
        info("start pipe".format())
        
        self.msg = "your message here"

        self.buf = self.font.render(self.msg)
        log(str(self.buf))
        
        self.mask = self.draw(x,y,**params)
        return True
    

    def draw(self,x,y,**params):
        pos = Position(x,y)

        self.mask = Mask() #self.fluepdot.buffer.read()
        self.mask.mask(self.buf,pos=pos)
        ret = self.fluepdot.buffer.write(self.mask)
        info(str(self.mask))
        return ret 
        
