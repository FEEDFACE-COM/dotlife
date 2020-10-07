
from dotlife.util import *

from fliplife import Mask, FRAMESIZE

from fliplife import http


class Pixel:
    
    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address = address
        self.nowrite, self.noread = nowrite,noread


    def read(self,x,y):
        y = FRAMESIZE.h - y - 1 
        if x >= FRAMESIZE.w or y >= FRAMESIZE.h:
            raise Error("invalid read pixel {:d}/{:d}".format(x,y))
        params = { 'x': x, 'y': y }
    
        val = False
        if not self.noread:
            rsp = http.get(self.address,"pixel",params)
            if rsp == None:
                raise Error("fail read pixel {:d}/{:d}".format(x,y))
            val = rsp.read()
    
        if val == b'X\x00':
            return True
        return False
    

    def flip(self,x,y,val=None):
    
        y = FRAMESIZE.h - y - 1 
        if x >= FRAMESIZE.w or y >= FRAMESIZE.h:
            error("invalid write pixel {:d}/{:d}".format(x,y))
            return False
    
        params = { 'x': x, 'y': y }
        rsp = None
    
        if val == None: # get current pixel value
            val = False
            if not self.noread:
                rsp = http.get(self.address,"pixel",params)    
                if rsp == None:
                    error("fail flip pixel {:d}/{:d}".format(x,y))
                    return False
                if rsp.read() == b'X\x00':
                    val = True

        ret = False
        if val == True:
            debug("pixel {:3d}/{:2d} flip ⬛︎ bright".format(x,y))
            if self.nowrite:
                return True
            rsp = http.post(self.address,"pixel",params,data=None)
            if rsp == None:
                error("fail flip bright pixel {:3d}/{:2d}".format(x,y))
                return False
            ret = rsp.read()

        elif val == False:
            debug("pixel {:3d}/{:2d} flip ⬜︎ dark".format(x,y))
            if self.nowrite:
                return False
            rsp = http.delete(self.address,"pixel",params)
            if rsp == None:
                error("fail flip dark pixel {:3d}/{:2d}".format(x,y))
                return False                
            ret = rsp.read()

                
        if ret == b'X\x00':
            return True
        return False
    

    
#    def flipDelta(self,prev,mask):
#        for y in range(FRAMESIZE.h):
#            for x in range(FRAMESIZE.w):
#                if mask[x,y] and not prev[x,y]:
#                    self.flip(x,y,True)
#                if not mask[x,y] and prev[x,y]:
#                    self.flip(x,y,False)
#        return
#
#
