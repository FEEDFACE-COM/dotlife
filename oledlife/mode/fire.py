
from dotlife import *
from dotlife.util import *
from dotlife.mode import Mode

from dotlife.buffer import Buffer
import dotlife.fire as fire

def Init(timer):
    return Fire(timer)


class Fire(Mode):
    
    def __init__(self,timer):
        super().__init__(timer)
#        self.fire
        self.fire = fire.Fire()
    
    def step(self):
        self.fire.step()
    
    def draw(self):
        ret = self.fire.buffer()
        return ret
