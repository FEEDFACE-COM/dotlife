
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot


class Guns(Mode):
    
    
    def start(self,randomize,**params):
        info("start guns")
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
    
        self.life = life.Life(mask=self.mask)
        
        pos1 = Position(10,2)
        pos2 = Position(60,7)        
        off1 = Position(x=24,y=10)
        off2 = Position(x=24,y=-5)
        
        
        self.life.spawn(life.Pattern.gun,pos=pos1)
        self.life.spawn(life.Pattern.eater,pos=pos1+off1)
        
        self.life.spawn(life.Pattern.gun,pos=pos2,flip=Flip.horizontal)
        self.life.spawn(life.Pattern.eater,pos=pos2+off2,flip=Flip.horizontal)

        self.mask = Mask(self.life)

        self.draw(**params)

        return True
        
    
    def draw(self,**params):

        self.life.step()
        self.mask = Mask(mask=self.life)
        

        self.fluepdot.buffer.write(self.mask)
        info(str(self.mask))
        return self.mask
    
    flags = [
        Mode.FLAG("randomize"),
    ]
    
