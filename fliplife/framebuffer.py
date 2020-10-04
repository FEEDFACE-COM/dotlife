
from dotlife.util import *

import fliplife
from fliplife import http

from fliplife.mask import Mask






class Framebuffer(fliplife.mask.Mask):
    
    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address, self.nowrite, self.noread = address,nowrite,noread


    def write(self,mask):
        data = mask.toData()
        ret = mask
        debug("framebuffer write {:s}".format(self.address))
        if not self.nowrite:
            rsp = http.post(self.address,"framebuffer",None,data)
            ret = Mask.MaskFromResponse(rsp)
        return ret
        
    
    def read(self):
        ret = Mask()
        debug("framebuffer read {:s}".format(self.address))
        if not self.noread:
            rsp = http.get(self.address,"framebuffer",None)
            ret = Mask.MaskFromResponse(rsp)
        return ret

        
    
    def text(self,x,y,font,msg):
        params = {
            'x': x,
            'y': y,
            'font': font
        }
        ret = Mask()
        debug("framebuffer text {:s}".format(self.address))
        if not self.nowrite:
            rsp = http.post(self.address,"framebuffer/text",params,data=msg)
            ret = Mask.MaskFromResponse(rsp)
            
        return ret            



    
