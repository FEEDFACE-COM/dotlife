
from dotlife import *
from dotlife.util import *
from dotlife.mode import Mode

from dotlife.buffer import Buffer


def Init(timer):
    return Test(timer)


class Test(Mode):
    
    def __init__(self,timer):
        super().__init__(timer)
    
    def step(self):
        pass
    
    def draw(self):
        c = int(self.timer.count)
        d = int(c/4) % 4 
        
        
        d = 3
#        c = 1
        
        col = 0x1
        ret = Buffer()
        for y in range(ret.h):
            for x in range(ret.w):
                if y == 0:
                    ret[x,y] = x+1
                if y == 1:
                    ret[x,y] = 0xA + (x+1)**2
                
        return ret
        
        mul = c % 4 + 1
        direction = {
            0: Direction.north,
            1: Direction.west,
            2: Direction.south,
            3: Direction.east
        }[c%4]
        black = c%2 * 0x80
        white = (1 - c%2) * 0x80
        
        fun = {
            0: lambda : Buffer.Ranges(mul=mul),
            1: lambda : Buffer.SixtyFourShadesOfGrey(mul=mul),
            2: lambda : Buffer.Checkers(black=black,white=white),
            3: lambda : Buffer.Gradient(direction),
        }.get(d, lambda: Buffer() )
        
        ret = fun()
        return ret
