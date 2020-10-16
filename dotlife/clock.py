
import datetime, time

from dotlife.util import *
import dotlife.math as math


def NOW():
    return Clock.now

def FRAME():
    return Clock.frame    




    
CLOCK_RATE = 1.0    
FRAME_RATE = 60.

class Clock:

    start = datetime.datetime.now( datetime.timezone.utc )
    now   = 0.0
    frame = -1
    timers = []
    
    def Init():
        Clock.timers = []
        Clock.start = datetime.datetime.now( datetime.timezone.utc )
        Clock.now   = 0.0
        Clock.frame = -1
        
            
    def Str():
        return "#{:05d} {:5.1f}s".format(Clock.frame,Clock.now/1000.)
        
    def Tick():
        Clock.now = Clock.Elapsed() * CLOCK_RATE
        Clock.frame += 1
        tmp = []
        for timer in Clock.timers:
            if timer.update():
                tmp += [ timer ]
        Clock.timers = tmp
            
    def Sleep(duration=1./FRAME_RATE):
        time.sleep( duration )
    
    def Timer(duration,repeat=True):
        ret = Timer(duration,repeat)
#        Clock.timers.append(ret)
#        debug("clock timer {}".format( ret ) )
        return ret
    
    def Elapsed(): # miliseconds
        delta = datetime.datetime.now( datetime.timezone.utc ) - Clock.start
        ret = 0.0
        ret += float(delta.days * 24 * 60 * 60) * 1000.
        ret += float(delta.seconds) * 1000.
        ret += float(delta.microseconds) /1000.
        return ret

    
    
class Timer():
        
    def __init__(self,duration=1.,repeat=True):
        self.count = 0     # times fired
        self.fired = False # fired this tick?
        self.fun = None
        self.start = NOW()
        self.duration = duration
        self.repeat = repeat
        Clock.timers.append(self)
        
    def __str__(self):
        return "{:.1f}/{:.1f}{:s} {:4.2f} {:4.2f}π {:4.2f}∿  #{:d}".format(
            self.elapsed()/1000.,
            self.duration/1000.,
            "r" if self.repeat else " ",
            self.fader(), 
            self.cycle()/math.PI,
            self.ease(), 
            self.count
        )

    def elapsed(self):
        return NOW() - self.start

    def active(self):
        t = self.elapsed()
        return t >= 0.0 and t <= self.duration

    def fader(self): # 0..1 linearly
        t = self.elapsed()
        if t <= 0.0:
            return 0.0
        if t >= self.duration:
            return 1.0
        return t / self.duration
       

    def cycle(self): # 0..2π linearly
        return math.TAU * self.elapsed() / self.duration
        

    def linear(self,freq=1.): # 0..1 linear
        t = self.elapsed()
        if freq*t <= 0.0:
            return 0.0
        if freq*t >= self.duration:
            return 1.0
        return freq * t / self.duration        
                
    def ease(self,freq=1.): # 0..1 smooth
        t = self.elapsed()
        if freq*t <= 0.0:
            return 0.0
        if freq*t >= self.duration:
            return 1.0
        return - 0.5 * math.cos( freq*t/self.duration * math.PI ) + 0.5 
        
    def sin0(self,freq=1.,phase=0.): # 0..1 cosine
        return - 0.5 * math.cos( freq * self.elapsed() / self.duration * math.TAU + phase ) + 0.5

    def sin(self,freq=1.,phase=0.): # -1..1 cosine
        return math.cos( freq * self.elapsed() / self.duration * math.TAU + phase )

            
    def update(self): # returns True to keep, False to discard
        if NOW() > self.start + self.duration: # triggered?

            self.count += 1
            self.fired = True
            
            if self.fun: # fire!
                self.fun()
            
            if self.repeat:
                while self.start + self.duration < NOW():
                    self.start += self.duration 
                return True
                
            return False

        self.fired = False
        return True

        
        
        
        
