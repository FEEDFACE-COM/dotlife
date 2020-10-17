from importlib import reload
from bdb import BdbQuit

import sys, os, re, pprint, datetime, time
import random

import dotlife
import oledlife, fliplife

import dotlife.life

from dotlife.clock import *
from dotlife.buffer import *
from dotlife.mask import *
from dotlife.mode import *
from dotlife.pattern import *
from dotlife.plasma import *
from dotlife.font import *

from fliplife import *
from fliplife.pixel import *
from fliplife.framebuffer import *

from oledlife.paneloled import *
from fliplife.fluepdot import *



for m in fliplife.MODE:
    try:
        cls = __import__("fliplife.mode."+str(m.name), fromlist=[''])
#    except ModuleNotFoundError as x:   # ??
    except Exception as x:
        FATAL("mode {} not imported: {}".format(m.name,str(x)))


for m in oledlife.MODE:
    try:
        cls = __import__("oledlife.mode."+str(m.name), fromlist=[''])
#    except ModuleNotFoundError as x:   # ??
    except Exception as x:
        FATAL("mode {} not imported: {}".format(m.name,str(x)))


def p(x): 
    print(x)

