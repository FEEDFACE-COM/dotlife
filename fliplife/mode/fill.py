
from dotlife.util import *

from dotlife.font import Font,FONT

import fliplife
from fliplife import Mask, FRAMESIZE

from enum import Enum, auto

class Pattern(Enum):
    Check = auto()
    Font = auto()

    def __str__(self):
        return self.name

    @classmethod
    def named(self,s):
        for f in Pattern:
            if f.name == s:
                return f
        raise Error("unknown pattern: "+str(s))
    

class Fill(fliplife.mode.Mode):
    
    DefaultPattern = Pattern.Check
    
    
    def run(self,invert,pattern,font,**params):
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
        if pattern in [Pattern.Check]:
            for y in range(FRAMESIZE.h):
                for x in range(FRAMESIZE.w):
                    if pattern == Pattern.Check:
                        if x%2 == y%2:
                            mask[x,y] = True
        elif pattern == Pattern.Font:
            mask = Mask()
            fnt = Font.Font(font)
            msk = fnt.repertoire(size=mask.size())
            mask.mask(msk)
        
        if invert: 
            mask.inv()
        mask = self.fluepdot.buffer.write(mask)
        log(str(mask))
        return False
    
