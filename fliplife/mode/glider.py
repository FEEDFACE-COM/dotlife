
import random

from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life


import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

class Glider(Mode):
    
    
    def run(self,count,randomize,**params):
        info("start life")
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)


        mask = self.fluepdot.buffer.read()        
        
        self.life = life.Life(mask=mask)
        
        
        if randomize:
            for c in range(count):
                a,b = int(2.*(random.getrandbits(1)-0.5)), (int(2.*(random.getrandbits(1)-0.5)))
                log("got random {:d},{:d}".format(a,b))
                direction = Direction( (a,b)  )
                log("got direction {:s}".format(str(direction)))
                pos = Position( random.randint(0,FRAMESIZE.w-1), random.randint(0,FRAMESIZE.h-1) )
                step = random.randint(0,3)
                log("add glider #{:d} at {:d}/{:d} course {:s}".format(c,pos.x,pos.y,str(direction)))
                self.life.spawn(life.Pattern.glider,pos=pos,step=step)

        else:
            d = int(FRAMESIZE.w / count)
            direction = Direction.SouthEast
            step = 0
            pos = Position( int(FRAMESIZE.w/2) , int(FRAMESIZE.h/2) )
            for c in range(count):
                log("add glider #{:d} at {:d}/{:d} course {:s}".format(c,pos.x,pos.y,str(direction)))
                self.life.spawn(life.Pattern.glider,pos=pos,step=step)
                pos = Position( (pos.x+d)%FRAMESIZE.w, pos.y )
                lon,lat = direction.value
                direction = Direction( (lon*-1, lat*-1) )
                step = (step+1)%5
                
#        self.life.addGlider(direction=Direction.SouthEast)
#        self.life.addGlider(pos=(25,4),step=2,direction=Direction.NorthEast)
#        self.life.addGlider(pos=(50,6),step=4,direction=Direction.SouthWest)
#        self.life.addGlider(pos=(100,8),step=3,direction=Direction.NorthWest)

        
        
        self.mask = self.draw(**params)
        return False
        
    
    def draw(self,**params):
        
        prev = self.fluepdot.buffer.read()
        mask = Mask(mask=self.life)
        self.fluepdot.buffer.write(mask)
        
        info(str(mask))
        return mask
    
    flags = [
        Mode.FLAG["count"],
        Mode.FLAG["randomize"],
    ]
