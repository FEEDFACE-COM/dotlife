
from dotlife.util import *

import dotlife
from dotlife import font


FRAMESIZE = dotlife.Size(8,8)
DEFAULT_FONT = font.FONT.font3x5

def Mask(mask=None,size=FRAMESIZE):
    return dotlife.mask.Mask(mask=mask,size=size)

def Buffer(val=0x00,size=FRAMESIZE):
    return dotlife.buffer.Buffer(val=val,size=size)

from oledlife.mode import fyi


class MODE(Enum):
    fyi       = fyi.FYI
