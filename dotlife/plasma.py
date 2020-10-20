
import dotlife
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.math import *
from dotlife.util import *
from dotlife.palette import Palette

from dotlife.time import Timer


class Fun():  # fun( [0..π..2π] ) => [ 0 .. 1 .. 0 ]
    
    def __init__(self,amp=1.0,freq=1.0*PI,phase=0.0): 
        self.amp,self.freq,self.phase = amp,freq,phase
    
    def __call__(self,x):
        return sine(x,self.amp,self.freq,self.phase)

class Nop():
    def __init__(self):
        pass
        
    def __call__(self,x):
        return 0.


class Plasma():


    def __init__(self,duration,op=Operation.add,palette=Palette.Linear()):
        self.timers = [
            Timer(duration*1.3),
            Timer(duration*1.9),
            Timer(duration*2.3),
            Timer(duration*2.9),
        ]
        self.op = op
        self.palette = palette

    def buffer(self,off=0.):
        ret = Buffer()
        
        phase0,phase1 = 0.,0.
        amp0,amp1 = 1.,1.

        
        self.freq0 = (self.timers[2].sin() * 4. + 4. + 1. ) / 4. * PI
        self.freq1 = (self.timers[3].sin() * 4. + 4. + 1. ) / 4. * PI

        phase0 = off+math.cos( self.timers[0].cycle() )
        phase1 = off+math.cos( self.timers[1].cycle() )
        
        
        fun0 = Fun( amp=amp0, freq=self.freq0, phase=phase0)
        fun1 = Fun( amp=amp1, freq=self.freq1, phase=phase1)
        
        
        for y in range(ret.h):
            for x in range(ret.w):
                val0 = fun0( float(x/ret.w) ) if fun0 else 0.0
                val1 = fun1( float(y/ret.h) ) if fun1 else 0.0
                val = val0
                if self.op == Operation.add:
                    val = val0 / 2.
                    val+= val1 / 2.
                elif self.op == Operation.sub:
                    val = val0 / 2.
                    val-= val1 / 2.         

                ret[x,y] = self.palette[ self.palette.idx( val ) ]
                
        return ret
    
