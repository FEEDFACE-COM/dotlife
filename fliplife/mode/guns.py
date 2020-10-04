
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


class Guns(fliplife.mode.Mode):
    
    
    def run(self,count,randomize,**params):
        info("start life")
        self.fluepdot.rendering.setMode(Rendering.Mode.Diff)
    

        self.mask = self.fluepdot.buffer.read()        
        self.life = life.Life(mask=self.mask)
        
        pos1 = Position(10,2)
        pos2 = Position(60,7)        
        off1 = Position(x=24,y=10)
        off2 = Position(x=24,y=-5)
        
        
        self.life.spawn(life.Pattern.Gun,pos=pos1)
        self.life.spawn(life.Pattern.Eater,pos=pos1+off1)
        
        self.life.spawn(life.Pattern.Gun,pos=pos2,flip=Flip.Horizontal)
        self.life.spawn(life.Pattern.Eater,pos=pos2+off2,flip=Flip.Horizontal)

        self.mask = Mask(self.life)

        self.draw(**params)

        return True
        
    
    def draw(self,invert,**params):

        self.life.step()
        self.mask = Mask(mask=self.life)
        

        self.fluepdot.buffer.write(self.mask)
        info(str(self.mask))
        return self.mask
    
