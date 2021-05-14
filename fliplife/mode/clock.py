
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
   
    
    def start(self,style,stamp,cuckoo,**params):
        self.fluepdot.rendering.setMode(Fluepdot.Mode.full)
        
        self.clock = dotlife.clock.Clock()
        self.timezone = datetime.datetime.now().astimezone().tzinfo
        
        self.now = datetime.datetime.now(self.timezone)
        if stamp != "":
            try:
                self.now = datetime.datetime.fromisoformat(stamp)
            except ValueError as x:
                raise Error(str(x))
            self.start = datetime.datetime.now(self.timezone)
        
        
        info("start clock: {:s}{:s}".format(self.now.strftime("%F %T")," [kuckuck]" if cuckoo else ""))

        self.mask = self.clock.mask(size=FRAMESIZE,now=self.now,style=style)
        self.next = self.mask

        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        self.kuckuck = None
        self.hour = self.now.hour
        
        return True
    
    
    def step(self,style,stamp,**params):
        self.now = datetime.datetime.now(self.timezone)
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now(self.timezone) - self.start )

        self.next = self.clock.mask(size=FRAMESIZE,now=self.now,style=style)


    def draw(self,style,stamp,cuckoo,**params):


        if self.kuckuck and self.kuckuck.active():
            hour = int(self.kuckuck.repeat/1)
            count = int(self.kuckuck.count/1) + 1
            ret = Mask()
            
            idx = self.kuckuck.count%2

            if 1 <= hour <= 4:
                vader = invader.INVADER.one.Mask(idx).double()
                msk = Mask(size=Size((4+vader.w)*hour, vader.h))
                for c in range(hour):
                    pos = Position(c*(4+vader.w),0)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)

            elif 5 <= hour <= 8:
                vader = invader.INVADER.one.Mask(idx)
                msk = Mask(size=Size((2+vader.w)*hour, vader.h))
                for c in range(hour):
                    pos = Position(c*(2+vader.w),0)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)
                
            elif 9 <= hour <= 12:
                vader = invader.INVADER.one.Mask(idx)
                msk = Mask(size=Size((2+vader.w)*ceil(hour/2), 2 * (vader.h)))
                for c in range(hour):
                    pos = Position(int(c/2)*(2+vader.w),0)
                    if c % 2 == 1:
                        pos.y += vader.h
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)

            return ret

    
        hour = datetime.datetime.now(self.timezone).hour
        if stamp != "":
            hour = (datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now(self.timezone) - self.start )).hour
            
        if cuckoo == True and hour != self.hour:
            self.step(style,stamp,**params)
            times = hour%12 
            if times == 0:
                times = 12
            self.kuckuck = dotlife.time.Clock.Timer(1500., times )
            debug("KUCKUCK {:}".format(self.kuckuck))
            self.hour = hour
            self.step(style,stamp,**params)
            prev = self.mask
            self.mask = self.next
            return self.draw(style,stamp,cuckoo,**params) # recurse once!



        if self.next != self.mask:
        
        
            if style in [Clock.Style.small,Clock.Style.large]:
                m = Morph2(self.mask,self.next,steps=1,flipcount=1)
                debug("to\n"+str(self.next))
                self.mask = m[1]
            elif style in [Clock.Style.split]:
                m = Morph2(self.mask,self.next,steps=1,flipcount=2)
                debug("to\n"+str(self.next))
                self.mask = m[1]
#            elif style in [Clock.Style.unix]:
#                m = Morph2(self.mask,self.next,steps=1,flipcount=4)
#                debug("to\n"+str(self.next))
#                self.mask = m[1]
            else:
#                debug("to\n"+str(self.next))
                self.mask = self.next
                

        self.hour = hour
        return self.mask
        

        
    flags = [
        Mode.FLAG("style",DefaultStyle),
        ("K","kuckuck","cuckoo",True,"kuckuck?", None ),
        ("", "stamp=", "stamp", "", "timestamp", None ),
    ]
    
    





