
import random

import dotlife
from dotlife import *
from dotlife.util import *



import fliplife
from fliplife.mode import Mode

from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.font import FONT, Font




class Echo(Mode):
        

    DefaultFont = FONT.font5x5
    
    def start(self,font,alignv,scroll,msg="hello, world",**params):
        dump(params)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.full)
        self.font = Font(font)
        self.msg = msg


        info("start echo: {:s}".format(self.msg))

        if scroll and alignv == AlignVertical.center:
            log("cannot scroll with center vertical alignment")
            scroll = False
        

        self.text = self.font.render(self.msg)
        log("text is {:}".format(self.text.size()))
        log(str(self.text))
        
        self.mask = self.draw(scroll,alignv,**params)
        return False
    

    def draw(self,scroll,alignv,alignh,**params):


        self.mask = Mask()
        if scroll and alignv in [AlignVertical.top, AlignVertical.bottom]:
            rest = Size(FRAMESIZE.w, FRAMESIZE.h - (self.font.size.h +1 ))
            top = Position(0,0)
            bot = Position(0, self.font.size.h + 1)

            prev = self.fluepdot.buffer.read()
            if alignv == AlignVertical.top:
                tmp = prev.subMask(pos=top,size=rest)
                self.mask.addMask(tmp,pos=bot)
            elif alignv == AlignVertical.bottom:
                tmp = prev.subMask(pos=bot,size=rest)
                self.mask.addMask(tmp,pos=top)


        pos = Position(0,0)
        if alignv == AlignVertical.top:
            pos.y = 0
        elif alignv == AlignVertical.center:
            pos.y = math.floor(abs(FRAMESIZE.h - self.text.h)/2)
        elif alignv == AlignVertical.bottom:
            pos.y = FRAMESIZE.h - self.text.h
            
        if alignh == AlignHorizontal.left:
            pos.x = 0
        elif alignh == AlignHorizontal.center:
            pos.x = math.floor(abs(FRAMESIZE.w - self.text.w)/2)
        elif alignh == AlignHorizontal.right:
            pos.x = FRAMESIZE.w - self.text.w

        
        self.mask.addMask(self.text,pos=pos)
        return self.mask


        
    flags = [
        ("S", "scroll", "scroll", False, "scroll line?", None),
        Mode.FLAG("font",DefaultFont),
        Mode.FLAG("msg"),
        Mode.FLAG("alignv",AlignVertical.center),
        Mode.FLAG("alignh",AlignHorizontal.center),
    ]
    
    
