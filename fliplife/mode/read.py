
from dotlife.util import *


import fliplife
from fliplife import FRAMESIZE


class Read(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start read")
        
        self.mask = self.fluepdot.buffer.read()
        log(str(self.mask))
        return False
    
    def draw(self):
        return self.mask
