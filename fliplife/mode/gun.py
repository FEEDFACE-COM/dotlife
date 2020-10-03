
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


class Gun(fliplife.mode.Mode):
    
    
    def run(self,count,randomize,**params):
        info("start life")
        rendering.SetMode(self.address,rendering.Differential)


        self.mask = framebuffer.Read(self.address)        
        
#        self.life = life.Life(mask=mask)

        pos1 = Position(10,2)
        pos2 = Position(60,7)        
        off = Position(x=24,y=10)
        
        eat = Mask.Load(life.Life.EATER[0])
        gun = Mask.Load(life.Life.GUN[1])
        log("add gun at {:s}:\n{:s}".format(str(pos1),str(gun)))
        self.mask.mask(gun, pos=pos1, wrap=True)
        self.mask.mask(eat, pos=pos1+off, wrap=True)


        gun = gun.flip(Axis.Horizontal)
        eat = eat.flip(Axis.Horizontal)
        log("add gun at {:s}:\n{:s}".format(str(pos1),str(gun)))
        self.mask.mask(gun, pos=pos2, wrap=True)
        self.mask.mask(eat, pos=pos2+Position(x=24,y=-5), wrap=True)


#        eat = eat.flip(Axis.Horizontal)
#        gun = gun.flip(Axis.Vertical)
#        log("add gun at {:s}".format(str(pos2)))
#        self.mask.mask(gun, pos=pos1, wrap=True)
#        self.mask.mask(eat, pos=pos1+off, wrap=True)

                
        self.draw(**params)
        return False
        
    
    def draw(self,invert,**params):
        
        prev = framebuffer.Read(self.address)
#        mask = Mask(mask=self.life.board)
        framebuffer.Write(self.address,self.mask)
        
        debug(str(self.mask))
        return self.mask
    
