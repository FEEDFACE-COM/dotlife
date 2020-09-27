

import dotlife
from dotlife import *
from dotlife.math import *
from dotlife.buffer import Buffer

class Palette():

    def __init__(self,color=None):
        self.color = color if color else [ LIGHT ]
        self.length = len(self.color)


    def idx(self,x):
        ret= ( int( float(self.length - 1) * x )  )
        return ret


            
    def __getitem__(self,idx):
        if idx < 0:
            return self.color[0]
        if idx >= self.length:
            return self.color[self.length-1]
        return self.color[ idx ]

    def __setitem__(self,idx,val):
        if 0 <= idx < self.length:
            self.color[ idx ] = val

    def __str__(self):
        return "{:s}".format(str(self.color))

    def reverse(self):
        self.color.reverse()
        return self
        
    def append(self,palette):
        self.color += palette.color
        self.length = len(self.color)
        return self

    def add(self,val):
        for i in range(self.length):
             self.color[i] += val
        return self

    def Polynom(min=1):
        return Palette( [ (x+min) for x in range(0,16) ] + [ (x+1)*2 for x in range(8,16) ] + [ (x+1)*4 for x in range(8,16) ])

    def Linear(min=1):
        return Palette( [ (x+min) for x in range(0,32) ] )
    
    def Quadratic(min=1):
        return Palette( [ (x+min)*2 for x in range(0,32) ] )# + [ (x+1)*2 for x in range(16,32) ] )
    
    
    def Sine(freq=1.,amp=32.0):
        pal = [ 0 for x in range(0,32) ]
        for x in range(len(pal)):
            phi = x / len(pal) * TAU
            pal[x] = int( (amp-1.) * sine( freq*phi ) + 1. )
        return Palette( pal )
        

