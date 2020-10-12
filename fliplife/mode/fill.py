
from dotlife.util import *

from dotlife.font import Font,FONT

from fliplife import Mask, FRAMESIZE, DEFAULT_FONT
from fliplife.mode import Mode

from enum import Enum, auto

class Pattern(Enum):
    check = auto()
    font = auto()

    def __str__(self):
        return self.name

    @classmethod
    def named(self,s):
        for f in Pattern:
            if f.name == s:
                return f
        raise Error("unknown pattern: "+str(s))
    

class Fill(Mode):
    
    DefaultPattern = Pattern.check
    
    
    def run(self,invert,pattern,font,**params):
        log("start fill {:s}{:s}".format(str(pattern)," [invert]" if invert else ""))
        mask = self.fluepdot.buffer.read()
        log(str(mask))



        if pattern in [Pattern.check]:
            for y in range(FRAMESIZE.h):
                for x in range(FRAMESIZE.w):
                    if pattern == Pattern.check:
                        if x%2 == y%2:
                            self.mask[x,y] = True

        elif pattern == Pattern.font:
            self.mask = Mask()
            fnt = Font(font)
            msk = fnt.repertoire(size=self.mask.size())
            self.mask.addMask(msk)
        
        if invert: 
            self.mask.inv()
        self.mask = self.fluepdot.buffer.write(self.mask)
        log(str(self.mask))
        return False
    
    
    patterns = Pattern
    
    flags = [
        ("p:", "pattern=",     "pattern",    DefaultPattern, "pattern", lambda x: Pattern[x.lower()] ),
        Mode.FLAG["invert"],
        Mode.FLAG["font"],
    ]        
    
