from dotlife import *

from dotlife.util import *

from oledlife import Buffer, FRAMESIZE

from oledlife.dmx import DMX


def debug(x): pass

class Paneloled():

    def send(self,buf):
        data = Paneloled.dataFromBuffer(buf)
        debug("framebuffer write {}".format(str(buf.size())))
        if not self.nowrite:
            self.dmx.send( data )
                
            
        

    def __init__(self,device,nowrite,val=0x0):
        super().__init__()
        self.dmx = None
        if device and not nowrite:
            try:
                info("open dmx {}".format(device))
                self.dmx = DMX(device)
            except Error as x:
                FATAL("open dmx {}: {}".format(device,x))
        self.nowrite = nowrite
    



    @classmethod
    def dataFromBuffer(self,buf):
        ret = bytearray(FRAMESIZE.w * FRAMESIZE.h)
        i = 0
        for y in range(FRAMESIZE.h):
            for x in range(FRAMESIZE.w):
                if y % 2 == 0:
                    col = x
                    try:
                        ret[i] = buf[x,y]
                    except ValueError:
                        continue
                else: # fixup even rows
                    col = (FRAMESIZE.w-1-x) % FRAMESIZE.w
                    try:
                        ret[i] = buf[col,y] 
                    except ValueError:
                        continue
                i += 1

        # fixup bum pixel
        if ret[3*FRAMESIZE.w] in [0x1, 0x2, 0x3]:
            ret[3*FRAMESIZE.w] += 1

        return ret


