

from dotlife.util import *

from dotlife import *
from dotlife.mask import Mask

class Symbol(Enum):

    def Mask(self,step=0,flip=Flip.noflip):
        if self.name == "none":
            return Mask()
        if type(self.value) == type([]):
            txt = self.value[step%len(self.value)] 
        else:
            txt = self.value    
        ret = Mask.Load(txt)
        ret = ret.flip(flip)
        return ret

    none = ""

    question = """
[][][]  
      []
    []  
  []    
        
  []    
"""


    checkers = """
[]  []  []  []  
  []  []  []  []
[]  []  []  []  
  []  []  []  []
[]  []  []  []  
  []  []  []  []
[]  []  []  []  
  []  []  []  []
"""

    skull = """
  [][][][][]  
[][][][][][][]
[]    []    []
[][][][][][][]
[][][]  [][][]
[][][]  [][][]
  [][][][][]  
  []  []  []  
"""

    skull1 = """
  [][][][]  
[][][][][][]
[]  [][]  []
[][][][][][]
  [][][][]  
  []    []  
    [][]    
"""

    bracket = """
[][]    [][]
[]        []
            
            
[]        []
[][]    [][]
"""

    skull3 = """
  [][][][]  
[]  [][]  []
[][][][][][]
  [][][][]  
  []    []  
    [][]    
"""



    eye = """
[][][][][][]
[]        []
[]  [][]  []
[]  [][]  []
[]        []
[][][][][][]
"""
    hash = """
  []  []  
[][][][][]
  []  []  
[][][][][]
  []  []  
"""

    play = """
  []      
  [][]    
  [][][]  
  [][]    
  []      
"""

    pause = """
  []  []  
  []  []  
  []  []  
  []  []  
  []  []  
"""
    smiley = """
  []    []  
  []    []  
            
            
[]        []
  [][][][]  
"""
    love = """
  [][]  [][]  
[][][][][][][]
[][][][][][][]
  [][][]][[]  
    [][][]    
      []      
"""


    spacer = """
  []        []  
    []    []    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
[]  [][][][]  []
    []    []    
  [][]    [][]  
"""

    squid = """
      [][]      
    [][][][]    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
  []  [][]  []  
[]            []
  []        []  
"""
    
    ghost = """
      [][]    
    [][][][]  
  [][]  []  []
[][][][][][][]
[][][][][][][]
  []  []  []  
"""

    spacer2 = """
    []    []    
    []    []    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
[][][][][][][][]
[]  []    []  []
    []    []    
"""


    pi = """
[][][][][][]
  []    []  
  []    []  
  []    []  
"""


    
