
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask
from fliplife.http import *


class Clear(fliplife.mode.Mode):
    
    
    def run(self,**params):
        log("start clear")
        mask = Mask()
        log(str(mask))
        data = mask.toData()
        rsp = post(self.address,"framebuffer",None,data)
        log(str(mask))
        return False
    
    def draw(self):
        return Mask()
        c = int(self.timer.count)
        ret = Mask()
        for y in range(ret.h):
            for x in range(ret.w):
                if y%2 == x%2:
                    ret[x,y] = True
                else:
                    ret[x,y] = False
                
        return ret
