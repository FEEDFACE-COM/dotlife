
from dotlife import *
from dotlife.util import *
from dotlife.buffer import Buffer
from dotlife.mask import Mask


from enum import Enum,auto

class Pattern(Enum):
    Glider = \
"""
  []  
    []
[][][]
"""

    Gun = \
"""
                                                []                      
                                            []  []                      
                        [][]            [][]                        [][]
                      []      []        [][]                        [][]
[][]                []          []      [][]                            
[][]                []      []  [][]        []  []                      
                    []          []              []                      
                      []      []                                        
                        [][]                                            
""" 

    Eater = \
"""
[][]    
[]      
  [][][]
      []
"""

    Copperhead = \
"""
      [][]  [][][]      
[]  []        [][][]    
[]    []        []  [][]
[]    []        []  [][]
[]  []        [][][]    
      [][]  [][][]      
"""

    Rpentomino = \
"""
  [][]
[][]  
  []  
"""

    Herschel = \
"""
[]    
[]  []
[][][]
    []
"""

    def __init__(self,name):
        super().__init__()
        return self


    def Mask(self,step=0,flip=Flip.NoFlip):
        log("spawn " + str(self.name))
        ret = Mask.Load(self.value)
        ret.flip(flip)
        return ret



class Life:


    
    ALIVE = 0x80
    DEAD = 0x00

    def __str__(self):
        return "gen#{}\n".format(self.gen) + str(self.board)


    def buffer(self,alive=ALIVE,dead=DEAD):
        ret = Buffer()
        ret.mask( self.board, light=alive )
        return ret
    
    def __init__(self,size=Size(8,8),gen=0,mask=None):
        self.gen = gen
        if mask == None:
            self.board = Mask(size=size)
        else:
            self.board = Mask(mask=mask)
        

    def step(self):
        tmp = Mask(size=(self.board.w,self.board.h) )
        for x in range(self.board.w):
            for y in range(self.board.h):
                if self.alive(x,y):
                    tmp[x,y] = True
                

        self.gen = self.gen+1
        self.board = tmp
#        info(str(self))


    def spawn(self,pattern,pos=Position(0,0),step=0,flip=Flip.NoFlip):
        pat = pattern.Mask(step,flip)
        self.board.mask( pat, pos=pos, wrap=True )
        return

    def minimal(self):
        p0,p1 = Position(self.board.w,self.board.h),Position(0,0)
        for y in range(self.board.h):
            for x in range(self.board.w):
                if self.board[x,y]:
                    if x < p0.x:
                        p0.x = x
                    if x > p1.x:
                        p1.x = x
                    if y < p0.y:
                        p0.y = y
                    if y > p1.y:
                        p1.y = y
        
        size = Size( p1.x - p0.x, p1.y - p0.y )
        ret = Mask(size=(size.x,size.y))
        for y in range(p0.y,p1.y):
            for x in range(p0.x,p1.x):
                ret[x-p0.x,y-p0.y] = self.board[x,y]
        
        log("minimal board {:s}:\n{:s}".format(str(size),str(ret)))
        return ret


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
        x,y = pos
        return self.add(Pattern.Glider,pos=Position(x,y),step=step)


#    def addEater(self,pos=Position(0,0)):
#        eater = Mask.Load( Life.EATER[0] )
#        self.board.mask(eater,pos=pos,wrap=True )
#
#    def addGun(self,pos=Position(10,0)):
#        gun = Mask.Load( Life.GUN[1] )
#        self.board.mask( gun, pos=pos, wrap=True )
#
#    def addGlider(self,pos=Position(2,2),step=0,direction=Direction.SouthEast):
#        glider = Mask.Load( Life.GLIDER[step%4] )
#        self.board.mask( glider, pos=pos, wrap=True )
        
