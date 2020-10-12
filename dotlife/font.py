
from enum import Enum, auto

from dotlife import *
from dotlife.util import *


from dotlife.mask import Mask

from dotlife.fonts import font3x5, font5x7, blinkenlights


#def debug(s): pass


class FONT(Enum):
    font3x5        = font3x5
    font5x7        = font5x7
    blinkenlights  = blinkenlights

    def __str__(self):
        return self.name


class Font:

    def __init__(self,font):
        try:
            self.alphabet = {}
            self.size = font.value.Size
            self.empty = Mask.Load(font.value.Empty)
            for key,val in font.value.Alphabet.items():
                try:
                    self.alphabet[key] = Mask.Load(val)
                except Error:
                    pass
        except Exception as x:
            raise Error("font {} broken: {}".format(font.name,str(x)))


    def __str__(self):
        return "font {:d} chars, {:s}".format(len(self.alphabet),str(self.size))

    def repertoire(self,size=Size(8,8),fixed=False):
        ret = Mask(size=size)
        pos = Position(0,0)
        keys = list(self.alphabet)
        k = 0 
        key = keys[k]
        while pos.y + self.size.h <= size.h+1:
            while pos.x + self.size.w <= size.w:
                buf = self.glyph(key)
                if fixed and buf.w < self.size.w:
                    pass # TODO: add columns to buf                            
                ret.addMask( buf, pos=pos )
                pos.x += buf.w + 1
                k += 1
                k %= len(keys)
                key = keys[k]
            pos.x = 0
            pos.y += self.size.h + 1
            k += 1
            k %= len(keys)
            key = keys[k]
            
        info("repertoire:\n"+str(ret))
        return ret





    def glyph(self,char):
        ret = self.empty
        try:
            ret = self.alphabet[char]
#            debug("glyph '{:s}' is {:s}".format(char,str(ret.size())))
        except KeyError as x:
            error("no glyph for char '{:s}'".format(char))
        return ret
        

    def render(self,txt,fixed=False,space=None):
        dim = Size()
        for c in txt:
            if fixed:
                dim.w += self.size.w + 1
            else:
                dim.w += self.glyph(c).w + 1
        dim.h = self.size.h + 1
    
        ret = Mask(size=dim)
        pos = Position(0,0)
        for c in txt:
            if c == " " and type(space) == type(0):
                buf = Mask(size=Size(space,self.size.h))
            else:
                buf = self.glyph(c)
            if fixed and buf.w < self.size.w:
                pass # TODO: add columns to buf                            
            ret.addMask(buf,pos=pos)
            if fixed:
                pos.x += self.size.w + 1
            else:
                pos.x += buf.w + 1
        debug("rendered {:s}: {:s}".format(str(ret.size()),txt))
        return ret

