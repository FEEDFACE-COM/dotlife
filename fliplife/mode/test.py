
from dotlife.util import *

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask



class Test(fliplife.mode.Mode):
    
    def run(self,**params):
        return False


    
    def draw(self):
        c = int(self.timer.count)
        ret = Mask(size=FRAMESIZE)
        for y in range(ret.h):
            for x in range(ret.w):
                if y%2 == x%2:
                    ret[x,y] = True
                else:
                    ret[x,y] = False
                
        return ret
