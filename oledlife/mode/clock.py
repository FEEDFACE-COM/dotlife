
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

        
        self.now = datetime.datetime.now()
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp)
            self.start = datetime.datetime.now()
        
        
        info("start clock: {:s}".format(self.now.strftime("%F %T")))

        self.mask = self.render(size=FRAMESIZE,now=self.now)

        radius = 5./8.
        self.tunnel = dotlife.tunnel.Tunnel(duration=self.timer.duration,radius=radius)

        return True
    
    
    def step(self,stamp,**params):
        info("FIRE")
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now() - self.start )
        else:
            self.now = datetime.datetime.now()

        self.mask = self.render(size=FRAMESIZE,now=self.now)


    def draw(self,stamp,back,invert,**params):

        self.buffer = Buffer()

        front = self.tunnel.buffer(off=0.)
        if invert:
            self.buffer.add(front.addMask(self.mask,light=DARK))
        else:
            self.buffer.add(front.addMask(self.mask.inverse(),light=DARK))
        
        
        if back:
            back = self.tunnel.buffer(off=0.5)
            self.buffer.add(back.addMask(self.mask.inverse(), light=DARK))
        
        
        return self.buffer
        


    def render(self,size,now):
        ret = Mask(size=size)
        _,_,_,hour,minute,_,_,_,_ = now.timetuple()
        h0 = int(hour / 10)
        h1 = hour % 10
        m0 = int(minute/10)
        m1 = minute%10
        
        H0 = mask.Mask.Load( Clock.font33[ h0%10 ] )
        H1 = mask.Mask.Load( Clock.font33[ h1%10 ] )
        M0 = mask.Mask.Load( Clock.font33[ m0%10 ] )
        M1 = mask.Mask.Load( Clock.font33[ m1%10 ] )
        
        ret = ret.addMask(H0,Position(0,0))
        ret = ret.addMask(H1,Position(5,0))
        ret = ret.addMask(M0,Position(0,5))
        ret = ret.addMask(M1,Position(5,5))
        return ret
    
        
    flags = [
        ("b", "back", "back", False, "", None),
        ("", "stamp=", "stamp", "", "timestamp", None ),
        Mode.FLAG("invert"),  
    ]
    
    




    font44 = [ """
[][][][]
[]    []
[]    []
[][][][]
""","""
    []  
  [][]  
    []  
    []  
""","""
[][]    
    [][]
  []    
[][][][]
""","""
[][][][]
    [][]
      []
[][][][]
""","""
[]    []
[]    []
[][][][]
      []
""","""
[][][][]
[]     
    [][]
[][]  
""","""
[]      
[][][][]
[]    []
[][][][]
""","""
[][][][]
      []
    []  
    []  
""","""
  [][]
[][][][]
[]    []
[][][][]
""","""
[][][][]
[]    []
[][][][]
      []
"""]


    font33 = [
"""
[][][]
[]  []
[][][]
""","""
  []  
  []  
  []  
""", """
[]    
  []  
[][][]
""","""
[][][]
  [][]
[][][]
""","""
[]  []
[][][]
    []
""","""
[][][]
  []  
[][]  
""","""
[]    
[][][]
[][][]
""","""
[][][]
    []
    []
""","""
[][][]
[][][]
[][][]
""","""
[][][]
[][][]
    []
"""]    


    dots = ["""
      
      
      
""","""
      
  []  
      
""","""
[]    
      
    []
""","""
    []
  []  
[]    
""","""
[]  []
      
[]  []
""","""
[]  []
  []  
[]  []
""","""
[]  []
[]  []
[]  []
""","""
[]  []
[][][]
[]  []
""","""
[][][]
[]  []
[][][]
""","""
[][][]
[][][]
[][][]
"""]


