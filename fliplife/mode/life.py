
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer, pixel
from fliplife.mask import Mask
from fliplife.rendering import Rendering

class Life(fliplife.mode.Mode):
    
    
    def run(self,count,**params):
        info("start life")
        self.fluepdot.rendering.setMode(Rendering.Mode.Diff)

        mask = self.fluepdot.buffer.read()

        self.life = life.Life(mask=mask)
        
        self.draw(**params)
        
        return True
        
    
    def draw(self,invert,**params):

        prev = Mask(mask=self.life.board)
        self.life.step()
        mask = Mask(mask=self.life.board)


        if True:
            self.fluepdot.buffer.write(mask)

        else:
            self.fluepdot.pixel.flipDelta(prev,mask)
        
        info(str(mask))
        return mask
    
