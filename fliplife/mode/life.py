


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

    class gliders(): # seed 61848383
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

    class spaceships():
        def fun(lifE,count):
            for i in range(count):
                step = Random.Number(0,4)
                flip = Random.Choice( Flip )
                pos =  Random.Position( FRAMESIZE )
                pat = Random.Choice( [life.Pattern.lwss, life.Pattern.mwss,life.Pattern.hwss] )
                #step = random.randint(0,4)
                #flip = random.choice( list( Flip.__members__.values() ))
                #pos = Position(random.randint(0,FRAMESIZE.w), random.randint(0,FRAMESIZE.h))
                lifE.spawn(pat, pos=pos, step=step, flip=flip)
            return


    # class schick():
    #     def fun(lifE,count):
    #         lifE.spawn(life.Pattern.coe, pos=Position(4,4), step=0, flip=Flip.horizontal)
    #         lifE.spawn(life.Pattern.schick, pos=Position(46,4), flip=Flip.vertical)
    #         lifE.spawn(life.Pattern.coe, pos=Position(84,4), flip=Flip.noflip)
    #         return

    class fireships():
        def fun(lifE,count):
            lifE.spawn(life.Pattern.fireship, pos=Position(4,4))
            if count > 1:
                lifE.spawn(life.Pattern.fireship, pos=Position(44,4), step=2)
            if count > 2:
                lifE.spawn(life.Pattern.fireship, pos=Position(84,4), step=4)



class Life(Mode):

    Style = Style
    DefaultStyle = Style.read


    
    def start(self,style,count,wrap=True,**params):
        self.offset = Position(0, 0)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.diff)

        if style == Style.read:
            buf = self.fluepdot.buffer.read()
            self.life = life.Life(wrap=wrap,mask=buf)
            return True

        buf = Mask(size=FRAMESIZE)
        self.life = life.Life(wrap=wrap, size=buf.size())

        style.value.fun(self.life,count)
        info("start "+str(self.life))
        return True
        
    
    def draw(self,**params):
        debug("{:s}".format(str(self.life)))
        self.life.step()
        return Mask(mask=self.life)


    
    flags = [
        Mode.FLAG("style",DefaultStyle),
        Mode.FLAG("count", 16),
#        ("w", "wrap", "wrap", True, "wrap edges", None)
    ]
