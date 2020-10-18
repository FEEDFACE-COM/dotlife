
import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.math import *

from dotlife.pattern import Pattern
from oledlife import Mask,Buffer
import dotlife.plasma as plasma

from dotlife.palette import Palette
from dotlife.clock import Timer

from oledlife.mode import Mode






class Plasma(Mode):



    def start(self,step,invert,pattern,**params):
        info("plasma start {:}".format(pattern))
        self.mask = Mask().addMask(pattern.Mask(),pos=None)
    
        self.plasma = plasma.Plasma(self.timer.duration,op=Operation.add,palette=Palette.Polynom())

        if invert:
            self.mask = self.mask.inverse()
        info(str(self.mask))
        return True
        
        
        
    def draw(self,back,step,**params):

        ret = Buffer()
        front = self.plasma.buffer(off=0)
        ret.add(front.addMask(self.mask,light=DARK))
        
        if back:
           back = self.plasma.buffer(off=PI/2.)
           ret.add(back.addMask(self.mask.inverse(), light=DARK))


        return ret


    Pattern = dotlife.pattern.Pattern
    DefaultPattern = dotlife.pattern.Pattern.fyi
     
    flags = [
        ("b", "back", "back", False, "", None),
        Mode.FLAG("pattern",DefaultPattern), 
        Mode.FLAG("invert"),  
        Mode.FLAG("step"),
    ]

        
