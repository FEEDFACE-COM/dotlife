from dotlife.util import *
from dotlife.mode import Mode
#from dotlife.clock import timer

from dotlife.pattern import *
from dotlife.buffer import Buffer
from dotlife.mask import Mask


def Init(timer):
    return Invader(timer)



class Invader(Mode):

    def __init__(self,timer):
        super().__init__(timer)
        self.mask = Mask.Load( INVADER[ self.timer.count % len(INVADER)] )
        
        
    def draw(self):
        ret = Buffer()
        ret.mask( self.mask )
        return ret


    def step(self):
        super().step()
        self.mask = Mask.Load( INVADER[ self.timer.count % len(INVADER) ] )



INVADER= ["""
  []        []  
    []    []    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
[]  [][][][]  []
    []    []    
  []        []  
""","""
  []    []      
    []    []    
  [][][][][][]  
[][][]  []  [][]
[][][][][][][][]
[]  [][][][]  []
    []    []    
  []    []      
""","""
  []        []  
    []    []    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
[]  [][][][]  []
    []    []    
  []        []  
""","""
      []    []  
    []    []    
  [][][][][][]  
[][]  []  [][][]
[][][][][][][][]
[]  [][][][]  []
    []    []    
      []    []  
"""]
