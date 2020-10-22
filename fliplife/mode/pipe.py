
import sys, random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.font import Font, FONT

class Pipe(Mode):
        
    
    def start(self,font,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        

        self.font = Font(font)
        log(str(self.font))
        
        info("start pipe".format())
        

        if font == FONT.font3x5:        
            self.pos = [ Position(0,2), Position(0,9) ]
            self.buffer = [ " ", " " ]
        elif font == FONT.font5x7:
            self.pos = [ Position(0,0), Position(0,9) ]
            self.buffer = [ " ", " " ]
        else:
            self.pos = [ Position(0,0) ]
            self.buffer = [ " " ]
        self.rows = len(self.buffer)
        


#        self.buf = self.font.render(self.msg)
#        log(str(self.buf))
        
        self.mask = self.draw(**params)
        
        
        
        while True:
            line = sys.stdin.readline()
            if not line:
                log("end of file.")
                break
            debug("read "+line)
            self.buffer[1] = self.buffer[0]
            self.buffer[0] = line.rstrip()[:30]
            self.draw(**params)
        
        return False
    

    def draw(self,**params):
        
        pos = Position(0,0)

        self.mask = Mask() #self.fluepdot.buffer.read()
        for i in range(self.rows):
            try:
                self.mask.addMask( self.font.render( self.buffer[i]), pos=self.pos[i] )
            except Error as x:
                pass

#        self.mask.mask(self.buf,pos=pos)
        ret = self.fluepdot.buffer.write(self.mask)
        info(str(self.mask))
        return ret 
        
    flags = [
        Mode.FLAG("font"),
    ]
        
