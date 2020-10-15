
from dotlife.util import *
from dotlife.mode import Mode

from dotlife.life import *

from oledlife import FRAMESIZE

def Init(timer):
    return Glider(timer)



class Glider(Mode):
    
    
    def __init__(self,timer):
        super().__init__(timer)
        self.life = Life(size=FRAMESIZE)
        self.life.addGlider(pos=Position(3,3),step=0, direction=Direction.center)
        self.life.addGlider(pos=Position(-1,-1),step=3, direction=Direction.center)

    def draw(self):
        buffer = Buffer(size=FRAMESIZE)
        buffer.add (self.life.buffer(0x1,0x00) )
        return buffer


    def step(self):
        super().step()
        self.life.step()
