
from dotlife import *
from dotlife.util import *
from oledlife.mode import *

from oledlife import Mask, Buffer, FRAMESIZE
import dotlife.pattern
import dotlife.life



class Test(Mode):


#    DefaultStyle = Style.grades
    Pattern = dotlife.life.Pattern
    

    
    def start(self,pattern,step,flip,light,**params):
        info("start test {:}".format(pattern))
        

        self.life = dotlife.life.Life(size=FRAMESIZE)        

        mask = pattern.Mask(flip=flip,step=step)
        debug(str(mask))
                
        pos = Buffer().centerForMask(mask)
        
        self.life.spawn(pattern,pos=pos)
        self.buffer = Buffer().addMask(self.life,light=light)
        
        
        return True
    
    def step(self,light,**params):
        debug("STEP")
        self.life.step()
        self.buffer = Buffer().addMask(self.life,light=light)
        
    
    def draw(self,pattern,step,light,**params):
        c = 0
#        debug("draw life {:}#{:d}".format(pattern,c))
        
        return self.buffer
        
        pos = Buffer().centerForMask(self.mask)
        buf = Buffer().addMask(self.mask,light=light,pos=pos)
        return buf
        


    flags = [
        Mode.FLAG("step"),
        Mode.FLAG("flip"),
        Mode.FLAG("pattern",Pattern.glider),
        ("l:","light=","light",1,"brightness",lambda x: int(x) ),
    ]
    