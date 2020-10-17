
from dotlife.util import *

from dotlife.life import *

from oledlife import FRAMESIZE
from oledlife.mode import Mode



class Glider(Mode):
    
    
    def start(self,**params):
        self.life = Life(size=FRAMESIZE)
        self.life.addGlider(pos=Position(3,3),step=0, direction=Direction.center)
        self.life.addGlider(pos=Position(-1,-1),step=3, direction=Direction.center)
        return True

    def draw(self,**params):
        buffer = Buffer(size=FRAMESIZE)
        buffer.add (self.life.buffer(0x1,0x00) )
        return buffer


    def step(self,**params):
        self.life.step()
