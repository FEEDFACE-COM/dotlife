
import random

from dotlife.util import *

import fliplife
from fliplife import FRAMESIZE, Mask


class Test(fliplife.mode.Mode):
    
    def run(self,**params):
        info("start test")
        self.mask = self.draw(params)
        return False


    
    def draw(self,invert,**params):
        log(str(self.mask))
        return self.mask


    
