
import dotlife
from dotlife.pattern import *
from dotlife.mask import *
from dotlife.buffer import *
from dotlife.util import *
import dotlife.tunnel
from dotlife.palette import *
from dotlife.time import Timer
from dotlife.math import *

from oledlife import FRAMESIZE 
from oledlife.mode import Mode

from dotlife.pattern import Pattern

from dotlife import symbols

class Tunnel(Mode):

    def start(self,pattern,step,invert,**params):

        info("tunnel start {:}".format(pattern))
        self.mask = Mask().addMask(pattern.Mask(step=step),pos=None)

        radius = 5./8.
        self.tunnel = dotlife.tunnel.Tunnel(duration=self.timer.duration,radius=radius)
        
        if invert:
            self.mask = self.mask.inverse()
        info(str(self.mask))
        return True
        

    def draw(self,back,**params):
        ret = Buffer()

        front = self.tunnel.buffer(off=0.)
        ret.add(front.addMask(self.mask,light=DARK))
        
        if back:
            back = self.tunnel.buffer(off=0.5)
            ret.add(back.addMask(self.mask.inverse(), light=DARK))
        return ret

    
    Pattern = dotlife.symbols.Symbol
    DefaultPattern = dotlife.symbols.Symbol.question
     
    flags = [
        ("b", "back", "back", False, "", None),
        Mode.FLAG("pattern",DefaultPattern), 
        Mode.FLAG("invert"),  
        Mode.FLAG("step"),
    ]

