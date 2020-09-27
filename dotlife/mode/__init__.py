
from dotlife.util import *

from dotlife.buffer import Buffer

#
# to add a new mode 'foobar':
#   1. add 'foobar = "foobar"' to MODE Enum
#   2. create dotlife/mode/foobar.py
#



class MODE(Enum):
    fyi       = "fyi"     #auto()
    glider    = "glider"  #auto()
    pulser    = "pulser"  #auto()
    tetris    = "tetris"  #auto()
    plasma    = "plasma"  #auto()
    invader   = "invader" #auto()
    scroller  = "scroller"#auto()
    life      = "life"    #auto()
    tunnel    = "tunnel"  #auto()
    fire      = "fire"    #auto()
    draft     = "draft"   #auto()
    palette   = "palette" #auto()
    test      = "test"    #auto()
#    random    = "random"  #auto()



import dotlife.clock as clock

class Mode():

    def __init__(self,timer):
        self.timer = timer
        self.timer.fun = lambda : self.step()
        self.last = Buffer()
        self.debug = False


    def draw(self):
        return Buffer()

    def step(self):
        self.last = self.draw()

    def __str__(self):
        return "mode " + type(self).__name__.lower()
    

    def signal(self):
        self.debug ^= True
        debug("debug {}".format("on" if self.debug else "off") )

    def Init(mode,step):
    
        # static import for exec time checking
        from dotlife.mode import fyi
        from dotlife.mode import glider
        from dotlife.mode import pulser
        from dotlife.mode import tetris
        from dotlife.mode import scroller
        from dotlife.mode import plasma
        from dotlife.mode import invader
        from dotlife.mode import life
        from dotlife.mode import draft
        from dotlife.mode import palette
        from dotlife.mode import test
        from dotlife.mode import tunnel
        from dotlife.mode import fire
        
        try:
            cls = __import__("dotlife.mode."+str(mode), fromlist=[''])
        except ModuleNotFoundError as x:   # ??
#            error("module {} not found: {}".format(mode,str(x)))
            raise Error("module {} not found".format(mode))
        except Exception as x:
            raise Error("mode {} imported exception: {}".format(mode,str(x)))
        
        timer = clock.Clock.Timer(step,repeat=True)
        ret = cls.Init(timer)
        ret.last = ret.draw()
        return ret
    


