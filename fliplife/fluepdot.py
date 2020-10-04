
from dotlife.util import *

from fliplife.framebuffer import Framebuffer
from fliplife.rendering import Rendering    
from fliplife.pixel import Pixel


class Fluepdot():

    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address = address
        self.nowrite, self.noread = nowrite,noread
        if self.noread:
            self.nowrite = True
        self.buffer = Framebuffer(self.address,self.nowrite,self.noread)
        self.pixel = Pixel(self.address,self.nowrite,self.noread)
        self.rendering = Rendering(self.address,self.nowrite,self.noread)
        