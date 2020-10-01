
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
    log("got rendering mode " + str(val))
    if val == b"0\n\x00":
        return Full
    if val == b"1\n\x00":
        return Differential
    return None


def PutMode(address,data):
    
    data = "{:d}".format(data).encode()

    rsp = http.put(address,"rendering/mode",None,data)
    if rsp == None:
        return None
    val = rsp.read()
    log("sot rendering mode " + str(val))
    return 0



def GetTimings(address):
    rsp = http.get(address,"rendering/timings",None)
    if rsp == None:
        return None
    val = rsp.read()
    log("got rendering timings " + str(val))
    # todo
    return None



