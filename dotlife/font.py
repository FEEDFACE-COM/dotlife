
from dotlife import *
from dotlife.util import *


from dotlife.mask import Mask

from dotlife.fonts import font3x5, fixed3x5, font5x5, font5x7, blinkenlights


def debug(s): pass


class FONT(Enum):
    fix3x5         = fixed3x5
    font3x5        = font3x5
    font5x5        = font5x5
    font5x7        = font5x7
    blinkenlights  = blinkenlights


class Font:

    def __init__(self,font):
        try:
            self.alphabet = {}
            self.spacer = 1
            try:
                self.spacer = font.value.Spacer
            except Exception as x:
                pass
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


    def desc(self):
        ret = ""
        for k,v in self.alphabet.items():
            m = Mask(v)
            ret += "glyph '{}' {}\n".format(k,str(m.size()))
        return ret

    def render_repertoire(self,size=Size(8,8),fixed=False,offset=0):
        ret = Mask(size=size)
        pos = Position(0,0)
        keys = list(self.alphabet)
        k = offset % len(keys)
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
                dim.w += self.size.w + self.spacer
            else:
                dim.w += self.glyph(c).w + self.spacer
        dim.h = self.size.h
    
        ret = Mask(size=dim)
        pos = Position(0,0)
        for c in txt:
            if c == " " and type(space) == type(0):
                buf = Mask(size=Size(space,self.size.h))
#                buf.inv()
            else:
                if fixed:
                    g = self.glyph(c)
                    p = Position(0,0)
                    p.x = int((self.size.w - g.w )/2)
                    t = Mask(size=self.size)
                    buf = t.addMask( g,pos=p )
                else:
                    buf = self.glyph(c)
            
            
#            buf.set(True)
            
            ret.addMask(buf,pos=pos)
            pos.x += buf.w + self.spacer


        debug("rendered {:s}: {:s}".format(str(ret.size()),txt))
        return ret

