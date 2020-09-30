
import random

from dotlife.util import *


import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask
from fliplife.http import *



class Gauss(fliplife.mode.Mode):
    
    def run(self,fun,**params):
        info("start gauss")
        self.mask = Mask(size=FRAMESIZE)
        for y in range(FRAMEHEIGHT):
            for x in range(FRAMEWIDTH):
                if random.gauss(1.,3.) > 4.:
                    self.mask[x,y] = True
        data = self.mask.toData()
        rsp = post(self.address,"framebuffer",None,data)

        self.mask = Mask.MaskFromResponse( rsp )
        log(str(self.mask))
        
        return False
    

        