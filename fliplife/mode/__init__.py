
from dotlife.util import *


from fliplife.mask import Mask
from dotlife.mode import Mode as dotMode
#
# to add a new mode 'foobar':
#   1. add 'foobar = "foobar"' to MODE Enum
#   2. create dotlife/mode/foobar.py
#



class MODE(Enum):
    test      = "test"
    ping      = "read"
    clear     = "clear"
    fill      = "fill"
    gauss     = "gauss"
    echo      = "echo"
    exec      = "exec"
    grow      = "grow"
    pixel     = "pixel"
    dots      = "dots"
    life      = "life"


import dotlife.clock as clock

class Mode(dotMode):

    def Init(mode,address,printFun,step):
    
        # static import for run time checking
        from fliplife.mode import test
        from fliplife.mode import read
        from fliplife.mode import clear
        from fliplife.mode import fill
        from fliplife.mode import gauss
        from fliplife.mode import echo
        from fliplife.mode import exec
        from fliplife.mode import grow
        from fliplife.mode import pixel
        from fliplife.mode import dots
        from fliplife.mode import life
        
        try:
            mod = __import__("fliplife.mode."+str(mode), fromlist=[''])
            cls = getattr(mod,mode.capitalize())
        except AttributeError as x:
            raise Error("class {} not found".format(mode.capitalize()))
        except ModuleNotFoundError as x:   # ??
#            error("module {} not found: {}".format(mode,str(x)))
            raise Error("module {} not found".format(mode))
        except Exception as x:
            raise Error("mode {} imported exception: {}".format(mode,str(x)))
        
        timer = clock.Clock.Timer(step,repeat=True)
        ret = cls(address,printFun,timer)
        return ret
    

    def __init__(self,address,printFun,timer):
        super().__init__(timer)
        self.address = address
        self.printFun = printFun

        
    
    
