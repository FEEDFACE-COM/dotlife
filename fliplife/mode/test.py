
import random

from dotlife.util import *

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask

from fliplife import pixel,framebuffer


class Test(fliplife.mode.Mode):
    
    def run(self,**params):
        info("start test")
        prev = self.framebuffer.read()
        self.mask = Mask()
        self.mask = self.draw(params)
        return False


    
    def draw(self,invert,**params):
        
#        def dot(mask,x,y):
#            mask[x,y-1] = True
#            mask[x-1,y] = True
#            mask[x,y] = True
#            mask[x+1,y] = True
#            mask[x,y+1] = True
#            return mask
#        
#        
#        mask = Mask()
#        mask = dot(mask,int(FRAMEWIDTH/2),int(FRAMEHEIGHT/2))
#        mask = dot(mask,0,0)
#        mask = dot(mask,0,FRAMEHEIGHT-1)
#        mask = dot(mask,FRAMEWIDTH-1,0)
#        mask = dot(mask,FRAMEWIDTH-1,FRAMEHEIGHT-1)




        log(str(self.mask))
        return self.mask