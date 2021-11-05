
from enum import auto
from dotlife.util import Enum

from dotlife.font import FONT
from dotlife import *


class Mode():


    Pattern = ()


    def __init__(self,timer,**params):
        self.timer = timer
        self.timer.fun = lambda: self.step(**params)
        self.debug = False


    def start(self):
        return False

    def draw(self):
        return Mask()

    def step(self,**params):
        pass

    def __str__(self):
        return "mode " + type(self).__name__.lower()
    

    def signal(self):
        self.debug ^= True
        debug("debug {}".format("on" if self.debug else "off") )


    def FLAG(name,default=None):
        (s,l,n,d,h,f) = {
            # param: short long name default help func #
            "seed":      ("S:", "seed=",        "seed",       None,                    "random seed",                                         lambda x: int(x,16) ),
            "speed":     ("s:", "speed=",       "speed",      1.0,                     "step speed [s]",                                      lambda x : float(x) ),
            "invert":    ("i",  "invert",       "invert",     False,                   "invert pattern?",                                                    None ),
            "count":     ("c:", "count=",       "count",      1,                       "count",                                                 lambda x : int(x) ),
            "font":      ("F:", "font=",        "font",       default,                 "font",                                                  lambda x: FONT[x] ),
            "pattern":   ("p:", "pattern=",     "pattern",    default,                 "pattern",                                     lambda x:  type(default)[x] ), # get type of default, then lookup x in type
            "step":      ("q:", "step=",        "step",       0,                       "step",                                                  lambda x : int(x) ),
            "flip":      ("f:", "flip=",        "flip",       Flip.noflip,             ",".join([str(f) for f in Flip]),                       lambda x : Flip[x] ),
            "x":         ("x:", "",             "x",          0,                       "x offset",                                              lambda x : int(x) ),
            "y":         ("y:", "",             "y",          0,                       "y offset",                                              lambda x : int(x) ),
            "randomize": ("R", "random",        "randomize",  False,                   "randomize?",                                                         None ),
            "style":     ("Y:", "style=",       "style",      default,                 "style",                                       lambda x:  type(default)[x] ), # get type of default, then lookup x in type
            "msg":       (None, None,           "msg",        "hello, world.",         "message",                                                            None ),
            "alignv":    ("V:", "vertical=",    "alignv",     AlignVertical.top,       ",".join([str(j) for j in AlignVertical]),      lambda x: AlignVertical[x] ),
            "alignh":    ("H:", "horizontal=",  "alignh",     AlignHorizontal.left,    ",".join([str(j) for j in AlignHorizontal]),  lambda x: AlignHorizontal[x] ),
        }.get(name,("","","",None,"",None))

        if default != None:
            d = default
            
        return (s,l,n,d,h,f)

    
