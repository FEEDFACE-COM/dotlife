
from dotlife import *
from dotlife.util import *
from oledlife.mode import *

from dotlife.buffer import Buffer


class Style(Enum): # need to make it tuple: foo = ( lambda x: pass, ) # otherwise foo becomes a method
    ranges = ( lambda x: Buffer.Ranges(mul=(x % 4 + 1)), )
    shades = ( lambda x: Buffer.SixtyFourShadesOfGrey(mul=(x % 4 + 1)), )
    checks = ( lambda x: Buffer.Checkers(black=(x%2 * 0x80), white=((1 - x%2) * 0x80)), )
    grades = ( lambda x: Buffer.Gradient(heading={ 0: Direction.north, 1: Direction.west, 2: Direction.south, 3: Direction.east }[x%4]), )



class Fill(Mode):


#    DefaultStyle = Style.grades
    Style = Style
    

    
    def start(self,style,**params):
        info("start test {:}".format(style))
        return True
    
    def draw(self,style,step,**params):
        c = int(self.timer.count) % 4
        debug("draw test {:}#{:d}".format(style,c))
        fun, = style.value
        buf = fun( c )
        return buf
        


    flags = [
        Mode.FLAG("step"),
        Mode.FLAG("style",Style.checks),
    ]
    