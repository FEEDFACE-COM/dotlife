
from dotlife.util import *
from dotlife.mode import Mode
from dotlife.buffer import Buffer

import dotlife.tetris

from oledlife import Buffer, FRAMESIZE
from oledlife.mode import Mode



class Tetris(Mode):
    
    def start(self,**params):
        self.tetris = dotlife.tetris.Tetris(size=FRAMESIZE)
        return True
    
    def draw(self,light,**params):
        buffer = self.tetris.buffer(light=light)
        return buffer


    def step(self,**params):
        self.tetris.step()

    flags = [
        ("l:","light=","light",1,"brightness",lambda x: int(x) ),
    ]
