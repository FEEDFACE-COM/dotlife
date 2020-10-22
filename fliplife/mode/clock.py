
import random, datetime

import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.math import *


import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.time import Clock
from dotlife.font import Font, FONT
from dotlife.effects import Morph, Morph2, Axis, Scan

from dotlife import invader
import dotlife.clock


        
        

class Clock(Mode):
    
    Style = dotlife.clock.Style
    DefaultStyle = dotlife.clock.Style.large
   
    
    def start(self,style,stamp,**params):
        self.fluepdot.rendering.setMode(Fluepdot.Mode.full)
        
        self.clock = dotlife.clock.Clock()

        
        self.now = datetime.datetime.now()
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp)
            self.start = datetime.datetime.now()
        
        
        info("start clock: {:s}".format(self.now.strftime("%F %T")))

        self.mask = self.clock.mask(size=FRAMESIZE,now=self.now,style=style)
        self.next = self.mask

        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        self.kuckuck = None
        self.hour = self.now.hour
        
        return True
    
    
    def step(self,style,stamp,**params):
        self.now = datetime.datetime.now()
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now() - self.start )

        self.next = self.clock.mask(size=FRAMESIZE,now=self.now,style=style)


    def draw(self,style,stamp,**params):


        if self.kuckuck and self.kuckuck.active():
            count = self.kuckuck.count + 1
            ret = Mask()
            info("kuckuck: "+str(self.kuckuck))
            idx = count % 2
            if count < 4:
                vader = invader.INVADER.one.Mask(idx).double()
                msk = Mask(size=Size((4+vader.w)*count, vader.h))
                for c in range(count):
                    pos = Position(c*(4+vader.w),0)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)
            elif count < 7:
                vader = invader.INVADER.one.Mask(idx)
                msk = Mask(size=Size((2+vader.w)*count, vader.h))
                for c in range(count):
                    pos = Position(c*(2+vader.w),0)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)
            else:
                vader = invader.INVADER.one.Mask(idx)
                msk = Mask(size=Size((2+vader.w)*ceil(count/2), 2*vader.h))
                for c in range(count):
                    if c % 2 == 0:
                        pos = Position(int(c/2)*(2+vader.w),0)
                    else:
                        pos = Position(int((c-1)/2)*(2+vader.w),vader.h)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)
            return ret

    
        hour = datetime.datetime.now().hour
        if stamp != "":
            hour = (datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now() - self.start )).hour
            
        if hour != self.hour:
            self.step(style,stamp,**params)
            times = hour%12 
            if times == 0:
                times = 12
            self.kuckuck = time.Clock.Timer(1500., times )
            debug("KUCKUCK {:}".format(self.kuckuck))
            self.hour = hour
            self.step(style,stamp,**params)
            prev = self.mask
            self.mask = self.next
            return prev



        if self.next != self.mask:
        
        
            if style in [Clock.Style.small,Clock.Style.large,Clock.Style.double]:
                m = Morph2(self.mask,self.next,steps=1)
                debug("from\n"+str(self.mask))
                debug("to\n"+str(self.next))
                self.mask = m[1]
                
                
            else:
                debug("to\n"+str(self.next))
                self.mask = self.next
                

        self.hour = hour
        return self.mask
        

        
    flags = [
        Mode.FLAG("style",DefaultStyle),
#        ("y:", "style=", "style", Style.large, "clock style", lambda x: Style[x] ),
        ("", "stamp=", "stamp", "", "timestamp", None ),
    ]
    
    





