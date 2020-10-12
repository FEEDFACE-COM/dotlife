
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import Mask, FRAMESIZE


class Clear(fliplife.mode.Mode):
    
    
    def run(self,invert,**params):
        log("start clear{:s}".format(" [invert]" if invert else ""))
        mask = Mask()
        if invert: 
            mask.inv()
        mask = self.fluepdot.buffer.write(mask)
        log(str(mask))
        return False
    
    flags = [
        ("i",  "invert",           "invert",               False,                  "invert pattern?",                                         None ),
    ]
