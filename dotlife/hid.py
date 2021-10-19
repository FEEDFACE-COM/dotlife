

import os
import hid
import struct

from dotlife.util import *

class HIDError(Error):
    pass

class Key(Enum):
    left  = "LEFT"
    right = "RGHT"
    top0  = "TOP0"
    top1  = "TOP1"
    top2  = "TOP2"

class State:

    def __str__(self):
        ret = ""
        ret += "RAW {:+03x} {:02x} {:02x} {:02x} {:02x}  ".format(self.raw[0],self.raw[1],self.raw[2],self.raw[3],self.raw[4])
        ret += "DIAL {:04.2f}".format( float(self.dial)/256. )
        if self.jog != 0:
            ret += " JOG {:+02d}".format( self.jog )
        else:
            ret += "       "
        for k in Key:
            if self.key[k]:
                ret += " " + str(k.value)
            else:
                ret += "     "
        return ret


    def __init__(self,val=0x0):
        self.key= {}
        self.dial = 0x00
        self.jog  = 0x00
        for k in Key:
            self.key [ k ] = False
      
 
        if len(val) != 5:
            error("state() with len(val) != 5")
            dump(val)
            return

        self.raw = struct.unpack("bBBBB", val)
        
        self.jog  = self.raw[0] 
        self.dial  = self.raw[1]   

        self.key[Key.left]  = self.raw[3] >> 4 & 0x1
        self.key[Key.right] = self.raw[4] & 0x1
        self.key[Key.top0]  = self.raw[3] >> 5 & 0x1
        self.key[Key.top1]  = self.raw[3] >> 6 & 0x1
        self.key[Key.top2]  = self.raw[3] >> 7 & 0x1
        




class HID:

    VENDOR  = 0x0b33
    PRODUCT = 0x0020


    def __str__(self):
        return "hid".format()

    def __init__(self):
        self.dev = None 
        try:
            self.dev = hid.Device(HID.VENDOR,HID.PRODUCT)
        except Exception as x:
            raise HIDError("fail open device 0x{:04x} 0x{:04x}: {:s}".format(HID.VENDOR,HID.PRODUCT,str(x)))

        debug("hid vendor {:s}".format(self.dev.manufacturer))
        debug("hid product {:s}".format(self.dev.product))

        self.dev.nonblocking = True

    def read(self):
        ret = None
        try:
            val = self.dev.read(5)    
        except hid.HIDException as x:
            raise HIDError("fail read device: {:s}".format(str(x)))
        if len(val) <= 0:
            return False
        return State(val)




