

from dotlife.util import *
import dotlife.mode

from oledlife import DEFAULT_FONT


#
# to add a new mode 'foobar':
#   1. add 'from oledlife.mode import foobar'
#   2. add 'foobar = "foobar.Foobar"' to Enum oledlife.MODE
#   3. create class Foobar(oledlife.mode.Mode) in oledlife/mode/foobar.py
#



class Mode(dotlife.mode.Mode):

    help = ""

    def __init__(self,timer,buffer,**params):
        super().__init__(timer,**params)
        self.buffer = buffer


    def start(self,**params):
        return super().start()
        
    def draw(self,**params):
        return Buffer()

    FLAGS = [
        dotlife.mode.Mode.FLAG("speed"),
    ]
    
    flags = []








