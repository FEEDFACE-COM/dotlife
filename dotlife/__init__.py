
from dotlife.util import *
from enum import Enum, auto

LIGHT = 0x1
DARK  = 0x0

class Rotation(Enum):
    Clockwise = auto()
    CounterClockwise = auto()


class Operation(Enum):
	Nop = auto()
	Add = auto()
	Sub = auto()
	

class Axis(Enum):
    Horizontal = auto()
    Vertical   = auto()

class Direction(Enum): 
    NorthWest= (-1,-1)
    North=     ( 0,-1)
    NorthEast= (+1,-1)
    East=      (+1, 0)
    SouthEast= (+1,+1)
    South=     ( 0,+1)
    SouthWest= (-1,+1)
    West=      (-1, 0)
    Center=    ( 0, 0)


#class Palette(Enum):
#    Linear =    [  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16 ]
#    Custom =    [  1,  2,  3,  4,  5,  6,  7,  8,  9, 11, 13, 19, 29, 38, 51, 63 ] 

class Blend(Enum):
    Jump  = auto()
    Black = auto()
    Frame = auto()


def Clamp(p): 
    if int(p) < 0:    return int(0x00)
    if int(p) > 0xff: return int(0xff)
    return int(p)


class Size():
    def __init__(self,w=0,h=0):
        self.w,self.h = w,h

    def __str__(self):
        return "{:d}x{:d}".format(self.w,self.h)


class Position():

    def __init__(self,x=0,y=0):
        self.x,self.y = x,y
        
    def __str__(self):
        return "{:d}/{:d}".format(self.x,self.y)
        
    def __add__(self,b):
        return Position(x=self.x+b.x, y=self.y+b.y)
        
    def __sub__(self,b):
        return Position(x=self.x-b.x, y=self.y-b.y)
    
