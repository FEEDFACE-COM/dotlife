

from dotlife import *
from dotlife.util import *
from dotlife.math import *

from dotlife.pattern import PATTERN
from dotlife.buffer import Buffer
import dotlife.plasma as plasma

from dotlife.palette import Palette
from dotlife.clock import Timer

from oledlife.mode import Mode



def Init(timer):
    return Plasma(timer)



class Plasma(Mode):

    def __init__(self,timer):
        super().__init__(timer)
        self.timers = [
            Timer(timer.duration*1.3),
            Timer(timer.duration*1.9),# - timer.duration/2.),
            Timer(timer.duration*2.3),# - timer.duration/3.),
            Timer(timer.duration*2.9),# - timer.duration/5.),
        ]
        self.plasma = plasma.Plasma()
        self.freq0, self.freq1 = PI,PI
        
    def draw(self):
        phase0,phase1 = 0.,0.
        amp0,amp1 = 1.,1.

        
        self.freq0 = (self.timers[2].sin() * 4. + 4. + 1. ) / 4. * PI
        self.freq1 = (self.timers[3].sin() * 4. + 4. + 1. ) / 4. * PI

        phase0 = math.cos( self.timers[0].cycle() )
        phase1 = math.cos( self.timers[1].cycle() )
        
        if self.debug:
            self.freq0 = PI
            self.freq1 = PI
            phase0 = 0.
            phase1 = 0.
            
        
        
        fun0 = plasma.Fun( amp=amp0, freq=self.freq0, phase=phase0)
        fun1 = plasma.Fun( amp=amp1, freq=self.freq1, phase=phase1)

        ret = self.plasma.buffer(fun0=fun0,fun1=fun1,op=Operation.Add,palette=Palette.Polynom())

        return ret


    def __str__(self):
        return "plasma f{:.1f} f{:.1f}".format(self.freq0/PI,self.freq1/PI)

        
