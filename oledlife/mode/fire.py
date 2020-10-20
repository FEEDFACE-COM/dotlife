
from dotlife import *
from dotlife.util import *
from oledlife.mode import Mode

from dotlife.buffer import Buffer
import dotlife.fire as fire



class Fire(Mode):
    
    def start(self,**params):
        self.fire = fire.Fire()
        return True
    
    def step(self,**params):
        self.fire.step()
    
    def draw(self,**params):
        ret = self.fire.buffer()
        return ret


    flags = [
    ]
