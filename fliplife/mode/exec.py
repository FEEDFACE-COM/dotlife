
import random

from dotlife.util import *

from dotlife.buffer import Buffer

import fliplife
from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE
from fliplife import mask,framebuffer



class Exec(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,font,rem=None,**params):
        
        self.randomize = randomize
        self.cmd = 'date "+%F %T%z"'
        if type(rem) == type([]):
            self.cmd = " ".join(rem)
        elif type(rem) == type("") and rem != "":
            self.cmd = rem

        info("start exec: {:s}".format(self.cmd))

        self.draw(x,y,font,**params)

        return True
    

    def draw(self,x,y,font,**params):
        txt = b''
        try:
            txt,err,ret = shell(self.cmd)
        except OSError as ex:
            raise Error("fail run {:s}: {:s}".format(self.cmd,str(ex)))
        txt = txt.decode()
        log("ran {:s}: {:s}".format(self.cmd,str(txt)))
#        txt = " ".join(txt)
        log("txt is {:d}".format(len(txt)))
        if self.randomize:
            font = 'fixed_5x8'
            w = FRAMEWIDTH - (6*len(txt))
            h = FRAMEHEIGHT - (8*1)
            x = int(random.random() * float(w))
            y = int(random.random() * float(h))
        
        debug("render text {:d}/{:d}: {:s}".format(x,y,txt))
        self.mask = self.fluepdot.buffer.text(x,y,font,txt)
        log(str(self.mask))
        return self.mask
