
from dotlife import *
from dotlife.util import *
from dotlife.buffer import Buffer
from dotlife.mask import Mask





class Life(Mask):


    
    ALIVE = 0x80
    DEAD = 0x00

    def __str__(self):
        return "gen#{}\n".format(self.gen) + super().__str__()


    def buffer(self,alive=ALIVE,dead=DEAD):
        ret = Buffer()
        ret.addMask( self, light=alive )
        return ret
    
    def __init__(self,size=Size(8,8),gen=0,mask=None):
        if mask == None:
            super().__init__(size=size)
        else:
            super().__init__(mask=mask)
        self.gen = gen
        

    def step(self):
        prev = Life(mask=self)
        for x in range(self.w):
            for y in range(self.h):
                if prev.alive(x,y):
                    self[x,y] = True
                else:
                    self[x,y] = False
                
                

        self.gen = self.gen+1
#        info(str(self))


    def spawn(self,pattern,pos=None,step=0,flip=Flip.noflip):
        pat = pattern.Mask(step,flip)
        if pos == None:
            pos = Position( int(abs(self.w-pat.w)/2), int(abs(self.h-pat.h)/2) )
        log("spawn " + str(self.name) + "step "+step + ("flip "+str(flip)) if flip!=Flip.noflip else '' )
        self.addMask( pat, pos=pos, wrap=True )
        return

    def minimal(self):
        p0,p1 = Position(self.w,self.h),Position(0,0)
        for y in range(self.h):
            for x in range(self.w):
                if self[x,y]:
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
                ret[x-p0.x,y-p0.y] = self[x,y]
        
        log("minimal board {:s}:\n{:s}".format(str(size),str(ret)))
        return ret


    def alive(self,x,y):
        neighbours = 0
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if r == 0 == c:
                    continue
                if self[x+c,y+r]:
                    neighbours += 1
        if self[x,y] and neighbours in [2,3]:
            return True
        if not self[x,y] and neighbours == 3:
            return True
        return False


    def addGlider(self,pos=Position(2,2),step=0,direction=Direction.southeast):
        return self.spawn(Pattern.glider,pos=pos,step=step)


        
class Pattern(Enum):


    def Mask(self,step=0,flip=Flip.noflip):
        msk = Mask.Load(self.value)
        if step > 0:
            tmp = Life(size=Size(msk.w*2,msk.h*2))
            tmp.addMask(msk)
            for s in range(step):
                tmp.step()
            ret = tmp.trimMask()
        else:                
            ret = Mask.Load(self.value)
    
        ret.flip(flip)
        return ret




    glider = \
"""
  []  
    []
[][][]
"""

    gun = \
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

    eater = \
"""
[][]    
[]      
  [][][]
      []
"""

    copperhead = \
"""
      [][]  [][][]      
[]  []        [][][]    
[]    []        []  [][]
[]    []        []  [][]
[]  []        [][][]    
      [][]  [][][]      
"""

    rpentomino = \
"""
  [][]
[][]  
  []  
"""

    herschel = \
"""
[]    
[]  []
[][][]
    []
"""

    block = \
"""
[][]
[][]
"""

    shuttle = \
"""
                  []                        
              []  []                        
            []  []                          
[][]      []    []                          
[][]        []  []                          
              []  []                [][]    
                  []                []  []  
                                        []  
                                        [][]
"""


    fourteener = \
"""
        [][]  
[][]    []  []
[]          []
  [][][][][]  
      []      
"""

    turtle = \
"""
  [][][]              []
  [][]    []  [][]  [][]
      [][][]        []  
  []    []  []      []  
[]        []        []  
[]        []        []  
  []    []  []      []  
      [][][]        []  
  [][]    []  [][]  [][]
  [][][]              []
"""

    toad = \
"""
  [][][]
[][][]  
"""

    octagon = \
"""
      [][]      
    []    []    
  []        []  
[]            []
[]            []
  []        []  
    []    []    
      [][]      
"""

    opentomino = \
"""
[][][][][]
"""

    paperclip = \
"""
    [][]  
  []    []
  []  [][]
[][]  []  
[]    []  
  [][]    
"""

    pentadecathlon = \
"""
    []        []    
[][]  [][][][]  [][]
    []        []    
"""
