
import random

from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer




class Gauss(fliplife.mode.Mode):
    
    def run(self,**params):
        info("start gauss")
        self.mask = mask.Mask(size=FRAMESIZE)
        for y in range(FRAMEHEIGHT):
            for x in range(FRAMEWIDTH):
                if random.gauss(1.,3.) > 4.:
                    self.mask[x,y] = True
        
        
        log(str(self.mask))
        self.mask = framebuffer.Post(self.address,self.mask)
        log(str(self.mask))
        
        return False
    

        