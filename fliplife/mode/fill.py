
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer
from fliplife.mask import Mask


class Fill(fliplife.mode.Mode):
    
    
    def run(self,invert,pattern,**params):
        log("start fill{:s}".format(" [invert]" if invert else ""))
        mask = framebuffer.Read(self.address)
        log(str(mask))

        mask = Mask()
        if pattern == "check":
            for y in range(FRAMEHEIGHT):
                for x in range(FRAMEWIDTH):
                    if x%2 == y%2:
                        mask[x,y] = True
        
        if invert: 
            mask.inv()
        mask = framebuffer.Write(self.address,mask)
        log(str(mask))
        return False
    
