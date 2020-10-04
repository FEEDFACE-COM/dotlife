
from dotlife.util import *


#def Pattern(pattern):
#    ret = pattern
#    if pattern[0] == "\n":
#        self.pattern = self.pattern[1:]
#    if self.pattern[-1:] == "\n":
#        self.pattern = self.pattern[:-1]
#    
#
#
#class Pattern():
#
#    def __init__(self,pattern):
#        self.pattern = pattern.value
#        if self.pattern[0] == "\n":
#            self.pattern = self.pattern[1:]
#        if self.pattern[-1:] == "\n":
#            self.pattern = self.pattern[:-1]
#        
#    def __str__(self):
#        return self.pattern


class PATTERN(Enum):


    FF= """
[][][][]
  [][]  
[][][][]
  [][]  
  [][]  
"""

    DOTLIFE = """
    []            []    []          []        
    []          [][][]  []  []    []      []  
  []      []      []    []      [][][]  [][][]
[]  []  []  []    []    []  []    []    []    
  []      []      []    []  []    []      [][]
"""


    FLIPLIFE = """
    []  []              []          []        
  []    []  []          []  []    []      []  
[][][]  []        []    []      [][][]  [][][]
  []    []  []  []  []  []  []    []    []    
  []    []  []  [][]    []  []    []      [][]
                []                                 
                []                                 
"""



    DOTLIFE2 = """
[][]      []    [][][]  []      []  [][][]  [][][]
[]  []  []  []    []    []          []      []    
[]  []  []  []    []    []      []  [][][]  [][][]
[]  []  []  []    []    []      []  []      []    
[][]      []      []    [][][]  []  []      [][][]
"""

    FLIPLIFE2 = """
  [][]  []  []    []    []  []  [][]  [][]
  []    []      []  []  []      []    []  
  [][]  []  []  [][]    []  []  [][]  [][]
  []    []  []  []      []  []  []    []  
  []    []  []  []      []  []  []    [][]
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




    SYMBOLS= ["""
[][][]  
      []
    []  
  []    
        
  []    
""","""
  [][][][][]  
[][][][][][][]
[]    []    []
[][][][][][][]
[][][]  [][][]
[][][]  [][][]
  [][][][][]  
  []  []  []  
""","""
  [][][][]  
[][][][][][]
[]  [][]  []
[][][][][][]
  [][][][]  
  []    []  
    [][]    
""","""
[][]    [][]
[]        []
            
            
[]        []
[][]    [][]
""","""
  [][][][]  
[]  [][]  []
[][][][][][]
  [][][][]  
  []    []  
    [][]    
""","""
[][][][][][]
[]        []
[]  [][]  []
[]  [][]  []
[]        []
[][][][][][]
""","""
  []  []  
[][][][][]
  []  []  
[][][][][]
  []  []  
""","""
  []      
  [][]    
  [][][]  
  [][]    
  []      
""","""
  []  []  
  []  []  
  []  []  
  []  []  
  []  []  
""","""
  []    []  
  []    []  
            
            
[]        []
  [][][][]  
""","""
  [][]  [][]  
[][][][][][][]
[][][][][][][]
  [][][]][[]  
    [][][]    
      []      
""","""
  []        []  
    []    []    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
[]  [][][][]  []
    []    []    
  [][]    [][]  
""","""
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
  [][]  []  []
[][][][][][][]
[][][][][][][]
  []  []  []  
""","""
    []    []    
    []    []    
  [][][][][][]  
[][]  [][]  [][]
[][][][][][][][]
[][][][][][][][]
[]  []    []  []
    []    []    
"""]

    PI = """
[][][][][][]
  []    []  
  []    []  
  []    []  
"""

    LOVE = """
  [][]  [][]  
[][][][][][][]
[][][][][][][]
  [][][]][[]  
    [][][]    
      []      
"""




