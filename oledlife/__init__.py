
from dotlife.util import *

import dotlife
from dotlife import font


FRAMESIZE = dotlife.Size(8,8)
DEFAULT_FONT = font.FONT.font3x5

def Mask(mask=None,size=FRAMESIZE):
    return dotlife.mask.Mask(mask=mask,size=size)

def Buffer(val=0x00,size=FRAMESIZE):
    return dotlife.buffer.Buffer(val=val,size=size)

from oledlife.mode import test, clear, glider, fyi, fill
from oledlife.mode import fire, tunnel, invader, plasma, pulser
from oledlife.mode import scroller, tetris, palette, draft, symbol
from oledlife.mode import clock

class MODE(Enum):
    test      = test.Test
    clear     = clear.Clear
    fyi       = fyi.FYI
    glider    = glider.Glider
    fill      = fill.Fill
    fire      = fire.Fire
    tunnel    = tunnel.Tunnel
    invader   = invader.Invader
    plasma    = plasma.Plasma
    pulser    = pulser.Pulser
    scroller  = scroller.Scroller
    tetris    = tetris.Tetris
    palette   = palette.Palette
    draft     = draft.Draft
    symbol    = symbol.Symbol
    clock     = clock.Clock


