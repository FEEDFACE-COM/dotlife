
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.font import Font

class Fluep(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,font,rem=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        self.randomize = randomize
        self.font = font
        
        self.msg = "hello, world."
        if type(rem) == type([]):
            self.msg = " ".join(rem)
        elif type(rem) == type("") and rem != "":
            self.msg = rem

        info("start fluep: {:s}".format(self.msg))
        

        self.mask = self.draw(x,y,**params)
        log(str(self.mask))
        return True
    

    def draw(self,x,y,**params):
        self.mask = self.fluepdot.text(x,y,"fixed_10x20",self.msg)
        return self.mask
        
