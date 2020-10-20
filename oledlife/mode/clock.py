
import random, datetime

import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.math import *


import fliplife
from oledlife.mode import Mode
from oledlife import Mask, Buffer, FRAMESIZE

from dotlife.time import Clock
from dotlife.font import Font, FONT
from dotlife.effects import Morph, Morph2, Axis, Scan

import dotlife.clock


        
        

class Clock(Mode):
    
    Style = dotlife.clock.Style
    DefaultStyle = dotlife.clock.Style.large
   
    
    def start(self,stamp,**params):
        self.clock = dotlife.clock.Clock()

        
        self.now = datetime.datetime.now()
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp)
            self.start = datetime.datetime.now()
        
        
        info("start clock: {:s}".format(self.now.strftime("%F %T")))

        self.mask = self.clock.mask(size=FRAMESIZE,now=self.now,style=Clock.Style.mini)

        radius = 5./8.
        self.tunnel = dotlife.tunnel.Tunnel(duration=self.timer.duration,radius=radius)

        return True
    
    
    def step(self,stamp,**params):
        info("FIRE")
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now() - self.start )
        else:
            self.now = datetime.datetime.now()

        self.mask = self.clock.mask(size=FRAMESIZE,now=self.now,style=Clock.Style.mini)


    def draw(self,stamp,back,**params):

        self.buffer = Buffer()

        front = self.tunnel.buffer(off=0.)
        self.buffer.add(front.addMask(self.mask,light=DARK))
        
        if back:
            back = self.tunnel.buffer(off=0.5)
            self.buffer.add(back.addMask(self.mask.inverse(), light=DARK))
        
        
        return self.buffer
        

        
    flags = [
        ("b", "back", "back", False, "", None),
        ("", "stamp=", "stamp", "", "timestamp", None ),
        Mode.FLAG("invert"),  
    ]
    
    





