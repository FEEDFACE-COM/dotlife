
from dotlife import *
from dotlife.util import *
from oledlife.mode import *

from dotlife.buffer import Buffer


class Clear(Mode):

    def start(self,**params):
        log("start clear")
        self.buffer = Buffer()
        return False
        
    
    def draw(self,**params):
        
        return self.buffer
        
    
