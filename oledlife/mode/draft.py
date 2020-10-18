
import dotlife
from dotlife.pattern import *
from dotlife.mask import *
from dotlife.buffer import *
from dotlife.util import *
from dotlife.plasma import Plasma, Fun
from dotlife.palette import PALETTE, Palette
from dotlife.clock import Timer
from dotlife.math import *



from oledlife import FRAMESIZE, Buffer, Mask
from oledlife.mode import Mode

class Draft(Mode):
    
    
    def start(self,palette,**params):
        self.palette = Palette(color=[LIGHT,DARK,LIGHT,DARK])
        self.timers = [
            Timer(self.timer.duration*10),
            Timer(self.timer.duration*2.3),
        ]
        return True
        
    
    def ring(x,y,off=Position(0,0)):
        for s in range(8):
            if (x-off.x) < s or (x-off.x) >= FRAMESIZE.w-s:
                return s-1
            if (y-off.y) < s or (y-off.y) >= FRAMESIZE.w-s:
                return s-1
        return None
    
    def draw(self,**params):
        ret = Buffer()
        palette0 = Palette.Sine(amp=31,bias=1.)
        palette1 = Palette.Sine(amp=31,bias=1.,phase=1.*PI/6.)
        palette2 = Palette.Sine(amp=31,bias=1.,phase=2.*PI/6.)
        palette3 = Palette.Sine(amp=31,bias=1.,phase=3.*PI/6.)
        palette4 = Palette.Sine(amp=31,bias=1.,phase=4.*PI/6.)
        palette5 = Palette.Sine(amp=31,bias=1.,phase=5.*PI/6.)


#        palette0 = Palette(color=[DARK])
#        palette1 = Palette(color=[LIGHT])
#        palette2 = Palette(color=[LIGHT])
#        palette3 = Palette(color=[DARK])
#        palette4 = Palette(color=[DARK])
#        palette5 = Palette(color=[DARK])
        
        c = self.timer.count
        shade = [
            palette2.item(c),
            palette3.item(c),
            palette4.item(c),
            palette5.item(c),
            palette0.item(c),
            palette1.item(c),
            palette1.item(c),
            palette1.item(c),
        ]
        

        center = Position(0,0)
#        center.x += 2
#       center.y += -2
        for y in range(FRAMESIZE.h):
            for x in range(FRAMESIZE.w):
                s = Draft.ring(x,y,center)
                ret[x,y]= shade[s%len(shade)]
        
        return ret
        
        
        
    flags = [
        ("P:","palette=","palette",PALETTE.linear,"palette",lambda x: PALETTE[x] ),
    ]
        


