
from dotlife.util import *

from fliplife.mask import Mask
from fliplife import http
    


def Get(address):
    rsp = http.get(address,"framebuffer",None)
    ret = Mask.MaskFromResponse(rsp)
    return ret


def Post(address,mask):
    data = mask.toData()
    rsp = http.post(address,"framebuffer",None,data)
    ret = Mask.MaskFromResponse(rsp)
    return ret


def Text(address,x,y,font,msg):
    params = {
        'x': x,
        'y': y,
        'font': font
    }
    rsp = http.post(address,"framebuffer/text",params,data=msg)
    ret = Mask.MaskFromResponse(rsp)
    return ret
        