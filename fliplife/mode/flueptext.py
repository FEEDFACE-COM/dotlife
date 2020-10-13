
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.font import Font

class Fluep(Mode):
        
    
    def run(self,randomize,x,y,fluepfont,msg=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        self.randomize = randomize
        self.font = font
        
        self.msg = "hello, world."
        if msg:
            self.msg = msg

        info("start flueptext {:s}: {:s}".format(fluepfont,self.msg))
        

        self.mask = self.draw(x,y,fluepfont,**params)
        log(str(self.mask))
        return True
    

    def draw(self,x,y,fluepfont,**params):
        self.mask = self.fluepdot.text(x,y,fluepfont,self.msg)
        return self.mask
        

    flags = [
        ("F:","fluepfont=",            "fluepfont",                 "fixed_10x20",           "fluepdot font",                                 None),
        Mode.FLAG["x"],
        Mode.FLAG["y"],
        Mode.FLAG["randomize"],
        (None, None,            "msg",                 "hello, world.",           "message",                                 None),
    ]