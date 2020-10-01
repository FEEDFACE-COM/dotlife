
import random

from dotlife.util import *

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask

from fliplife import pixel,framebuffer


class Test(fliplife.mode.Mode):
    
    def run(self,**params):
        c = int(self.timer.count)
        self.mask = Mask(size=FRAMESIZE)
        for y in range(self.mask.h):
            for x in range(self.mask.w):
                if y%2 == x%2:
                    self.mask[x,y] = True
                else:
                    self.mask[x,y] = False
        return True


    
    def draw(self,**params):
        x = random.randint(0,FRAMEWIDTH-1)
        y = random.randint(0,FRAMEHEIGHT-1)
        val = pixel.Pixel.Get(self.address,x,y)
        buf = framebuffer.Framebuffer.Get(self.address)
        log("got val: "+str(val))
        return self.mask
