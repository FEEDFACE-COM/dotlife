
from dotlife.util import *
from dotlife.mode import Mode
from dotlife.buffer import Buffer

import dotlife.tetris


def Init(timer):
    return Tetris(timer)


class Tetris(Mode):
    
    def __init__(self,timer):
        super().__init__(timer)
        self.tetris = dotlife.tetris.Tetris()
    
    def draw(self):
        buffer = self.tetris.buffer(0x1,0x00)
        return buffer


    def step(self):
        super().step()
        self.tetris.step()


