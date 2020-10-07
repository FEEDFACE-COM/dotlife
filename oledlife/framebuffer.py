from dotlife import *
from dotlife.buffer import Buffer
from dotlife.util import *

from oledlife import FRAMESIZE

class FrameBuffer(Buffer):


    def __str__(self):
        ret = ""
        for y in range(FRAMESIZE.h):
            for x in range(FRAMESIZE.w):
                p = self.pixel[x][y]
                if p < 0x00:
                    ret += "¿?"
                elif p == 0x00:
                    ret += "  "
                elif p <= 0x01:
                    ret += " ."
                elif p <= 0x02:
                    ret += " ."
                elif p <= 0x10:
                    ret += " ▫︎"
                elif p <= 0x20:
                    ret += " □"
                elif p <= 0x40:
                    ret += " ◻︎"
                elif p <= 0x80:
                    ret += " ☐"
                elif p <= 0xff:
                    ret += " ◼︎"
                else:
                    ret += "?¿"
            ret += " {:01d}\n".format(y)

        for x in range(FRAMESIZE.w):
            ret += " {:01d}".format(x)
        ret += "  \n"
        
        return ret[:-1]



    def __init__(self,val=0x0):
        super().__init__(val=val,size=FRAMESIZE)
    

    def bytes(self):
        ret = bytearray(FRAMESIZE.w * FRAMESIZE.h)
        i = 0
        for y in range(FRAMESIZE.h):
            for x in range(FRAMESIZE.w):
                if y % 2 == 0:
                    col = x
                    try:
                        ret[i] = self.pixel[x][y]
                    except ValueError:
                        continue
                else: # fixup even rows
                    col = (FRAMESIZE.w-1-x) % FRAMESIZE.w
                    try:
                        ret[i] = self.pixel[col][y] 
                    except ValueError:
                        continue
                i += 1


        # fixup bum pixel
        if ret[3*FRAMESIZE.w] in [0x1, 0x2, 0x3]:
            ret[3*FRAMESIZE.w] += 1


        return ret


    
