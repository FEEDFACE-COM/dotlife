
from dotlife.util import *

from fliplife.mask import Mask
from fliplife import http
    
Full = 0
Differential = 1


def GetMode(address):
    rsp = http.get(address,"rendering/mode",None)
    if rsp == None:
        return None
    val = rsp.read()
    if val == b"0\n\x00":
        return Full
    if val == b"1\n\x00":
        return Differential
    return None


def SetMode(address,data):
    
    data = "{:d}".format(data).encode()

    rsp = http.put(address,"rendering/mode",None,data)
    if rsp == None:
        return None
    val = rsp.read()
    return 0



def GetTimings(address):
    rsp = http.get(address,"rendering/timings",None)
    if rsp == None:
        return None
    val = rsp.read()
    # todo
    return None



