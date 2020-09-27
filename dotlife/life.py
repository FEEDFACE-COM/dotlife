
from dotlife import *
from dotlife.util import *
from dotlife.buffer import Buffer
from dotlife.mask import Mask


class Life:

    W = FRAMEWIDTH
    H = FRAMEHEIGHT
    
    ALIVE = 0x80
    DEAD = 0x00


    GLIDER = [ 
    
    
"""
  []  
    []
[][][]
""",

"""
[]  []
  [][]
  []  
""",

"""
    []
[]  []
  [][]
""",

"""
[]    
  [][]
[][]  
"""
    
    ]



    def __str__(self):
        return "gen#{}\n".format(self.gen) + str(self.board)


    def buffer(self,alive=ALIVE,dead=DEAD):
        ret = Buffer()
        ret.mask( self.board, light=alive )
        return ret
    
    def __init__(self,gen=0):
        self.gen = gen
        self.board = Mask( size=(Life.W,Life.H) )
        
    def step(self):
        tmp = Mask(size=(Life.W,Life.H) )
        for x in range(Life.W):
            for y in range(Life.H):
                if self.alive(x,y):
                    tmp[x,y] = True
                

        self.gen = self.gen+1
        self.board = tmp
        info(str(self))



    def alive(self,x,y):
        neighbours = 0
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if r == 0 == c:
                    continue
                if self.board[x+c,y+r]:
                    neighbours += 1
        if self.board[x,y] and neighbours in [2,3]:
            return True
        if not self.board[x,y] and neighbours == 3:
            return True
        return False




    def addGlider(self,pos=(2,2),step=0,direction=Direction.SouthEast):
        glider = Mask.Load( Life.GLIDER[step%4] )
        self.board.mask( glider, pos=pos, wrap=True )
        
