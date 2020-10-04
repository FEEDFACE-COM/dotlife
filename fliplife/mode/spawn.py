
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer, pixel
from fliplife.mask import Mask
from fliplife import rendering


class Spawn(fliplife.mode.Mode):
    

    
    DefaultPattern = life.Pattern.Glider
    DefaultPosition = Position(0,0)
    

    
    def run(self,x,y,randomize,pattern,step,count,**params):
    
        if pattern == "default":
            pattern = DefaultPattern
        else:
            try:
                pattern = getattr(life.Pattern,pattern.capitalize())
            except AttributeError as x:
                raise Error("unknown pattern {:s}".format(pattern))
        
        info("start spawn {:s}".format(pattern))
        rendering.SetMode(self.address,rendering.Differential)

        mask = framebuffer.Read(self.address)        
        self.life = life.Life(mask=mask)


        if randomize:
            for c in range(count):
                pos = Position(random.randint(0,FRAMEWIDTH-1),random.randint(0,FRAMEHEIGHT-1))
                flip = random.choice( list(Flip) )
                self.life.spawn(pattern,pos,step,flip)

        else:
            pos = Position(x,y)
            self.life.spawn(pattern,pos,step,Flip.NoFlip)            
        
        self.draw(**params)
        return True
        
    
    def draw(self,**params):
        
        prev = framebuffer.Read(self.address)
        self.life.step()
        mask = Mask(mask=self.life.board)

#        framebuffer.Write(self.address,mask)
        
        log(str(mask))
        return mask
    
