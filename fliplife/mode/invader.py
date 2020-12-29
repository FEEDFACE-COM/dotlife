
from dotlife.util import *

import fliplife
from fliplife.mode import Mode
from fliplife import FRAMESIZE, Mask

import dotlife.invader as invader
from dotlife.invader import INVADER

class Invader(Mode):


    def start(self,count,alternate,**params):
        info("start invader{:s}{:s}".format(" ({:d} invaders)".format(count) if count else "" ,"alt" if alternate else ""))
        self.invader = invader.Invader(self.timer.duration,count,alternate)
        return True
        
    
    def draw(self,**params):
        return self.invader.mask(size=FRAMESIZE)
        
    
    flags = [
        ("c:","count=","count",0,"invader count", lambda x: int(x)),
        ("A","alt","alternate",False,"alternate rows?", None),
    ]
