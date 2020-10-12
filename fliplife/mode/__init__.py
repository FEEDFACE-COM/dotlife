
from dotlife.util import *


from dotlife.mode import Mode as dotMode
from dotlife.font import FONT

from fliplife import DEFAULT_FONT

#
# to add a new mode 'foobar':
#   1. add 'from fliplife.mode import foobar'
#   2. add 'foobar = "foobar.Foobar"' to Enum fliplife.MODE
#   3. create class Foobar(fliplife.mode.Mode) in dotlife/mode/foobar.py
#



def Class(mode):

    # static import for run time checking
    from fliplife.mode import test,read,clear,fill,gauss,echo,exec
    from fliplife.mode import grow,pixel,dots,life,glider,guns,spawn
    
    try:
        mod = __import__("fliplife.mode."+str(mode.name), fromlist=[''])
        ret = getattr(mod,mode.name.capitalize())
    except AttributeError as x:
        raise Error("class {} not found".format(mode.capitalize()))
    except ModuleNotFoundError as x:   # ??
        raise Error("module {} not found".format(mode.name))
    except Exception as x:
        raise Error("mode {} imported exception: {}".format(mode.name,str(x)))
    
    return ret


class Mode(dotMode):

    help = ""

    def __init__(self,fluepdot,timer,mask):
        super().__init__(timer)
        self.fluepdot = fluepdot
        self.mask = mask



    FLAG = {
        # param: short long default help func #             
        "speed":     ("s:", "speed=",       "speed",      1.0,             "step speed [s]",       lambda x : float(x) ),
        "invert":    ("i",  "invert",       "invert",     False,           "invert pattern?",                     None ),
        "count":     ("c:", "count=",       "count",      1,               "count",                  lambda x : int(x) ),
        "font":      ("f:", "font=",        "font",       DEFAULT_FONT,    "font",                   lambda x: FONT[x] ),
        "pattern":   ("p:", "pattern=",     "pattern",    None,            "pattern",                             None ),
        "step":      ("q:", "step=",        "step",       0,               "pattern step",           lambda x : int(x) ),
        "x":         ("x:", "",             "x",          0,               "x offset",               lambda x : int(x) ),
        "y":         ("y:", "",             "y",          0,               "y offset",               lambda x : int(x) ),
        "randomize": ("r", "random",        "randomize",  False,           "randomize?",                          None ),
    }
    
    FLAGS = [
        FLAG["speed"],
    ]
    
    flags = []

