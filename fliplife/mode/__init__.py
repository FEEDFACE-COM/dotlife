
from dotlife.util import *


import dotlife.mode
from dotlife.font import FONT

from fliplife import DEFAULT_FONT

#
# to add a new mode 'foobar':
#   1. add 'from fliplife.mode import foobar'
#   2. add 'foobar = "foobar.Foobar"' to Enum fliplife.MODE
#   3. create class Foobar(fliplife.mode.Mode) in fliplife/mode/foobar.py
#



class Mode(dotlife.mode.Mode):

    help = ""

    def __init__(self,fluepdot,timer,mask,**params):
        super().__init__(timer,**params)
        self.fluepdot = fluepdot
        self.mask = mask


    def start(self,**params):
        return super().start()
        
    def draw(self,**params):
        return Mask()    
    
    FLAGS = [
        dotlife.mode.Mode.FLAG("speed"),
    ]
    
    flags = []

