
from dotlife.util import *



from dotlife.mode import Mode as dlMode
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

class Mode(dlMode):

    def Init(mode,step):
    
        # static import for run time checking
        from oledlife.mode import fyi
        from oledlife.mode import glider
        from oledlife.mode import pulser
        from oledlife.mode import tetris
        from oledlife.mode import scroller
        from oledlife.mode import plasma
        from oledlife.mode import invader
        from oledlife.mode import life
        from oledlife.mode import draft
        from oledlife.mode import palette
        from oledlife.mode import test
        from oledlife.mode import tunnel
        from oledlife.mode import fire
        
        try:
            cls = __import__("oledlife.mode."+str(mode), fromlist=[''])
        except ModuleNotFoundError as x:   # ??
#            error("module {} not found: {}".format(mode,str(x)))
            raise Error("module {} not found".format(mode))
        except Exception as x:
            raise Error("mode {} imported exception: {}".format(mode,str(x)))
        
        timer = clock.Clock.Timer(step,repeat=True)
        ret = cls.Init(timer)
        ret.last = ret.draw()
        return ret
    


