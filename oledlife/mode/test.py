
from dotlife import *
from dotlife.util import *
from oledlife.mode import *

from oledlife import Mask, Buffer, FRAMESIZE
import dotlife.pattern
import dotlife.life

from dotlife import tunnel

class Style(Enum):
    none = lambda x: Buffer(),
    tunnel = lambda x: x.tunnel.buffer(),

class Test(Mode):


    Pattern = dotlife.life.Pattern
    
    Style = Style
    DefaultStyle = Style.none

    
    def start(self,style,pattern,step,flip,light,**params):
        info("start test {:}".format(pattern))

        self.tunnel = dotlife.tunnel.Tunnel(duration=self.timer.duration,radius=5./8.)
        
        self.render, = style.value

        self.life = dotlife.life.Life(size=FRAMESIZE)        

        mask = pattern.Mask(flip=flip,step=step)
        debug(str(mask))
                
        
        self.life.spawn(pattern,pos=None)
        self.buffer = Buffer().addMask(self.life,light=light)
        
        
        return True
    
    def step(self,style,light,**params):
        self.life.step()
        self.buffer = Buffer().addMask(self.life,light=light)
        
    
    def draw(self,style,pattern,step,light,**params):
        c = 0
#        debug("draw life {:}#{:d}".format(pattern,c))
 
        self.buffer = self.render(self)
        return self.buffer.addMask( self.life, light=light )
        
#        return self.buffer
#        
#        pos = Buffer().centerForMask(self.mask)
#        buf = Buffer().addMask(self.mask,light=light,pos=pos)
#        return buf
        


    flags = [
        Mode.FLAG("step"),
        Mode.FLAG("flip"),
        Mode.FLAG("style",DefaultStyle),
        Mode.FLAG("pattern",Pattern.glider),
        ("l:","light=","light",1,"brightness",lambda x: int(x) ),
    ]
    