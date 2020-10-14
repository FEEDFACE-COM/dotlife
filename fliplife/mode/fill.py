
import random

from dotlife.util import *

from dotlife.font import Font,FONT
from dotlife.effects import Axis, Border, Morph, Morph2

from fliplife import Mask, FRAMESIZE, DEFAULT_FONT
from fliplife.mode import Mode

from enum import auto

class Pattern(Enum):
    check = auto()
    gauss = auto()
    font = auto()
    axis = auto()
    border = auto()

    

class Fill(Mode):
    
    DefaultPattern = Pattern.check
    
    
    def run(self,pattern,invert,font,offset,**params):
        log("start fill with {:s}{:s}".format(str(pattern)," [invert]" if invert else ""))

        self.font = Font(font)
        self.offset = offset
        
        log("before:\n"+str(self.mask))
        
        msk = self.tick(pattern,invert,**params)
        self.mask.addMask(msk)
        log("after:\n"+str(self.mask))
        
        return True
    
    

    def tick(self,pattern,invert,**params):
    
        ret = Mask()
        
    
        if pattern == Pattern.check:
            for y in range(FRAMESIZE.h):
                for x in range(FRAMESIZE.w):
                    if x%2 != y%2:
                        ret[x,y] = True

        elif pattern == Pattern.gauss:
            for y in range(FRAMESIZE.h):
                for x in range(FRAMESIZE.w):
                    if random.gauss(0.,1.) > 0.:
                        ret[x,y] = True

        elif pattern == Pattern.font:
            fill = self.font.render_repertoire(offset=self.offset,size=self.mask.size())
            self.offset += 1
            ret.addMask(fill)
        
        elif pattern == Pattern.axis:
            fill = Axis(self.mask.size())
            ret.addMask(fill)

        elif pattern == Pattern.border:
            fill = Border(self.mask.size())
            ret.addMask(fill)
        
        if invert: 
            ret.inv()
    
        return ret

    
    def draw(self,pattern,invert,**params):

        self.offset += 1

        mask = self.mask
        next = self.tick(pattern,invert,**params)
        
        log("from:\n"+str(mask))
        log("to:\n"+str(next))
        
        ret = Morph2(mask,next)
        return ret
    

    patterns = Pattern
    
    flags = [
        ("p:", "pattern=",     "pattern",    DefaultPattern, "pattern", lambda x: Pattern[x.lower()] ),
        ("o:", "offset=",      "offset",                  0, "offset",  lambda x: int(x)             ),
        Mode.FLAG["invert"],
        Mode.FLAG["font"],
    ]        
    
