
from dotlife import *
from dotlife.util import *
from dotlife.buffer import Buffer
from dotlife.mask import Mask

import random, copy

class Tetris:

    def __str__(self):
        return "tetris"
        
    def buffer(self,light=LIGHT,dark=DARK):
        ret = Buffer(size=Size(self.w,self.h))
        ret.addMask( self.tile.mask,light=light, pos=Position(self.tile.x,self.tile.y) )
        return ret
        
        
    def __init__(self,size=DefaultSize):
        random.seed()
        self.w,self.h = size.w,size.h
        tetros = []
        for t in Tetris.Tetronimo:
            tetros.append( t )
        r = random.randrange(0,len(tetros))
        self.tile = Tetris.Tile(tetros[r])
        debug("new "+str(self.tile))
            

    def step(self):
        x,y = self.tile.x, self.tile.y
        if y >= self.h: # new tile
            tetros = []
            for t in Tetris.Tetronimo:
                tetros.append( t )
            r = random.randrange(0,len(tetros))
            self.tile = Tetris.Tile( tetros[r] )
            debug("new "+str(self.tile))
            return 


        r = random.randrange(0,4)
        if r == 0:
            x += 1
        elif r == 1:
            x -= 1
        else:
#            breakpoint()
            r = random.randrange(0,4)
            if r == 0:
                self.tile.rotate(Rotation.clockwise)
            elif r == 1:
                self.tile.rotate(Rotation.counterclockwise)


        if x < 0:
            x = 0
        if x > self.w - self.tile.mask.w:
            x = self.w - self.tile.mask.w


        self.tile.x = x
        self.tile.y = y+1
        debug("step "+str(self.tile))



    class Tile():

        def __str__(self):
            return "{} {}x{} {},{}\n".format(self.tetronimo.name,self.mask.w,self.mask.h,self.x,self.y) + str(self.mask)
        
        
        def rotate(self,direction=None):
            msk = Mask( val=False, size=Size(self.mask.h,self.mask.w) )
            for y in range(msk.h):
                for x in range(msk.w):
                    if direction == Rotation.clockwise:
                        msk[x,y] = self.mask[self.mask.h-y-1,x]
                    elif direction == Rotation.counterclockwise:
                        msk[x,y] = self.mask[y,self.mask.w-x-1]
                    else:
                        msk[x,y] = self.mask[y,x]
            self.mask = msk
            return
            
                        
        
        def __init__(self,tetronimo):
            self.tetronimo = tetronimo
            self.x, self.y = 3, -3
            self.mask = Mask.Load( self.tetronimo.value )

    class Tetronimo(Enum):
    
            I = """
[]
[]
[]
[]
"""

            J = """
[][]
[]  
[]  
"""
            L = """
[][]
  []
  []
"""
            T = """
[][][]
  []  
"""
            S = """
[]  
[][]
  []
"""
            Z = """
  []
[][]
[]  
"""
            O = """
[][]
[][]
"""

        
