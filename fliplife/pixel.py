
from dotlife.util import *

from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE

from fliplife import http


class Pixel:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    
    def __str__(self):
        return "".format(self.x,self.y)

def Read(address,x,y):
    y = FRAMEHEIGHT - y - 1 
    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
        debug("invalid read pixel {:d}/{:d}".format(x,y))
        return None
    params = { 'x': x, 'y': y }
    rsp = http.get(address,"pixel",params)
    if rsp == None:
        raise Error("fail read pixel {:d}/{:d}".format(x,y))
    val = rsp.read()
    if val == b'X\x00':
        return True
    return False

    
def Flip(address,x,y,val=None):
    y = FRAMEHEIGHT - y - 1 
    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
        debug("invalid write pixel {:d}/{:d}".format(x,y))
        return None

    params = { 'x': x, 'y': y }
    rsp = None

    if val == None: # get current pixel value
        rsp = http.get(address,"pixel",params)    
        if rsp == None:
            error("fail flip pixel {:d}/{:d}".format(x,y))
            return None
        if rsp.read() == b'X\x00':
            val = True
        else:
            val = False
    
    if val:
        debug("dot {:d}/{:d} flip on: ⬛︎".format(x,y))
        rsp = http.post(address,"pixel",params,data=None)
    else:
        debug("dot {:d}/{:d} flip off: ⬜︎".format(x,y))
        rsp = http.delete(address,"pixel",params)
    if rsp == None:
        raise Error("fail write pixel {:d}/{:d}".format(x,y))
    val = rsp.read()
    if val == b'X\x00':
        return True
    return False


def WriteDelta(address,prev,mask):
    for y in range(FRAMEHEIGHT):
        for x in range(FRAMEWIDTH):
            if mask[x,y] and not prev[x,y]:
                Flip(address,x,y,True)
            if not mask[x,y] and prev[x,y]:
                Flip(address,x,y,False)
    return
