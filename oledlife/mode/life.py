
from dotlife import *
from dotlife.util import *
from dotlife.mode import Mode
from dotlife.buffer import Buffer
from dotlife.plasma import Plasma, Fun
from dotlife.time import Timer

import dotlife.life as life

def Init(timer):
    return Life(timer)



class Life(Mode):
    
    def __init__(self,timer):
        super().__init__(timer)
        self.timerX = Timer(timer.duration * 1.1, repeat=timer.repeat)
        self.plasma = plasma.Plasma()
        self.life = life.Life()
        self.life.addGlider((4,4),0, Direction.northeast)
        self.timer.fun = lambda : self.life.step()

    def draw(self):
        buffer = Buffer()
        ret = self.plasma.buffer(Fun(),Fun())
        ret.mask( self.life.board, light=0x0 )
#        ret.add (self.life.buffer(0x10,0x00) )
#        ret.mul( 4.*self.timer.sin0(1.) )
        return ret
