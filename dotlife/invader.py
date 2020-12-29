


from dotlife import *
from dotlife.math import *
from dotlife.util import *
from dotlife.time import Timer

from dotlife.mask import Mask

DefaultSize = Size(16,16)

class Invader():

    def __init__(self,duration,count=None,alt=False,large=False):
        self.timers = [
            Timer(duration,fun=self.step),
        ]
        self.species = [
            [ ( m.double() if large else m ) for m in INVADER.one.Masks() ],
            [ ( m.double() if large else m ) for m in INVADER.two.Masks() ],
        ]
#        for m in self.species[0] + self.species[1]:
#            debug("{}".format(str(m)))

        self.count = count
        self.idx = 0
        self.size = Size(16,10)
        if large:
            self.size = self.size * 2
        self.alternate = alt

#        debug("invader size is {}".format(self.size))

        self.east = True
        self.start = Position(0,0)
        self.pos = self.start.copy()



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
            self.pos.y -= 2*self.size.h
            
        

    def mask(self,size=DefaultSize):
        margin = 0
        ret = Mask(size=size)
        
        
        cols = math.ceil(size.w / self.size.w) + 1
        rows = 1
        
        
        if self.count > (size.w / self.size.w):
            self.count = ceil(size.w / self.size.w)
        
        if self.count:
            cols = self.count
        
        
        bounds = Size(cols * self.size.w,  rows * self.size.h)
        center = Position( int(size.w/2), int(size.h/2) )
        
        
        pos = self.pos.copy()
        off = Position()
        pos.x += size.center().x - bounds.center().x 
        pos.y += size.center().y - bounds.center().y
        
        
        
        for c in range(cols):
            off.x = c * self.size.w
            ret.addMask( self.species[0][self.idx], pos=pos+off )
            ret.addMask( self.species[0][self.idx], pos=pos+off+Position(0,-2*self.size.h))
            if self.alternate:
                ret.addMask( self.species[1][self.idx], pos=pos+off+Position(0,-1*self.size.h))#            if self.alternate:
                ret.addMask( self.species[1][self.idx], pos=pos+off+Position(0,+1*self.size.h))#            if self.alternate:
              
        
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
        ret = ret.flip(flip)
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
    
    
