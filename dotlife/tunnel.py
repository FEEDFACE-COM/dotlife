
import dotlife
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.math import *
from dotlife.util import *
from dotlife.palette import Palette
import math

class Tunnel():


    def d(x,y,ctr=(3.5,3.5)):
        cx,cy = ctr
        return math.sqrt( (x-cx)*(x-cx) + (y-cy)*(y-cy) )

    def buffer(self,depth=0,radius=1.,palette=Palette.Linear(),center=(0,0),mask=None):
        ret = Buffer()
#        debug(str(palette))
        for y in range(ret.h):
            for x in range(ret.w):
                if mask and mask[x,y] == False:
                    continue
                deltaMax = Tunnel.d(ret.w-1,ret.h-1,ctr=(0,0))
                delta = Tunnel.d(x,y,ctr=center)
                idx = palette.idx( radius * (delta/deltaMax) + depth )
                ret[x,y] = palette[ idx % palette.length ]



                if False and x  == y:
                    debug("{:2d}/{:2d}  d{}  ∂{:.1f}  idx #{:5.1f}/{:d} col 0x{:02x}".format(x,y,depth,delta,idx,palette.length,palette[idx] ))
                
        
        return ret

