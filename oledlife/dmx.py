

import serial

from dotlife.util import *

class DMXError(Error):
    pass

def debug(s): pass

class DMX:


    OFFSET    = 0xFF


    def __str__(self):
        return "dmx {}".format(self.device)
        
    def __init__(self,dev="/dev/foo"):
        self.device = dev
        self.serial = None

        BAUDRATE  = 115200
        TIMEOUT = 1.

        try:
            self.serial = serial.Serial(self.device, BAUDRATE, write_timeout=TIMEOUT)
        except ValueError as x:
            raise ValueError("fail open serial {} with baud {} timeout {}: {}".format(self.device,BAUDRATE,TIMEOUT,str(x)))
        except serial.SerialException as x:
            raise DMXError(x.strerror)
    
    
    def send(self,data):
        FRAMESIZE = 511

        TX_DMX_PACKET       = 6
        START_BYTE          = 0x7e
        END_BYTE            = 0xe7
        FRAMESIZE_LOW_BYTE  =  FRAMESIZE       & 0xff
        FRAMESIZE_HIGH_BYTE = (FRAMESIZE >> 8) & 0xff
    
        frame = bytearray(FRAMESIZE)
        frame[DMX.OFFSET:DMX.OFFSET+len(data)] = data
        
        packet = bytearray()
        packet.append( START_BYTE )
        packet.append( TX_DMX_PACKET )
        packet.append( FRAMESIZE_LOW_BYTE ) 
        packet.append( FRAMESIZE_HIGH_BYTE )
        packet.extend( frame )
        packet.append( END_BYTE )
        
#        debug("write {:d} byte: {:s} {:s} {:s}".format(
#            len(packet),
#            packet[0:4].hex(),
#            packet[4:-1].hex(),
#            packet[-1:].hex()
#        ))
        try:
            l = self.serial.write(packet)
            debug("wrote {:d} byte".format(l))
        except serial.serialutil.SerialTimeoutException as x:
            raise DMXError("dmx write timeout")
        except serial.SerialException as x:
            raise DMXError(x.strerror)


    
