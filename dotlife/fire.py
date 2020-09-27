
import dotlife
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.math import *
from dotlife.util import *
from dotlife.palette import Palette

import random

class Fire():

    def __init__(self):
        self.state = Buffer(size=(FRAMEWIDTH,FRAMEHEIGHT+4))
        random.seed()
        for x in range(self.state.w):
            self.state[x,self.state.h-1] = 1+ random.randrange( 12 )
        pass


    def step(self):
#        for y in range(1,self.state.h):
#            for x in range(self.state.w-1,1,-1):
#                sum = self.state[x-1,y-1] + self.state[x,y-1] + self.state[x+1,y-1] + self.state[x,y-2]
#                self.state[x,y] = int( sum/4 )
        for x in range(self.state.w):
#            self.state[x,self.state.h-1] = random.randrange( 8 ) + random.randrange( 8 ) 
            self.state[x,self.state.h-1] = random.randrange( 16 )# + random.randrange( 8 ) 
        for y in range(0,self.state.h-1):
            for x in range(self.state.w):
                sum = self.state[x-1,y+1] + self.state[x,y+1] + self.state[x+1,y+1] + self.state[x,y+2]
                self.state[x,y] = int(sum/4.1)
                
        
        
    def buffer(self, mask=None):

        tmp = self.state.buffer(pos=(0,0))
        ret = tmp.palette( Palette.Polynom(0) )
        
        
        return ret
        
