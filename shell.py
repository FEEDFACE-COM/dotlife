from importlib import reload
from bdb import BdbQuit

import sys, os, re, pprint, datetime, time

import dotlife
from dotlife.clock import *
from dotlife.buffer import *
from dotlife.mask import *
from dotlife.framebuffer import *
from dotlife.mode import *
from dotlife.pattern import *
from dotlife.plasma import *

for m in MODE:
    try:
        cls = __import__("dotlife.mode."+str(m.name), fromlist=[''])
#    except ModuleNotFoundError as x:   # ??
    except Exception as x:
        fatal("mode {} not imported: {}".format(m.name,str(x)))

def p(x): 
    print(x)

