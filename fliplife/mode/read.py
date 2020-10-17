
from dotlife.util import *


import fliplife
from fliplife.mode import Mode
from fliplife import FRAMESIZE


class Read(Mode):
    
    
    def start(self,**params):
        info("start read")

        self.mask = self.fluepdot.buffer.read()
        return False
    
    def draw(self,**params):
        return self.mask
