

from dotlife.util import *
from dotlife.mode import Mode
from dotlife.buffer import Buffer
from dotlife.mask import Mask
from dotlife.palette import Palette



from oledlife.mode import Mode

class Pulser(Mode):
    
    def start(self,**params):
        self.mask = Mask().Load("""
    [][]
    [][]
[][]    
[][]    
""")
        return True
    
    def draw(self,**params):

        pal = Palette.Sine()


#        pal = Palette.Polynom().append( Palette.Polynom().reverse() )

        ret = Buffer()
        for y in range(ret.h):
            for x in range(ret.w):
                idx = pal.idx( y*ret.w + x + self.timer.linear())
                ret[x,y] = pal[idx % pal.length ] 

#        ret.tile(self.mask,light=0x0)
        return ret


    def step(self,**params):
        self.mask = self.mask.inverse()
