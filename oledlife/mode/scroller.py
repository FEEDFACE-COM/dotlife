
from dotlife.util import *
from dotlife.mode import Mode

from dotlife.buffer import Buffer

from oledlife.mode import Mode

def Init(timer):
    return Scroller(timer)


class Scroller(Mode):
    
    text = "3.1415926535897932384626433832795028841971693993751058209749445920"
    
    def start(self,**params):
        pass        
    
    def draw(self,**params):
        buffer = Buffer()
        return buffer

