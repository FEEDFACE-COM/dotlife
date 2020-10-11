
from dotlife.util import *


from dotlife.mode import Mode as dotMode
#
# to add a new mode 'foobar':
#   1. add 'foobar = "foobar"' to MODE Enum
#   2. create dotlife/mode/foobar.py
#


from enum import Enum, auto

class MODE(Enum):
    test      = auto()
    read      = auto()
    clear     = auto()
    fill      = auto()
    gauss     = auto()
    echo      = auto()
    exec      = auto()
    grow      = auto()
    pixel     = auto()
    dots      = auto()
    life      = auto()
    glider    = auto()
    guns      = auto()
    spawn     = auto()
    fluep     = auto()
    pipe      = auto()

import dotlife.clock as clock


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

    def __init__(self,fluepdot,timer):
        super().__init__(timer)
        self.fluepdot = fluepdot

