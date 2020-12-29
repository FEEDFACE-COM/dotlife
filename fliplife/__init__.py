
from dotlife.util import *

import dotlife
from dotlife import font

FRAMESIZE = dotlife.Size(115,16)
DEFAULT_FONT = font.FONT.font3x5

def Mask(mask=None,size=FRAMESIZE):
    return dotlife.mask.Mask(mask=mask,size=size)
    
    



from fliplife.mode import test, read, clear, reset, fill, echo, exec
from fliplife.mode import grow, pixel, dots, life, glider, guns, spawn
from fliplife.mode import flueptext, pipe, scroll, clock, smooth, invader

class MODE(Enum):
#    test      = test.Test
    read      = read.Read
    clear     = clear.Clear
    reset     = reset.Reset
    fill      = fill.Fill
    echo      = echo.Echo
#    exec      = exec.Exec
    grow      = grow.Grow
#    pixel     = pixel.Pixel
    dots      = dots.Dots
    life      = life.Life
#    glider    = glider.Glider
#    guns      = guns.Guns
    spawn     = spawn.Spawn
    flueptext = flueptext.Flueptext
    pipe      = pipe.Pipe
#    scroll    = scroll.Scroll
    clock     = clock.Clock
#    smooth    = smooth.Smooth
    invader   = invader.Invader


