
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

class Glider(fliplife.mode.Mode):
    
    
    def run(self,count,randomize,**params):
        info("start life")
        self.framebuffer.rendering.setMode(Rendering.Mode.Diff)


        mask = self.framebuffer.read()        
        
        self.life = life.Life(mask=mask)
        
        
        if randomize:
            for c in range(count):
                a,b = int(2.*(random.getrandbits(1)-0.5)), (int(2.*(random.getrandbits(1)-0.5)))
                log("got random {:d},{:d}".format(a,b))
                direction = Direction( (a,b)  )
                log("got direction {:s}".format(str(direction)))
                pos = Position( random.randint(0,FRAMEWIDTH-1), random.randint(0,FRAMEHEIGHT-1) )
                step = random.randint(0,3)
                log("add glider #{:d} at {:d}/{:d} course {:s}".format(c,pos.x,pos.y,str(direction)))
                self.life.addGlider(pos=pos,step=step,direction=direction)

        else:
            d = int(FRAMEWIDTH / count)
            direction = Direction.SouthEast
            step = 0
            pos = Position( int(FRAMEWIDTH/2) , int(FRAMEHEIGHT/2) )
            for c in range(count):
                log("add glider #{:d} at {:d}/{:d} course {:s}".format(c,pos.x,pos.y,str(direction)))
                self.life.addGlider(pos=pos,step=step,direction=direction)
                pos = Position( (pos.x+d)%FRAMEWIDTH, pos.y )
                lon,lat = direction.value
                direction = Direction( (lon*-1, lat*-1) )
                step = (step+1)%5
                
#        self.life.addGlider(direction=Direction.SouthEast)
#        self.life.addGlider(pos=(25,4),step=2,direction=Direction.NorthEast)
#        self.life.addGlider(pos=(50,6),step=4,direction=Direction.SouthWest)
#        self.life.addGlider(pos=(100,8),step=3,direction=Direction.NorthWest)

        
        
        self.draw(**params)
        return False
        
    
    def draw(self,invert,**params):
        
        prev = self.framebuffer.read()
        mask = Mask(mask=self.life.board)
        self.framebuffer.write(mask)
        
        debug(str(mask))
        return mask
    
