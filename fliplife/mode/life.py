


import dotlife
from dotlife import * 
from dotlife.util import *
from dotlife import math
from dotlife import life

import fliplife
from fliplife.mode import Mode 
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

class Style(Enum):


    read = auto()

    class blinkers():
        def fun(lifE,count):
            for i in range(count):
                step = Random.Number(0,1)
                pos = Random.Position(FRAMESIZE)
                #step = random.randint(0,1)
                #pos = Position(random.randint(0,FRAMESIZE.w), random.randint(0,FRAMESIZE.h))
                lifE.spawn(life.Pattern.blinker, pos=pos, step=step)
            return

    class gliders():
        def fun(lifE,count):
            for i in range(count):
                step = Random.Number(0,4)
                flip = Random.Choice( Flip )
                pos =  Random.Position( FRAMESIZE )
                #step = random.randint(0,4)
                #flip = random.choice( list( Flip.__members__.values() ))
                #pos = Position(random.randint(0,FRAMESIZE.w), random.randint(0,FRAMESIZE.h))
                lifE.spawn(life.Pattern.glider, pos=pos, step=step, flip=flip)
            return

class Life(Mode):

    Style = Style
    DefaultStyle = Style.read


    
    def start(self,style,count,wrap,**params):
        info("start life")
        self.offset = Position(0, 0)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        if style == Style.read:
            buf = self.fluepdot.buffer.read()
            self.life = life.Life(wrap=wrap,mask=buf)
            return True

        buf = Mask(size=FRAMESIZE)
        self.life = life.Life(wrap=wrap, size=buf.size())

        style.value.fun(self.life,count)
        return True
        
    
    def draw(self,**params):
        debug("{:s}".format(str(self.life)))
        self.life.step()
        return Mask(mask=self.life)


    
    flags = [
        Mode.FLAG("style",DefaultStyle),
        Mode.FLAG("count", 16),
        ("w", "wrap", "wrap", True, "wrap edges", None)
    ]
