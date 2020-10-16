
import dotlife
from dotlife import *
from dotlife.pattern import *

#from dotlife.mask import *
from dotlife.buffer import Buffer
#from dotlife.util import *
#from dotlife.mode import Mode
from dotlife.plasma import Plasma, Fun
from dotlife.palette import Palette
from dotlife.clock import Timer
from dotlife.math import *

from dotlife.util import *

import oledlife
from oledlife.mode import Mode
from oledlife import Mask, FRAMESIZE



class FYI(Mode):

    
    def start(self,**params):
        log("start FYI")
        pattern = dotlife.pattern.PATTERN.FYI.value
        self.plasma = Plasma()
        self.mask = Mask()
        self.mask.addMask( dotlife.mask.Mask.Load(pattern), pos=Position(0,2) )
        self.timers = [
            Timer(1.*self.timer.duration*2.),
            Timer(1.*self.timer.duration*3.),
            Timer(1.*self.timer.duration/5.),
            Timer(1.*self.timer.duration/3.),
        ]
        info(str(self.mask))
        return True
    
    
    
    def draw(self,**params):
        ret = Buffer()
        off = self.timer.count=1 * PI
        phase = self.timer.cycle()
        
        freq0,freq1 = PI,PI
        phase0,phase1 = 0.,0.
        amp0, amp1 = 0.9,0.9


        phase0 = self.timers[0].cycle()
        phase1 = self.timers[1].cycle()

        
        if self.debug:
            freq0 = PI
            freq1 = PI
            phase0 = PI
            phase1 = PI

        
        
        fun0 = Fun( amp=1., freq=PI, phase=phase0+PI)
        fun1 = Fun( amp=1., freq=PI, phase=phase1)
        
        offset = PI
        fun2 = Fun( amp=1., freq=PI, phase=phase0+offset+PI)
        fun3 = Fun( amp=1., freq=PI, phase=phase1+offset)


        back = self.plasma.buffer(fun0,fun1,palette=Palette.Polynom(),mask=self.mask)
        front = self.plasma.buffer(fun2,fun3,palette=Palette.Polynom(),mask=self.mask.inverse())

        ret.add(front)
        ret.add(back)
        return ret
        
        



