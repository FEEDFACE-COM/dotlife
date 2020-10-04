
from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import framebuffer, mask


class Read(fliplife.mode.Mode):
    
    
    def run(self,**params):
        info("start read")
        
        self.mask = self.framebuffer.read()
        log(str(self.mask))
        return False
    
    def draw(self):
        return self.mask
