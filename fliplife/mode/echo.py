
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE, DEFAULT_FONT
from fliplife.fluepdot import Fluepdot

from dotlife.font import Font

class Echo(Mode):
        
    
    def run(self,randomize,x,y,font,fixed,msg=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        self.randomize = randomize
        
        self.font = Font(font)
        log(str(self.font))
        
        self.msg = "hello, world."
        if msg:
            self.msg = msg

        info("start echo: {:s}".format(self.msg))
        

        self.buf = self.font.render(self.msg,fixed=fixed,space=4)
        log(str(self.buf))
        
        self.mask = self.draw(x,y,**params)
        return True
    

    def draw(self,x,y,**params):
        pos = Position(x,y)
        if self.randomize:
            w = FRAMESIZE.w - self.buf.size().w
            h = FRAMESIZE.h - self.buf.size().h
            pos.x = random.randint(0,w-1)
            pos.y = random.randint(0,h-1)


        self.mask = Mask() #self.fluepdot.buffer.read()
        self.mask.addMask(self.buf,pos=pos)
        ret = self.fluepdot.buffer.write(self.mask)
        info(str(self.mask))
        return ret 
        
    flags = [
        Mode.FLAG("font"),
        Mode.FLAG("x"),
        Mode.FLAG("y"),
        Mode.FLAG("randomize"),
        ("F","fixed","fixed",False,"fixed font width", None),
        (None, None,            "msg",                 "hello, world.",           "message",                                 None),
    ]
    
    
