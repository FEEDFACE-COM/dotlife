
from dotlife.util import *


from dotlife.mode import Mode as dotMode
from dotlife.font import FONT

from fliplife import DEFAULT_FONT

#
# to add a new mode 'foobar':
#   1. add 'from fliplife.mode import foobar'
#   2. add 'foobar = "foobar.Foobar"' to Enum fliplife.MODE
#   3. create class Foobar(fliplife.mode.Mode) in fliplife/mode/foobar.py
#



class Mode(dotMode):

    help = ""

    def __init__(self,fluepdot,timer,mask,**params):
        super().__init__(timer,**params)
        self.fluepdot = fluepdot
        self.mask = mask


    def start(**params):
        return super().start()
        
    def draw(**params):
        return Mask()

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

