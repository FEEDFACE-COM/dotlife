
from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.http import *
from fliplife.mask import Mask


class Ping(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start ping")
        
        rsp = get(self.address,"framebuffer",None)
        if rsp == None:
            error("fail ping")
            return

        self.mask = Mask.MaskFromResponse( rsp )
        log("new mask: {:d}x{:d}".format(self.mask.w,self.mask.h))
        log(str(self.mask))
#        fun(str(self.mask))
        return False
    
    def draw(self):
        return self.mask
