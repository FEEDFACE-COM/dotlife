


from dotlife import *
from dotlife.math import *
from dotlife.util import *
from dotlife.clock import Timer

from dotlife.mask import Mask

DefaultSize = Size(16,16)

class Invader():

    def __init__(self,duration):
        self.timers = [
            Timer(duration,fun=self.step),
        ]
        self.species = [
            INVADER.one.Masks(),
            INVADER.two.Masks(),
        ]
        self.idx = 0
        self.size = Size(16,10)

        self.east = True
                
        debug("invader size is {}".format(self.size))
        self.start = Position(-self.size.w+2, -2*self.size.h)
        self.pos = Position(self.start.x,self.start.y)
#        self.pos = Position(-self.size.w,self.starty)
        

    def step(self):
        self.idx += 1
        self.idx %= 2
        if self.east:
            self.pos.x += 1
        else:
            self.pos.x -= 1

#        self.pos.y += 1
            
        if self.timers[0].count % self.size.w == 0:
            if self.east:
                self.pos.x -= 1
            else:
                self.pos.x += 1
            self.east ^= True
            self.pos.y += 2
            
        if self.pos.y >= self.start.y + 2*self.size.h:
            self.pos.y = self.start.y

    def mask(self,size=DefaultSize):
    
        ret = Mask(size=size)

#        import pdb; pdb.set_trace()

        cols = math.ceil(size.w / self.size.w) + 1
        rows = math.ceil(size.h / self.size.h) + 2
#        debug("{:} rows".format(rows))
        for r in range(rows):
            for c in range(cols):
                s = r % len(self.species)
                pos = self.pos + Position(c * self.size.w, r * self.size.h)
                ret.addMask(self.species[s][self.idx], pos=pos)
            
        return ret





class INVADER(Enum):

    def Masks(self,flip=Flip.noflip):
        ret = []
        for txt in self.value:
            ret += [ Mask.Load(txt).flip(flip) ]
        return ret

    def Mask(self,step=0,flip=Flip.noflip):
        if type(self.value) == type([]):
            txt = self.value[step%len(self.value)] 
        else:
            txt = self.value
        ret = Mask.Load(txt)
        ret = ret.flip()
        return ret


    one = ["""
    []          []    
      []      []      
    [][][][][][][]    
  [][]  [][][]  [][]  
[][][][][][][][][][][]
[]  [][][][][][][]  []
[]  []          []  []
      [][]  [][]      
""","""
    []          []    
[]    []      []    []
[]  [][][][][][][]  []
[][][]  [][][]  [][][]
[][][][][][][][][][][]
    [][][][][][][]    
    []          []    
  []              []  
"""]

    two = ["""
        [][]          
      [][][][]        
    [][][][][][]      
  [][]  [][]  [][]    
  [][][][][][][][]    
    []  [][]  []      
  []            []    
    []        []      
""","""
        [][]          
      [][][][]        
    [][][][][][]      
  [][]  [][]  [][]    
  [][][][][][][][]    
      []    []        
    []  [][]  []      
  []  []    []  []    
"""]

    three = ["""
        [][][][]        
  [][][][][][][][][][]  
[][][][][][][][][][][][]
[][][]    [][]    [][][]
[][][][][][][][][][][][]
    [][][]    [][][]    
  [][]    [][]    [][]  
    [][]        [][]    
""","""
        [][][][]        
  [][][][][][][][][][]  
[][][][][][][][][][][][]
[][][]    [][]    [][][]
[][][][][][][][][][][][]
      [][]    [][]      
    [][]  [][]  [][]    
[][]                [][]
"""]
    
    
