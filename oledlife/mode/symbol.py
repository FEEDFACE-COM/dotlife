
import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.mode import Mode
#from dotlife.time import timer

from dotlife.symbols import Symbol


from oledlife import Mask, Buffer
from oledlife.mode import Mode


class Symbol(Mode):

    Pattern = dotlife.symbols.Symbol

    def start(self,pattern,**params):
        self.mask = pattern.Mask()
        return True
        
    def draw(self,light,**params):
        ret = Buffer()
        pos = Position()
        pos.x = int(abs(ret.w - self.mask.w)/2)
        pos.y = int(abs(ret.h - self.mask.h)/2)
        ret.addMask( self.mask, light=light, pos=pos )
        return ret


    def step(self,**params):
        pass

    flags = [
        ("l:","light=","light",1,"brightness",lambda x: int(x) ),
        Mode.FLAG("pattern",dotlife.symbols.Symbol.question)
    ]    


