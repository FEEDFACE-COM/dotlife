

from dotlife import *
from dotlife.util import *
from dotlife.math import *

from dotlife.pattern import Pattern
from oledlife import Buffer
import dotlife.plasma as plasma

from dotlife.palette import Palette
from dotlife.clock import Timer

from oledlife.mode import Mode






class Plasma(Mode):

    def start(self,**params):
        self.timers = [
            Timer(self.timer.duration*1.3),
            Timer(self.timer.duration*1.9),# - timer.duration/2.),
            Timer(self.timer.duration*2.3),# - timer.duration/3.),
            Timer(self.timer.duration*2.9),# - timer.duration/5.),
        ]
        self.plasma = plasma.Plasma()
        self.freq0, self.freq1 = PI,PI
        return True
        
        
        
    def draw(self,**params):
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

        ret = self.plasma.buffer(fun0=fun0,fun1=fun1,op=Operation.add,palette=Palette.Polynom())

        return ret



        
