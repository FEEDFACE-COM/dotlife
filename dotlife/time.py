
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
    paused = False
    pausetime = 0.0
    
    
    def Init():
        Clock.timers = []
        Clock.start = datetime.datetime.now( datetime.timezone.utc )
        Clock.now   = 0.0
        Clock.frame = -1
        
            
    def Str():
        return "#{:05d} {:5.1f}s".format(Clock.frame,Clock.now/1000.)


    def fps(prev):
        (frame, time) = prev
        return float( (Clock.frame - frame) /  ((Clock.now - time)/1000.) )
        
    def Tick():
        if Clock.paused:
            Clock.frame += 1
            Clock.now = Clock.pausetime
        else:
            Clock.frame += 1
            Clock.now = (Clock.Elapsed() - Clock.pausetime) * CLOCK_RATE
        tmp = []
        for timer in Clock.timers:
            if timer.update():
                tmp += [ timer ]
        Clock.timers = tmp
            
    def Sleep(duration=1./FRAME_RATE):
        time.sleep( duration )
    
    
    def Pause(state=None):
        if state == None:
            state = Clock.paused ^ True
        Clock.paused = state
        Clock.pausetime = (Clock.Elapsed() - Clock.pausetime) * CLOCK_RATE
        info("clock {:s}".format( "paused" if Clock.paused else "unpaused"))
        
        
        
    
    def Timer(duration,repeat=0,fun=None):
        ret = Timer(duration,repeat,fun)
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
        
    def __init__(self,duration=1.,repeat=0, fun=None):
        self.count = 0     # times fired
        self.fired = False # fired this tick?
        self.fun = fun
        self.start = NOW()
        self.duration = duration
        self.repeat = repeat
        Clock.timers.append(self)
        
    def __str__(self):
        return "{:.1f}/{:.1f} {:4.2f} {:4.2f}π {:4.2f}∿ #{:d}{:s}".format(
            self.elapsed()/1000.,
            self.duration/1000.,
            self.fader(), 
            self.cycle()/math.PI,
            self.ease(),
            self.count,
            "/∞" if self.repeat==0 else "/{:d}".format(self.repeat),
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

            self.fired = True
            self.count += 1
            
            if self.fun: # fire!
                self.fun()
            
            if self.repeat == 0 or self.count < self.repeat:
                while self.start + self.duration < NOW():
                    self.start += self.duration 
                return True
                
            else: # finite repeats
                return False
                
            return False

        self.fired = False
        return True

        
        
        
        
