
from dotlife.util import *
from dotlife.mode import Mode

from dotlife.life import *


def Init(timer):
    return Glider(timer)



class Glider(Mode):
    
    def __init__(self,timer):
        super().__init__(timer)
        self.life = Life()
        self.life.addGlider(pos=(3,3),step=0, direction=Direction.Center)
        self.life.addGlider(pos=(-1,-1),step=3, direction=Direction.Center)

    def draw(self):
        buffer = Buffer()
        buffer.add (self.life.buffer(0x1,0x00) )
        return buffer


    def step(self):
        super().step()
        self.life.step()
