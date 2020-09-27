

from dotlife.util import *
from dotlife.mode import Mode
from dotlife.buffer import Buffer
from dotlife.mask import Mask
from dotlife.palette import Palette

def Init(timer):
    return Pulser(timer)


class Pulser(Mode):
    
    def __init__(self,timer):
        super().__init__(timer)
        self.mask=Mask.Load("""
    [][]
    [][]
[][]    
[][]    
""")
        
    
    def draw(self):

        pal = Palette.Sine()


#        pal = Palette.Polynom().append( Palette.Polynom().reverse() )

        ret = Buffer()
        for y in range(ret.h):
            for x in range(ret.w):
                idx = pal.idx( y*ret.w + x + 0*self.timer.linear())
                ret[x,y] = pal[idx % pal.length ] 

#        ret.tile(self.mask,light=0x0)
        return ret


    def step(self):
        super().step()
        self.mask.inv()
