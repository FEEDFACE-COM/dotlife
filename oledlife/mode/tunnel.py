
import dotlife
from dotlife.pattern import *
from dotlife.mask import *
from dotlife.buffer import *
from dotlife.util import *
from dotlife.tunnel import Tunnel
from dotlife.palette import *
from dotlife.clock import Timer
from dotlife.math import *

from oledlife import FRAMESIZE 
from oledlife.mode import Mode


class Tunnel(Mode):

    def start(self,**params):
        self.tunnel = dotlife.tunnel.Tunnel()
        self.timers = [
            Timer(1.*self.timer.duration*1.),
            Timer(1.*self.timer.duration*1.9 * 7.),
            Timer(1.*self.timer.duration*2.3 * 5.),
        ]
        pattern0 = dotlife.pattern.Pattern.HEXDIGIT.value[0]
        pattern1 = dotlife.pattern.Pattern.HEXDIGIT.value[0xf]
        
#        self.mask = dotlife.mask.Mask(False,(8,8))
#        self.mask.mask( dotlife.mask.Mask.Load( dotlife.pattern.PATTERN.LOVE.value), (1,1)) 
#        self.mask = self.mask.inverse()

        self.mask = mask.Mask.Checkers(size=FRAMESIZE)
        return True
        

    def draw(self,**params):
        ret = Buffer()
        

        freq0,freq1 = TAU, TAU
        phase0,phase1 = 0.,0.
        amp0, amp1 = 1.,1.


        freq0 = PI  + 1. * self.timers[0].sin0() * PI
        
        phase0 = self.timers[1].cycle()

#        phase0 = self.timers[0].sin()
#        phase1 = self.timers[1].cycle()

        if self.debug:
            freq0 = TAU
            freq1 = TAU
            phase0 = 0.
            phase1 = 0.


#        fun0 = Fun( amp=amp0, freq=freq0, phase=phase0)
#       fun1 = Fun( amp=amp1, freq=freq1, phase=phase1)

        radius = 5./8.
        center = (0. + 1.49 * self.timers[1].sin() , 0. + 1.48 * self.timers[2].sin() )
#        center = (2.0 * self.timers[1].sin(), 0 )
        palette = Palette.Polynom().append( Palette.Polynom().reverse() ).add(3)
#        palette = Palette.Sine( 1./1., 32. ).add(3)
        
        palette = Palette( [1+x for x in range(16)] + [1+15-x for x in range(16)] )

        palette = Palette.Polynom()
        palette = palette.append( Palette.Polynom().reverse() ).add( 4 )
        depth = 1. - self.timers[0].linear()

        cx = self.timers[1].sin() * -7. 
        cy = self.timers[2].sin(phase=PI) * -7. 
        center = (cx,cy)
        
        
        if self.debug:
            center = (3.5,3.5)
    
        
#        self.mask= mask.Mask(size=(8,8))
#        for y in range(8):
#            for x in range(8):
#                self.mask[x,y] = (x%2 != y%2)
        
        back = self.tunnel.buffer(radius=radius,depth=depth,palette=palette,center=center,mask=self.mask)
        ret.add(back)

        front = self.tunnel.buffer(radius=radius,depth=depth+0.5,palette=palette,center=center,mask=self.mask.inverse())
        ret.add(front)
        
        
        return ret
        
        
