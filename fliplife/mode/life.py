
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife.mode import Mode 
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

class Style(Enum):

    class glider():
        pass

class Life(Mode):

    DefaultStyle = Style.glider


    
    def start(self,count,**params):
        info("start life")
        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        mask = self.fluepdot.buffer.read()
        self.life = life.Life(mask=mask)
        self.draw(**params)
        
        return True
        
    
    def draw(self,**params):

        self.life.step()

        return Mask(mask=self.life)


    
    flags = [
        Mode.FLAG("style",DefaultStyle),
    ]
