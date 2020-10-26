
import random

from dotlife.util import *

from dotlife.font import Font,FONT
from dotlife.effects import Axis, Border, Morph, Morph2

from fliplife import Mask, FRAMESIZE, DEFAULT_FONT
from fliplife.mode import Mode

from enum import auto

    
class Style(Enum):
    check = auto()
    gauss = auto()
    font = auto()
    axis = auto()
    border = auto()



class Fill(Mode):


    Style = Style
    DefaultStyle = Style.check
    DefaultFont = FONT.font3x5
    
    
    def start(self,style,invert,font,offset,**params):
        log("start fill with {:s}{:s}".format(str(style)," [invert]" if invert else ""))

        self.font = Font(font)
        self.offset = offset
        
        log("before:\n"+str(self.mask))
        
        msk = self.render(style,invert,**params)
        self.mask.addMask(msk)
        log("after:\n"+str(self.mask))
        
        return True
    
    

    def render(self,style,invert,cutoff,**params):
    
        ret = Mask()
        
    
        if style == Style.check:
            for y in range(FRAMESIZE.h):
                for x in range(FRAMESIZE.w):
                    if x%2 != y%2:
                        ret[x,y] = True

        elif style == Style.gauss:
            for y in range(FRAMESIZE.h):
                for x in range(FRAMESIZE.w):
                    if random.gauss(0.,1.) > cutoff:
                        ret[x,y] = True

        elif style == Style.font:
            fill = self.font.render_repertoire(offset=self.offset,size=self.mask.size())
            self.offset += 1
            ret.addMask(fill)
        
        elif style == Style.axis:
            fill = Axis(self.mask.size())
            ret.addMask(fill)

        elif style == Style.border:
            fill = Border(self.mask.size())
            ret.addMask(fill)
        
        if invert: 
            ret = ret.inverse()
    
        return ret

    
    def draw(self,style,invert,**params):
        self.offset += 1
        self.mask = self.render(style,invert,**params)
        return self.mask
    

    
    flags = [
        ("o:", "offset=",      "offset",                  0, "offset",  lambda x: int(x)             ),
        ("c:", "cutoff=",      "cutoff",                0.5, "cutoff",  lambda x: float(x)             ),
        Mode.FLAG("style",DefaultStyle),
        Mode.FLAG("invert"),
        Mode.FLAG("font",DefaultFont),
    ]        
    
