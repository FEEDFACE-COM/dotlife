
import random

import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.font import Font

import fliplife
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot


class Exec(fliplife.mode.Mode):
        
    
    def run(self,randomize,x,y,font,rem=None,**params):

        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        
        self.randomize = randomize
        self.cmd = 'date "+%F %T %z"'
        if type(rem) == type([]):
            self.cmd = " ".join(rem)
        elif type(rem) == type("") and rem != "":
            self.cmd = rem

        info("start exec: {:s}".format(self.cmd))

        self.font = Font.Font(font)
        log(str(self.font))

        self.draw(x,y,font,**params)

        return True
    

    def draw(self,x,y,font,**params):
        txt = b''
        try:
            txt,err,ret = shell(self.cmd)
        except OSError as ex:
            raise Error("fail run {:s}: {:s}".format(self.cmd,str(ex)))
        txt = txt.decode()
        txt = txt.rstrip()
        log("exec {:s}: {:s}".format(self.cmd,str(txt)))

        msk = self.font.render(txt)

        if self.randomize:
            w = FRAMESIZE.w - msk.size().w
            h = FRAMESIZE.h - msk.size().h
            x = random.randint(0,w-1)
            y = random.randint(0,h-1)
        
        debug("render text {:d}/{:d}: {:s}".format(x,y,txt))

#        self.mask = self.fluepdot.buffer.text(x,y,font,txt)
        
        self.mask = Mask()
        self.mask.mask(msk,pos=Position(x,y))
        self.mask = self.fluepdot.buffer.write(self.mask)
        
        log(str(self.mask))
        return self.mask
