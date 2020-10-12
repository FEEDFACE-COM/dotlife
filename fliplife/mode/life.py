
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife.mode import Mode 
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

class Life(Mode):
    
    
    def run(self,count,**params):
        info("start life")
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)

        mask = self.fluepdot.buffer.read()
        self.life = life.Life(mask=mask)
        self.draw(**params)
        
        return True
        
    
    def draw(self,invert,**params):

        prev = Mask(mask=self.life)
        self.life.step()
        mask = Mask(mask=self.life)


        if True:
            self.fluepdot.buffer.write(mask)

#        else:
#            self.fluepdot.pixel.flipDelta(prev,mask)
        
        info(str(mask))
        return mask
    
    flags = [
        Mode.FLAGS["invert"],
        Mode.FLAGS["count"],
    ]