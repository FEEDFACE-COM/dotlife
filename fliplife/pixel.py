
from dotlife.util import *

from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE

from fliplife import http


class Pixel:
    
    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address = address
        self.nowrite, self.noread = nowrite,noread


    def read(self,x,y):
        y = FRAMEHEIGHT - y - 1 
        if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
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
    
        y = FRAMEHEIGHT - y - 1 
        if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
            raise Error("invalid write pixel {:d}/{:d}".format(x,y))
    
        params = { 'x': x, 'y': y }
        rsp = None
    
        if val == None: # get current pixel value
            val = False
            if not self.noread:
                rsp = http.get(self.address,"pixel",params)    
                if rsp == None:
                    raise Error("fail flip pixel {:d}/{:d}".format(x,y))
                if rsp.read() == b'X\x00':
                    val = True
        ret = False
        if val == True:
            debug("dot {:d}/{:d} flip bright: ⬛︎".format(x,y))
            if self.nowrite:
                return True
            rsp = http.post(self.address,"pixel",params,data=None)
            if rsp == None:
                raise Error("fail bright pixel {:d}/{:d}".format(x,y))
            ret = rsp.read()

        elif val == False:
            debug("dot {:d}/{:d} flip dark: ⬜︎".format(x,y))
            if self.nowrite:
                return False
            rsp = http.delete(self.address,"pixel",params)
            if rsp == None:
                raise Error("fail dark pixel {:d}/{:d}".format(x,y))
            ret = rsp.read()

                
        if ret == b'X\x00':
            return True
        return False
    

    
    def flipDelta(self,prev,mask):
        for y in range(FRAMEHEIGHT):
            for x in range(FRAMEWIDTH):
                if mask[x,y] and not prev[x,y]:
                    self.flip(x,y,True)
                if not mask[x,y] and prev[x,y]:
                    self.flip(x,y,False)
        return


#def Read(address,x,y):
#    y = FRAMEHEIGHT - y - 1 
#    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
#        debug("invalid read pixel {:d}/{:d}".format(x,y))
#        return None
#    params = { 'x': x, 'y': y }
#    rsp = http.get(address,"pixel",params)
#    if rsp == None:
#        raise Error("fail read pixel {:d}/{:d}".format(x,y))
#    val = rsp.read()
#    if val == b'X\x00':
#        return True
#    return False

    
#def Flip(address,x,y,val=None):
#    y = FRAMEHEIGHT - y - 1 
#    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
#        debug("invalid write pixel {:d}/{:d}".format(x,y))
#        return None
#
#    params = { 'x': x, 'y': y }
#    rsp = None
#
#    if val == None: # get current pixel value
#        rsp = http.get(address,"pixel",params)    
#        if rsp == None:
#            error("fail flip pixel {:d}/{:d}".format(x,y))
#            return None
#        if rsp.read() == b'X\x00':
#            val = True
#        else:
#            val = False
#    
#    if val:
#        debug("dot {:d}/{:d} flip on: ⬛︎".format(x,y))
#        rsp = http.post(address,"pixel",params,data=None)
#    else:
#        debug("dot {:d}/{:d} flip off: ⬜︎".format(x,y))
#        rsp = http.delete(address,"pixel",params)
#    if rsp == None:
#        raise Error("fail write pixel {:d}/{:d}".format(x,y))
#    val = rsp.read()
#    if val == b'X\x00':
#        return True
#    return False
#

#def WriteDelta(address,prev,mask):
#    for y in range(FRAMEHEIGHT):
#        for x in range(FRAMEWIDTH):
#            if mask[x,y] and not prev[x,y]:
#                Flip(address,x,y,True)
#            if not mask[x,y] and prev[x,y]:
#                Flip(address,x,y,False)
#    return
