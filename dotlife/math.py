
import math

PI  =      math.pi
TAU = 2. * math.pi

def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)
    
def ease(x):
    return - 0.5 * math.cos( x ) + 0.5 

def floor(x):
    return math.floor(x)

def ceil(x):
    return math.ceil(x)
    
def sine(x,amp=1., freq=1.,phase=0.):      # 0..2π -> 0..1..0 cosine
    return amp * - 0.5 * math.cos( freq * x + phase ) + 0.5



