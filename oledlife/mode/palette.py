import dotlife
from dotlife.pattern import *
from dotlife.mask import *
from dotlife.buffer import *
from dotlife.util import *
from dotlife.mode import Mode
from dotlife.plasma import Plasma, Fun
import dotlife.palette as palette
from dotlife.clock import Timer
from dotlife.math import *

def Init(timer):
    return Palette(timer)


class Palette(Mode):
    
    
    def __init__(self,timer):
        super().__init__(timer)
        self.palette = palette.Palette.Linear()


    def draw(self):
    
        p = (self.timer.count / 2)
#        p = self.timer.count

        if p % 4 == 0:
            self.palette = palette.Palette.Linear()
        elif p % 4 == 1:
            self.palette = palette.Palette.Quadratic()
        elif p % 4 == 2:
            self.palette = palette.Palette.Polynom()
        elif p % 4 == 3:
            self.palette = palette.Palette.Sine()


#        self.palette = palette.Palette.Polynom()
        self.palette = palette.Palette.Sine(1.)
        pal = self.palette
        c = 16
#        c = self.timer.count
        buffer = Buffer()
        for y in range(int(buffer.h/2)):
            for x in range(buffer.w):
                buffer[x,y] = pal[c % pal.length]
                c += 1
        for y in range(int(buffer.h/2),buffer.h):
            for x in range(buffer.w):
                buffer[x,y] = pal[pal.length - c % pal.length]
                c += 1

#        buffer.mul( self.timer.sin0() * 0x20 + 0x8)
        return buffer


    def __str__(self):
        return "{}".format(self.palette)
