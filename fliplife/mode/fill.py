
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer
from fliplife.mask import Mask

from enum import Enum, auto

class Pattern(Enum):
    Check = auto()


class Fill(fliplife.mode.Mode):
    
    DefaultPattern = Pattern.Check
    
    
    def run(self,invert,pattern,**params):
        log("start fill{:s}".format(" [invert]" if invert else ""))
        mask = self.fluepdot.buffer.read()
        log(str(mask))

        if pattern == "default":
            pattern = Fill.DefaultPattern
        else:
            try:
                pattern = getattr(Pattern,pattern.capitalize())
            except AttributeError as x:
                raise Error("unknown pattern {:s}".format(pattern))


        mask = Mask()
        for y in range(FRAMEHEIGHT):
            for x in range(FRAMEWIDTH):
                if pattern == Pattern.Check:
                    if x%2 == y%2:
                        mask[x,y] = True
        
        if invert: 
            mask.inv()
        mask = self.fluepdot.buffer.write(mask)
        log(str(mask))
        return False
    
