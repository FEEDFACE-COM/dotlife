
import random

from dotlife.util import *

import fliplife
from fliplife.mode import Mode
from fliplife import FRAMESIZE, Mask


class Test(Mode):
    
    def start(self,**params):
        info("start test")
        self.mask = self.draw(**params)
        return False


    
    def draw(self,**params):
        log(str(self.mask))
        return self.mask


    
