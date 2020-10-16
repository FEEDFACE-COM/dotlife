
from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE


class Reset(Mode):
    
    
    def start(self,**params):
        log("start reset".format())
        
        self.fluepdot.buffer.write( Mask() )
        self.fluepdot.buffer.write( Mask().inverse() )
        self.fluepdot.buffer.write( Mask() )
                
        return False


    def draw(self,**params):
        return Mask()
                
    
    flags = []
