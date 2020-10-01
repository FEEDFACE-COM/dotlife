
from dotlife.util import *

from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE

from fliplife import http


def Get(address,x,y):
    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
        debug("invalid get pixel {:d}/{:d}".format(x,y))
        return None
    params = { 'x': x, 'y': y }
    rsp = http.get(address,"pixel",params)
    if rsp == None:
        raise Error("fail get pixel {:d}/{:d}".format(x,y))
    val = rsp.read()
    if val == b'X\x00':
        return True
    return False

    
def Post(address,x,y):
    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
        debug("invalid post pixel {:d}/{:d}".format(x,y))
        return None
    params = { 'x': x, 'y': y }
    rsp = http.post(address,"pixel",params,data=None)
    if rsp == None:
        raise Error("fail post pixel {:d}/{:d}".format(x,y))
    val = rsp.read()
    if val == b'X\x00':
        return True
    return False
    

def Delete(address,x,y):
    if x >= FRAMEWIDTH or y >= FRAMEHEIGHT:
        debug("invalid delete pixel {:d}/{:d}".format(x,y))
        return None
    params = { 'x': x, 'y': y }
    rsp = http.delete(address,"pixel",params)
    if rsp == None:
        raise Error("fail delete pixel {:d}/{:d}".format(x,y))
    val = rsp.read()
    if val == b'X\x00':
        return True
    return False
