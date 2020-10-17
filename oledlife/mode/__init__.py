

from dotlife.util import *
import dotlife.mode

from oledlife import DEFAULT_FONT


#
# to add a new mode 'foobar':
#   1. add 'from oledlife.mode import foobar'
#   2. add 'foobar = "foobar.Foobar"' to Enum oledlife.MODE
#   3. create class Foobar(oledlife.mode.Mode) in oledlife/mode/foobar.py
#



class Mode(dotlife.mode.Mode):

    help = ""

    def __init__(self,timer,mask,**params):
        super().__init__(timer,**params)
        self.mask = mask


    def start(**params):
        return super().start()
        
    def draw(**params):
        return Mask()

#    FLAG = {
#        # param: short long default help func #             
#        "speed":     ("s:", "speed=",       "speed",      1.0,             "step speed [s]",       lambda x : float(x) ),
#        "invert":    ("i",  "invert",       "invert",     False,           "invert pattern?",                     None ),
#        "count":     ("c:", "count=",       "count",      1,               "count",                  lambda x : int(x) ),
#        "font":      ("f:", "font=",        "font",       DEFAULT_FONT,    "font",                   lambda x: FONT[x] ),
#        "pattern":   ("p:", "pattern=",     "pattern",    None,            "pattern",                             None ),
#        "step":      ("q:", "step=",        "step",       0,               "pattern step",           lambda x : int(x) ),
#        "x":         ("x:", "",             "x",          0,               "x offset",               lambda x : int(x) ),
#        "y":         ("y:", "",             "y",          0,               "y offset",               lambda x : int(x) ),
#        "randomize": ("r", "random",        "randomize",  False,           "randomize?",                          None ),
#    }
    
    
    FLAGS = [
        dotlife.mode.Mode.FLAG("speed"),
    ]
    
    flags = []




#class MODE(Enum):
#    fyi       = "fyi"     #auto()
#    glider    = "glider"  #auto()
#    pulser    = "pulser"  #auto()
#    tetris    = "tetris"  #auto()
#    plasma    = "plasma"  #auto()
#    invader   = "invader" #auto()
#    scroller  = "scroller"#auto()
#    life      = "life"    #auto()
#    tunnel    = "tunnel"  #auto()
#    fire      = "fire"    #auto()
#    draft     = "draft"   #auto()
#    palette   = "palette" #auto()
#    test      = "test"    #auto()
##    random    = "random"  #auto()
#





#
#class Mode(dlMode):
#
#    def Init(mode,step):
#    
#        # static import for run time checking
#        from oledlife.mode import fyi
#        from oledlife.mode import glider
#        from oledlife.mode import pulser
#        from oledlife.mode import tetris
#        from oledlife.mode import scroller
#        from oledlife.mode import plasma
#        from oledlife.mode import invader
#        from oledlife.mode import life
#        from oledlife.mode import draft
#        from oledlife.mode import palette
#        from oledlife.mode import test
#        from oledlife.mode import tunnel
#        from oledlife.mode import fire
#        
#        try:
#            cls = __import__("oledlife.mode."+str(mode), fromlist=[''])
#        except ModuleNotFoundError as x:   # ??
##            error("module {} not found: {}".format(mode,str(x)))
#            raise Error("module {} not found".format(mode))
#        except Exception as x:
#            raise Error("mode {} imported exception: {}".format(mode,str(x)))
#        
#        timer = clock.Clock.Timer(step,repeat=True)
#        ret = cls.Init(timer)
#        return ret
#    


