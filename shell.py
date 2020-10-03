from importlib import reload
from bdb import BdbQuit

import sys, os, re, pprint, datetime, time
import random

import dotlife
import oledlife, fliplife


from dotlife.clock import *
from dotlife.buffer import *
from dotlife.mask import *
from dotlife.mode import *
from dotlife.pattern import *
from dotlife.plasma import *

from fliplife.mask import *
from oledlife.framebuffer import *

from fliplife import mode as flipmode
from oledlife import mode as oledmode

for m in flipmode.MODE:
    try:
        cls = __import__("fliplife.mode."+str(m.name), fromlist=[''])
#    except ModuleNotFoundError as x:   # ??
    except Exception as x:
        FATAL("mode {} not imported: {}".format(m.name,str(x)))


for m in oledmode.MODE:
    try:
        cls = __import__("oledlife.mode."+str(m.name), fromlist=[''])
#    except ModuleNotFoundError as x:   # ??
    except Exception as x:
        FATAL("mode {} not imported: {}".format(m.name,str(x)))


def p(x): 
    print(x)

