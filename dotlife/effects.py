
import random
from math import *

from dotlife import *
from dotlife.mask import Mask

def Checkers(size=Size(4,4)):
    ret = Mask(size=size)
    for y in range(ret.h):
        for x in range(ret.w):
            ret[x,y] = (x%2 != y%2)
    return ret



def Morph(fromMask,toMask):
    ret = [Mask(fromMask)]
    
    # scan for deltas
    diff = []
    for y in range(fromMask.h):
        for x in range(fromMask.w):
            if fromMask[x,y] != toMask[x,y]:
                diff += [ Position(x,y) ]

    m = Mask(fromMask)    
    
    # random delta order
    for d in range(len(diff)-1,-1,-1):
        r = random.randint(0,d)
        p = diff[r]
        
        m = Mask(m)
        m[p.x,p.y] = toMask[p.x,p.y]
        ret += [m]
        
        diff[r] = diff[d]
        diff[d] = p
    return ret
    
def Scan(fromMask,toMask):
    ret = [Mask(fromMask)]

    m = Mask(fromMask)    
    for y in range(fromMask.h):
        keep = False
        for x in range(fromMask.w):
            if m[x,y] != toMask[x,y]:
                m[x,y] = toMask[x,y]
                keep = True
        if keep:
            ret += [m]
        m = Mask(m)
    
    return ret

def Morph2(fromMask,toMask):
    ret = [Mask(fromMask)]
    
    # scan for deltas
    ons,offs = [],[]
    for y in range(fromMask.h):
        for x in range(fromMask.w):
            if fromMask[x,y] != toMask[x,y]:
                if toMask[x,y]:
                    ons += [ Position(x,y) ]
                else:
                    offs += [ Position(x,y) ]


    m = Mask(fromMask)    
    
    # random delta order
    while True:
        m = Mask(m)

        on = None
        if len(ons) > 0:
            r = random.randint(0,len(ons)-1)
            on = ons[r]
            ons = ons[:r] + ons[r+1:]
        
        off = None
        if len(offs) > 0:
            r = random.randint(0,len(offs)-1)
            off = offs[r]
            offs = offs[:r] + offs[r+1:]
        
    
        if on and off:
            m[on.x,on.y] = True
            m[off.x,off.y] = False
            ret += [m]
        elif on:
            m[on.x,on.y] = True
            ret += [m]
        elif off:
            m[off.x,off.y] = False
            ret += [m]
        else:
            break
        
                    
    return ret
    
    
def Border(size):
    ret = Mask(size=size)
    for x in range(ret.w):
        if x%2 == 0:
            ret[x,0] = True
        else:
            ret[x,ret.h-1] = True

    for y in range(ret.h):
        if y%2 == 0:
            ret[0,y] = True
            ret[ret.w-1,y] = True
    
    return ret
    

def Axis(size):
    ret = Mask(size=size)
    
    cx = int(floor(ret.w/2))
    cy = int(floor(ret.h/2))
    

    for x in range(ret.w):
        if x%2 != 0:
            ret[x,cy] = True

    for y in range(ret.h):
        if y%2 == 0:
            ret[cx,y] = True
    
    return ret
    
