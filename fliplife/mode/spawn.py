
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot


class Spawn(Mode):
    

    
    DefaultPattern = life.Pattern.glider
    DefaultPosition = Position(0,0)
    

    
    def run(self,x,y,randomize,pattern,step,count,**params):
    
        
        info("start spawn {:s}".format(pattern.name.lower()))
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)

        self.life = life.Life(mask=self.mask)



        if randomize:
            for c in range(count):
                pos = Position(random.randint(0,FRAMESIZE.w-1),random.randint(0,FRAMESIZE.h-1))
                flip = random.choice( list(Flip) )
                self.life.spawn(pattern,pos,step,flip)

        else:
            pos = Position(x,y)
            self.life.spawn(pattern,pos,step,Flip.NoFlip)            
        
        self.draw(**params)
        return True


    
    def draw(self,**params):
        
        prev = self.fluepdot.buffer.read()
        self.life.step()
        mask = Mask(mask=self.life)

        self.fluepdot.buffer.write(mask)
        
        info(str(mask))
        return mask
    
    
    
    patterns = life.Pattern

    flags = [
        ("p:", "pattern=",     "pattern",    DefaultPattern, "pattern", lambda x: life.Pattern[x.lower()] ),
#        Mode.FLAG["pattern"],
        Mode.FLAG["step"],
        Mode.FLAG["count"],
        Mode.FLAG["randomize"],
        Mode.FLAG["x"],
        Mode.FLAG["y"],
    ]
    
