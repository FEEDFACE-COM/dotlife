
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
    

    Pattern = life.Pattern
    DefaultPattern = life.Pattern.glider
    DefaultPosition = Position(0,0)
    

    
    def start(self,x,y,randomize,pattern,step,count,flip,**params):
    
        
        info("start spawn {:s}".format(pattern.name.lower()))
        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        self.life = life.Life(mask=self.mask)



        if randomize:
            for c in range(count):
                pos = Position(random.randint(0,FRAMESIZE.w-1),random.randint(0,FRAMESIZE.h-1))
                self.life.spawn(pattern,pos,step,random.choice( list(Flip) ))

        else:
            pos = Position(x,y)
            self.life.spawn(pattern,pos,step,flip)            
        
        self.draw(**params)
        return True


    
    def draw(self,**params):
        
        self.life.step()
        mask = Mask(mask=self.life)

        self.fluepdot.buffer.write(mask)
        
        return mask
    
    
    

    flags = [
        Mode.FLAG("pattern",DefaultPattern),
        Mode.FLAG("step"),
        Mode.FLAG("count"),
        Mode.FLAG("randomize"),
        ("F:","flip=","flip",Flip.noflip,"flip pattern?",lambda x: Flip[x]),
        Mode.FLAG("x"),
        Mode.FLAG("y"),
    ]
    
