
from dotlife.util import *

from dotlife import *
from dotlife.mask import Mask

class Pattern(Enum):

    def Mask(self,flip=Flip.noflip):
        ret = Mask.Load(self.value)
        ret.flip(flip)
        return ret



    FF = """
[][][][]
  [][]  
[][][][]
  [][]  
  [][]  
"""



    FYI= """
[][]  []  []  []
[]    []  []  []
[][]  [][][]  []
[]      []    []
"""



    GLIDER8x8 = ["""
                
                
    [][]        
    [][]        
    [][][][]    
    [][][][]    
[][]    [][]    
[][]    [][]    
""","""
                
                
    [][][][]    
    [][][][]    
[][]    [][]    
[][]    [][]    
        [][]    
        [][]    
""","""
                
                
    [][][][]    
    [][][][]    
        [][][][]
        [][][][]
    [][]        
    [][]        
""","""
                
                
    [][][][][][]
    [][][][][][]
            [][]
            [][]
        [][]    
        [][]    
""","""
        [][]    
        [][]    
        [][][][]
        [][][][]
    [][]    [][]
    [][]    [][]
                
                
""","""
        [][][][]
        [][][][]
    [][]    [][]
    [][]    [][]
            [][]
            [][]
                
                
"""]







    INVADER1= ["""
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


    INVADER2= ["""
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
"""],



    INVADER3= ["""
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
"""],


    HEXDIGIT= ["""
  []  
[]  []
[]  []
[]  []
  []  
""","""
  []  
[][]  
  []  
  []  
  []  
""","""
[][]  
    []
  []  
[]    
[][][]
""","""
[][]  
    []
  []  
    []
[][]  
""","""
[]    
[]  []
  [][]
    []
    []
""","""
[][][]
[]    
  []  
    []
[][]  
""","""
  []  
[]    
[][]  
[]  []
  []  
""","""
[][][]
    []
  []  
  []  
  []  
""","""
  []  
[]  []
  []  
[]  []
  []  
""","""
  []  
[]  []
  [][]
    []
  []  
""","""
  []  
[]  []
[][][]
[]  []
[]  []
""","""
[][]  
[]  []
[][]  
[]  []
[][]  
""","""
  [][]
[]    
[]    
[]    
  [][]
""","""
[][]  
[]  []
[]  []
[]  []
[][]  
""","""
[][][]
[]    
[][]  
[]    
[][][]
""","""
[][][]
[]    
[][]  
[]    
[]    
"""]



    DIGITS = ["""
  [][][]  
[]      []
[]    [][]
[]  []  []
[][]    []
[]      []
  [][][]  
""",""" 
    []    
  [][]    
    []    
    []    
    []    
    []    
  [][][]  
""","""
  [][][]  
[]      []
[]      []
[]      []
[]      []
[]      []
  [][][]  
""",""" 
    []    
  [][]    
    []    
    []    
    []    
    []    
    []    
""","""
  [][][]  
        []
        []
  [][][]  
[]        
[]        
  [][][]
""","""
  [][][]  
        []
        []
    [][]  
        []
        []
  [][][]  
""","""
      []  
[]    []  
[]    []  
  [][][][]
      []  
      []  
      []  
""","""
  [][][]  
[]        
[]  
  [][][]  
        []
        []
  [][][]  
""","""
  [][][]
[]        
[]        
  [][][]  
[]      []
[]      []
  [][][]  
""","""
  [][][][]
        []
      []
  [][][][] 
    []    
    []    
    []    
""","""
  [][][]  
[]      []
[]      []
  [][][]  
[]      []
[]      []
  [][][]  
""","""
  [][][]  
[]      []
[]      []
  [][][]  
        []
        []
  [][][]  
"""]





