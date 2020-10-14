
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.clock import Clock
from dotlife.font import Font
from dotlife.effects import Morph, Morph2, Axis, Scan

class Scroll(Mode):
        
    
    def run(self,font,msg=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        
        self.font = Font(font)
        debug(str(self.font))
        
        self.msg = "hello, world."
        if msg:
            self.msg = msg

        info("start scroll: {:s}".format(self.msg))
        

        
        self.mask = Mask()
        self.text = self.font.render(self.msg,fixed=True)

        p0 = int(math.floor(FRAMESIZE.w / (self.font.size.w+1)))
        
        p1 = p0 - len(self.msg)
        
        self.pos0 = Position((self.font.size.w+1)*int(p1/2),0)
        
#        self.pos0 = Position(int(FRAMESIZE.w/2)-int(self.text.w/2), 0 )
        
        self.mask.addMask(self.text,pos=self.pos0,wrap=True)
        
        self.fluepdot.buffer.write(self.mask)
        
        self.l = int(self.text.w/(self.font.size.w+1))
        self.k = 0
        
        return True
    
    
    
    

    def draw(self,**params):

        ret = []

        k = self.k
        L = self.text.w
        
        W,H = self.font.size.w+1, self.font.size.h+1


        next = Mask()
        pos0 = Position(-W,0)
        pos1 = Position(k*W,0)


        if k != 0:
            txt0 = self.text.subMask(size=Size(k*W,H))
            next.addMask(txt0,pos=self.pos0+pos0,wrap=True)
        
        if self.l-k != 0:            
            txt1 = self.text.subMask(pos=Position((k)*W,0),size=Size((self.l-k)*W,H))
            next.addMask(txt1,pos=self.pos0+pos1,wrap=True)


#        log("from\n"+str(self.mask))
#        log("to\n"+str(next))

        steps = Morph2(self.mask,next)


        for i in range(len(steps)):
            step = steps[i]
            ret += [ step ]
            self.mask = step
        

        
        self.k += 1
        if self.k > self.l:
            log("step")
            self.k = 0
            self.pos0.x -= W
            if self.pos0.x <= -L:
                self.pos0.x+= FRAMESIZE.w
                

        return ret

        
    flags = [
        Mode.FLAG["font"],
        ("P:","pause=",       "pause",                 1.0,                        "pause",                              lambda x: int(x) ),
        (None, None,            "msg",                 "hello, world.",           "message",                                 None),
    ]
    
    
