
from dotlife import *
from dotlife.util import *
from dotlife import font3x5

from dotlife.mask import Mask

class Font:


    def __init__(self,alphabet,size,empty):
        self.size = size
        self.empty = Mask.Load(empty)
        self.alphabet = {}
        for key,val in alphabet.items():
            try:
                self.alphabet[key] = Mask.Load(val)
            except Error as x:
                pass
        return


    def __str__(self):
        return "font {:d} chars, {:s}".format(len(self.alphabet),str(self.size))

    def repertoire(self,size=Size(8,8)):
        ret = Mask(size=size)
        pos = Position(0,0)
        keys = list(self.alphabet)
        k = 0 
        key = keys[k]
        while pos.y + self.size.h <= size.h+1:
            while pos.x + self.size.w <= size.w:
                ret.mask( self.alphabet[key], pos=pos )
                pos.x += self.size.w + 1
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


    @classmethod
    def Font3x5(self):
        fnt = Font(alphabet=font3x5.Alphabet,size=font3x5.Size,empty=font3x5.Empty)
        return fnt


    def render(self,txt):
        w = len(txt) * self.size.w + len(txt)-1
        h = self.size.h + 1
        
        ret = Mask(size=Size(w,h))
        pos = Position(0,0)
        for c in txt:
            msk = self.empty
            try:
                msk = self.alphabet[ c.upper() ]
                debug("glyph '{:s}' at {:s}".format(c,str(pos)))
            except KeyError as x:
                error("no glyph for char '{:s}'".format(c))
                pass
            ret.mask(msk,pos=pos)
            pos.x += self.size.w+1
        return ret
