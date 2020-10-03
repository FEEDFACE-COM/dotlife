
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
    
    
    def run(self,count,randomize,pattern,**params):
        info("start spawn")
        rendering.SetMode(self.address,rendering.Differential)


        mask = framebuffer.Read(self.address)        
        
        self.life = life.Life(mask=mask)
        
        if pattern == "default":
            pattern == "eater"
        if not pattern in [ "glider", "gun", "eater" ]:
            return False
        
        if randomize:
            for c in range(count):
                a,b = int(2.*(random.getrandbits(1)-0.5)), (int(2.*(random.getrandbits(1)-0.5)))
                log("got random {:d},{:d}".format(a,b))
                direction = Direction( (a,b)  )
                log("got direction {:s}".format(str(direction)))
                pos = Position( random.randint(0,FRAMEWIDTH-1), random.randint(0,FRAMEHEIGHT-1) )
                step = random.randint(0,3)
                if pattern == "glider":
                    log("add glider #{:d} at {:d}/{:d} course {:s}".format(c,pos.x,pos.y,str(direction)))
                    self.life.addGlider(pos=pos,step=step,direction=direction)
                elif pattern == "gun":
                    log("add gun #{:d} at {:d}/{:d}".format(c,pos.x,pos.y))
                    self.life.addGun(pos=pos,step=step)
                elif pattern == "eater":
                    self.life.addEater(pos=pos,step=step)
                    log("add eater #{:d} at {:d}/{:d}".format(c,pos.x,pos.y))

        else:
            d = int(FRAMEWIDTH / count)
            direction = Direction.SouthEast
            step = 0
            pos = Position( int(FRAMEWIDTH/2) , int(FRAMEHEIGHT/2) )
            for c in range(count):
                if pattern == "glider":
                    log("add glider #{:d} at {:d}/{:d} course {:s}".format(c,pos.x,pos.y,str(direction)))
                    self.life.addGlider(pos=pos,step=step,direction=direction)
                elif pattern == "gun":
                    log("add gun #{:d} at {:d}/{:d}".format(c,pos.x,pos.y))
                    self.life.addGun(pos=pos,step=step)
                elif pattern == "eater":
                    self.life.addEater(pos=pos,step=step)
                    log("add eater #{:d} at {:d}/{:d}".format(c,pos.x,pos.y))
                pos = Position( (pos.x+d)%FRAMEWIDTH, pos.y )
                lon,lat = direction.value
                direction = Direction( (lon*-1, lat*-1) )
                step = (step+1)%5
                

        
        
        self.draw(**params)
        return False
        
    
    def draw(self,invert,**params):
        
        prev = framebuffer.Read(self.address)
        mask = Mask(mask=self.life.board)
        framebuffer.Write(self.address,mask)
        
        debug(str(mask))
        return mask
    
