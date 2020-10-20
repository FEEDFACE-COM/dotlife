
from dotlife.util import *

import fliplife
from fliplife.mode import Mode
from fliplife import FRAMESIZE, Mask

import dotlife.invader as invader
from dotlife.invader import INVADER

class Invader(Mode):


    def start(self,species,**params):
        info("start invader {:}".format(species))
        self.invader = invader.Invader(self.timer.duration)
        return True
        
    
    def draw(self,**params):
        return self.invader.mask(size=FRAMESIZE)
        
    
    flags = [
        ("i:","invader=","species",INVADER.one,"invader species",lambda x: invader.INVADER[x]),
    ]
