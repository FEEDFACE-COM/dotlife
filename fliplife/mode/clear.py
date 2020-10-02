
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer
from fliplife.mask import Mask


class Clear(fliplife.mode.Mode):
    
    
    def run(self,invert,**params):
        log("start clear{:s}".format(" [invert]" if invert else ""))
        mask = Mask()
        if invert: 
            mask.inv()
        log(str(mask))
        mask = framebuffer.Write(self.address,mask)
        log(str(mask))
        return False
    
