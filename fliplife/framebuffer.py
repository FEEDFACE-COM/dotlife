

import dotlife
from dotlife.util import *

from fliplife import http

from fliplife import Mask, FRAMESIZE



def debug(x): pass



class Framebuffer(dotlife.mask.Mask):
    
    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address, self.nowrite, self.noread = address,nowrite,noread


    def write(self,mask):
        data = Framebuffer.dataFromMask(mask)
        ret = mask
        debug("framebuffer write {}".format(str(mask.size())))
        if not self.nowrite:
            rsp = http.post(self.address,"framebuffer",None,data)
            ret = Framebuffer.MaskFromResponse(rsp)
        return ret
        
    
    def read(self):
        ret = Mask()
        debug("framebuffer read")
        if not self.noread:
            rsp = http.get(self.address,"framebuffer",None)
            ret = Framebuffer.MaskFromResponse(rsp)
        return ret

    

    @classmethod
    def dataFromMask(self,mask):
        ret = ""
        for y in range(0,mask.h):
            row = ""
            for x in range(0,mask.w):
                if mask[x,y]:
                    row += "X"
                else:
                    row += " "
            row += "\n"
            ret += row 
        return ret


    @classmethod
    def MaskFromResponse(self,rsp):
        ret = Mask(size=FRAMESIZE)
        x,y = 0,0
        if rsp == None:
            return
        for row in rsp:
            if y >= FRAMESIZE.h:
                raise Error("invalid response: line count {} > {}".format(y,FRAMESIZE.h))                 
            x = 0
            for col in row:
                if x > FRAMESIZE.w:
                    raise Error("invalid response: column count {} > {}".format(x,FRAMESIZE.w))                 
                if col == 0x0A:
                    pass
                elif col == 0x20:
                    ret[x,y] = False
                else:
                    ret[x,y] = True
                x+=1
            y+=1
        return ret
