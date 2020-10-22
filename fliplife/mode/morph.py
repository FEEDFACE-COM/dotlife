
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.time import Clock
from dotlife.font import Font
from dotlife.effects import Morph, Morph2

class Scroll(Mode):
        
    
    def run(self,font,msg=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)
        
        self.font = Font(font)
        debug(str(self.font))
        
        self.msg = "hello, world."
        if msg:
            self.msg = msg

        info("start scroll: {:s}".format(self.msg))
        

        
        self.mask = Mask()
        self.text = self.font.render(self.msg,fixed=True)
        
        self.pos0 = Position(int(FRAMESIZE.w/2)-int(self.text.w/2), 0 )
        self.pos1 = Position(int(FRAMESIZE.w/2)-int(self.text.w/2), 8 )
        
        self.mask.addMask(self.text,pos=self.pos0,wrap=True)
        self.mask.addMask(self.text,pos=self.pos1,wrap=True)
        
        self.fluepdot.buffer.write(self.mask)
        
        return True
    
    
    
    

    def draw(self,**params):

        ret = []

        next = Mask()
        next.addMask(self.text,pos=self.pos0,wrap=True)
        next.addMask(self.text,pos=self.pos1,wrap=True)

        steps = Morph2(self.mask,next)
        
        for i in range(len(steps)):
            step = steps[i]
            ret += [ step ]
            self.mask = step
        

        
        self.pos0.x += self.font.size.w+1
        if self.pos0.x >= FRAMESIZE.w:
            self.pos0.x = int(FRAMESIZE.w/2)-int(self.text.w/2)

        self.pos1.x -= self.font.size.w+1
        if self.pos1.x <= - self.text.w:
            self.pos1.x = int(FRAMESIZE.w/2)-int(self.text.w/2)

        return ret

        
    flags = [
        Mode.FLAG["font"],
        ("P:","pause=",       "pause",                 1.0,                        "pause",                              lambda x: int(x) ),
        (None, None,            "msg",                 "hello, world.",           "message",                                 None),
    ]
    
    
