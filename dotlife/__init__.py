
from dotlife.util import *
from enum import auto

LIGHT = 0x1
DARK  = 0x0


class Rotation(Enum):
    clockwise = auto()
    counterclockwise = auto()


class Operation(Enum):
	nop = auto()
	add = auto()
	sub = auto()
	

class Flip(Enum):
    noflip     = auto()
    horizontal = auto()
    vertical   = auto()
    point      = auto()


class Direction(Enum): 
    northwest= (-1,-1)
    north=     ( 0,-1)
    northeast= (+1,-1)
    east=      (+1, 0)
    southeast= (+1,+1)
    south=     ( 0,+1)
    southwest= (-1,+1)
    west=      (-1, 0)
    center=    ( 0, 0)


#class Palette(Enum):
#    Linear =    [  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16 ]
#    Custom =    [  1,  2,  3,  4,  5,  6,  7,  8,  9, 11, 13, 19, 29, 38, 51, 63 ] 

class Blend(Enum):
    jump  = auto()
    black = auto()
    frame = auto()


def Clamp(p): 
    if int(p) < 0:    return int(0x00)
    if int(p) > 0xff: return int(0xff)
    return int(p)


class Size():
    def __init__(self,w=0,h=0):
        self.w,self.h = w,h

    def __str__(self):
        return "{:d}x{:d}".format(self.w,self.h)

    def __add__(self,b):
        return Size(w=self.w+b.w, h=self.h+b.h)

DefaultSize = Size(8,8)


class Position():

    def __init__(self,x=0,y=0):
        self.x,self.y = x,y
        
    def __str__(self):
        return "{:d}/{:d}".format(self.x,self.y)
        
    def __add__(self,b):
        return Position(x=self.x+b.x, y=self.y+b.y)
        
    def __sub__(self,b):
        return Position(x=self.x-b.x, y=self.y-b.y)
    
