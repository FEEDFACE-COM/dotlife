
import random

from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife.mask import Mask
from fliplife.http import *



class Echo(fliplife.mode.Mode):
        
    
    def run(self,randomize,msg,font,xoff,yoff,**params):

        self.data = " ".join(msg)
        self.params = {
            'font': font,
        }
        if xoff:
            self.params['x'] = int(xoff)
        if yoff:
            self.params['y'] = int(yoff)

        self.randomize = randomize

        info("start echo {:s}".format(self.data))
        mask = self.draw(**params)    
        log(str(mask))
        
        return True
    

    def draw(self,**params):
        
        if self.randomize:
            w = FRAMEWIDTH - (6*len(self.data))
            h = FRAMEHEIGHT - (8*1)
            self.params['font'] = 'fixed_5x8'
            self.params['x'] = int(random.random() * float(w))
            self.params['y'] = int(random.random() * float(h))
        
        info("echo {:s},{:s} {:s}".format("{:d}".format(self.params['x']) if self.params.get('x') else "","{:d}".format(self.params['y']) if self.params.get('y') else "",self.data))
        rsp = post(self.address,"framebuffer/text",self.params,data=self.data)
        return Mask.MaskFromResponse( rsp )
