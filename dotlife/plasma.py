
import dotlife
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.math import *
from dotlife.util import *
from dotlife.palette import Palette


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


#    def __init__(self):
#        pass        


    def buffer(self,fun0=Fun(),fun1=Fun(), op=Operation.add, palette=Palette.Linear(), mask=None):
        ret = Buffer()
        for y in range(ret.h):
            for x in range(ret.w):
                if mask and mask[x,y] == False:
                    continue
                val0 = fun0( float(x/ret.w) ) if fun0 else 0.0
                val1 = fun1( float(y/ret.h) ) if fun1 else 0.0
                val = val0
                if op == Operation.add:
                    val = val0 / 2.
                    val+= val1 / 2.
                elif op == Operation.sub:
                    val = val0 / 2.
                    val-= val1 / 2.         

                ret[x,y] = palette[ palette.idx( val ) ]
                
        return ret
    
