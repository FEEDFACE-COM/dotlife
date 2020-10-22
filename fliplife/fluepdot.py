
from dotlife.util import *


from fliplife.framebuffer import Framebuffer
from fliplife.rendering import Rendering
from fliplife.pixel import Pixel
from fliplife import http

from fliplife import FRAMESIZE, Mask


class Fluepdot():

    class Mode(Enum):
        full = b"0\n\x00"
        diff = b"1\n\x00"


    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address = address
        self.nowrite, self.noread = nowrite,noread
        if self.noread:
            self.nowrite = True
        self.buffer = Framebuffer(self.address,self.nowrite,self.noread)
        self.pixel = Pixel(self.address,self.nowrite,self.noread)
        self.rendering = Rendering(self.address,self.nowrite,self.noread)


    def text(self,x,y,font,msg):
        params = {
            'x': x,
            'y': y,
            'font': font
        }
        ret = Mask()
        debug("text {:s}".format(msg))
        if not self.nowrite:
            rsp = http.post(self.address,"framebuffer/text",params,data=msg)
            ret = Framebuffer.MaskFromResponse(rsp)
            
        return ret            



