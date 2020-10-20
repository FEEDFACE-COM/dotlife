import dotlife
from dotlife.pattern import *
from dotlife.mask import *
from dotlife.buffer import *
from dotlife.util import *
from dotlife.mode import Mode
from dotlife.plasma import Plasma, Fun
from dotlife.palette import PALETTE
from dotlife.time import Timer
from dotlife.math import *


from oledlife import FRAMESIZE, Buffer, Mask
from oledlife.mode import Mode

from enum import auto

class Style(Enum):
    scroll = auto()
    fade   = auto()
    all    = auto()

class Palette(Mode):
    
    Style = Style
    
    def start(self,palette,**params):
        self.palette = palette
        return True

    def draw(self,style,**params):

        pal = self.palette.value
        c = 16
        c = self.timer.count % pal.length

        buffer = Buffer()
        
        if style == Style.all:
            for y in range(int(buffer.h/2)):
                for x in range(buffer.w):
                    buffer[x,y+int(buffer.h/4)] = pal[c]
                    c += 1
                    c %= pal.length
        elif style == Style.fade:
            buffer = Buffer(size=FRAMESIZE,val=pal[c])
        elif style == Style.scroll:
            for y in range(buffer.h):
                for x in range(buffer.w):
                    buffer[x,y] = pal[c]
                c += 1
                c %= pal.length
                            
        return buffer

    flags = [
        Mode.FLAG("style",Style.all),
        ("P:","palette=","palette",PALETTE.linear,"palette",lambda x: PALETTE[x] ),
    ]
        
        
