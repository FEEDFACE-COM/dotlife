
from dotlife.util import *


FRAMEWIDTH = 8
FRAMEHEIGHT = 8
FRAMESIZE = (FRAMEWIDTH,FRAMEHEIGHT)


LIGHT = 0x1
DARK  = 0x0



class Rotation(Enum):
    Clockwise = "clockwise" #auto()
    CounterClockwise = "counterclockwise" #auto()


class Operation(Enum):
	Nop = "nop" #auto()
	Add = "add" #auto()
	Sub = "sub" #auto()
	

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
    Jump  = "jump" #auto()
    Black = "black" # auto()
    Frame = "frame" # auto()


def Clamp(p): 
    if int(p) < 0:    return int(0x00)
    if int(p) > 0xff: return int(0xff)
    return int(p)


