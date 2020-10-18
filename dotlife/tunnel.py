
import dotlife
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.math import *
from dotlife.util import *
from dotlife.palette import Palette
from dotlife.clock import Timer
import math

class Tunnel():


    def __init__(self,duration,radius,center=None):
        self.timers = [
            Timer(duration*1.),
            Timer(duration*1.9 * 7.),
            Timer(duration*2.3 * 5.),
        ]
        self.radius = radius

        self.palette = Palette.Polynom()
        self.palette = self.palette.append( Palette.Polynom().reverse() ).add( 4 )



    def d(x,y,ctr=(3.5,3.5)):
        cx,cy = ctr
        return math.sqrt( (x-cx)*(x-cx) + (y-cy)*(y-cy) )



    def buffer(self,off=0,):
        ret = Buffer()
        
        depth = 1. - self.timers[0].linear()
        
        freq0,freq1 = TAU, TAU
        phase0,phase1 = 0.,0.
        amp0, amp1 = 1.,1.

        freq0 = PI  + 1. * self.timers[0].sin0() * PI
        phase0 = self.timers[1].cycle()
        
        center = Position(3.5,3.5)
        center.x += self.timers[1].sin() * -3. 
        center.y += self.timers[2].sin(phase=PI) * -3. 
        
        
#        debug(str(palette))
        for y in range(ret.h):
            for x in range(ret.w):
                deltaMax = Tunnel.d(ret.w-1,ret.h-1,ctr=(0,0))
                delta = Tunnel.d(x,y,ctr=(center.x,center.y))
                idx = self.palette.idx( self.radius * (delta/deltaMax) + depth+off )
                ret[x,y] = self.palette[ idx % self.palette.length ]

                if False and x  == y:
                    debug("{:2d}/{:2d}  d{}  ∂{:.1f}  idx #{:5.1f}/{:d} col 0x{:02x}".format(x,y,depth+off,delta,idx,palette.length,palette[idx] ))
                
        
        return ret

