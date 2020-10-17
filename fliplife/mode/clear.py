
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE


class Clear(Mode):
    
    
    def start(self,invert,**params):
        log("start clear{:s}".format(" [invert]" if invert else ""))
        return False


    def draw(self,invert,**params):
        mask = Mask()
        if invert:
            mask = Mask().inverse()

        return mask
                
    
    flags = [
        Mode.FLAG("invert"),
    ]
