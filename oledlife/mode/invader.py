from dotlife.util import *
from dotlife.mode import Mode
#from dotlife.clock import timer

from dotlife.pattern import *


from oledlife import Mask, Buffer
from oledlife.mode import Mode


class Invader(Mode):

    def start(self,step,**params):
        c = (step+self.timer.count) % len(INVADER)
        self.mask = Mask().Load( INVADER[ c ] )
        return True
        
    def draw(self,light,**params):
        ret = Buffer()
        ret.addMask( self.mask, light=light )
        return ret


    def step(self,step,**params):
        c = (step+self.timer.count) % len(INVADER)
        self.mask = self.mask.Load( INVADER[ c ] )

    flags = [
        Mode.FLAG("step"),
        ("l:","light=","light",1,"brightness",lambda x: int(x) ),
    ]    

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
