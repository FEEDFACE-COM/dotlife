
import random

from dotlife.util import *


import fliplife
from fliplife import Mask, FRAMESIZE




class Gauss(fliplife.mode.Mode):
    
    def run(self,**params):
        info("start gauss")
        self.mask = Mask()
        for y in range(FRAMESIZE.h):
            for x in range(FRAMESIZE.w):
                if random.gauss(1.,0.) > 1.:
                    self.mask[x,y] = True
        
        
        log(str(self.mask))
        self.mask = self.fluepdot.buffer.write(self.mask)
        log(str(self.mask))
        
        return False
    

        

