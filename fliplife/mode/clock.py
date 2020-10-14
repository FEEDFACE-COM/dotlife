
import random, datetime

import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.math import *


import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.clock import Clock
from dotlife.font import Font, FONT
from dotlife.effects import Morph, Morph2, Axis, Scan

from enum import auto

class LAYOUT(Enum):
    large = auto()
    small = auto()
    dual   = auto()  
    detail = auto()   


class Clock(Mode):
    
    
    
    def run(self,msg=None,**params):
#        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)
        
        self.small = Font(FONT.font3x5) 
        self.fixed = Font(FONT.fix3x5)
        self.large = Font(FONT.font5x5)
        

        now = datetime.datetime.now()
        info("start clock: {:s}".format(now.strftime("%F %T")))


#        p0 = int(math.floor(FRAMESIZE.w / (self.font5.size.w+1)))
#        p1 = p0 - len(msg)
#        self.pos0 = Position((self.font5.size.w+1)*int(p1/2),int(self.font5.size.h/1))
        
        self.mask = self.tick(now,**params)
#        text = self.font.render(msg,fixed=True)
#        p0 = int(math.floor(FRAMESIZE.w / (self.font.size.w+1)))
#       p1 = p0 - len(msg)
#        self.pos0 = Position((self.font.size.w+1)*int(p1/2),int(self.font.size.h/1))
        
#       self.mask.addMask(text,pos=self.pos0,wrap=True)
        
        self.fluepdot.buffer.write(self.mask)
        
        
        return True
    
    
    
    def tick(self,now,layout,**params):
        ret = Mask()
        now = datetime.datetime.now()



        
        
        log("tick "+now.strftime("%F %T"))
        if layout in [ LAYOUT.small, LAYOUT.large]:
            date_time = now.strftime("%F %T")
            font = self.large
            if layout == LAYOUT.small:
                font = self.fixed
            w = FRAMESIZE.w - len(date_time)*(font.size.w+1)
            pos0 = Position( int(ceil(w/2)), 6 )
            text = font.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0,wrap=True)



    
        elif layout == LAYOUT.dual:
            date = now.strftime("%F")
            time = now.strftime("%T")
            w0 = FRAMESIZE.w - len(date)*(self.large.size.w+1)
            w1 = FRAMESIZE.w - (len(date)-2)*(self.large.size.w+1)
            pos0 = Position(int(w0/2),1)
            pos1 = Position(int(w1/2),8)
            text = self.large.render(date,fixed=True)
            ret.addMask(text,pos=pos0)
            text = self.large.render(time,fixed=True)
            ret.addMask(text,pos=pos1)
    
        else:
            date_time = now.strftime("%F %T")
            pos0 = Position(0,1)
            
            
            year_start = now.replace(month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            day_start = now.replace(hour=0,minute=0,second=0,microsecond=0)
            decade_start = now.replace(year=2020,month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            
            year_delta = now - year_start
            day_delta = now - day_start
            decade_delta = now - decade_start
            

            seconds_per_day = 24. * 60. * 60.
            seconds_per_year = 365. * seconds_per_day
            seconds_per_decade = 10. * seconds_per_year
 
            
            daydone = day_delta.total_seconds() / seconds_per_day * 100.
            yeardone = year_delta.total_seconds() / seconds_per_year * 100.
            decdone = decade_delta.total_seconds() / seconds_per_decade * 100.
            
#            detail = "20s:{:4.1f}% YEAR:{:5.1f}% DAY:{:5.1f}% ".format(decdone,yeardone,daydone)
            detail = "YEAR:{:5.1f}% COMPLETE DAY:{:5.1f}%".format(yeardone,daydone)
#            detail = "YEAR {:5.1f}% OVER".format(yeardone)           
            
            
#            day = "DAY{:3.0f}% DONE.".format(seconds_today / seconds_per_day)
#           detail = detail.replace("DAY",now.strftime("%a").upper())
#            year = "YEAR{:3.0f}% DONE.".format(50)
#            detail = detail.replace("YEAR",now.strftime("%Y"))
#            decade = "DEC:{:5.1f}%".format(0.5)
#            decade = decade.replace("DEC",now.strftime("%Y")[0:2]+"s")

            pos1 = Position( 0, 8)
#            pos1 = Position( 2+(9  +4  + 3  ) * 4, 8 )
#            pos2 = Position( ( 0   ) * 4, 8 )
#            pos3 = Position( 4+(9+10)* 4, 8 )

            text = self.large.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0)

            text = self.small.render(detail,fixed=False,space=3)
            ret.addMask(text,pos=pos1)

#            text = self.small.render(day,fixed=False,space=3)
#            ret.addMask(text,pos=pos1)
#            text = self.small.render(year,fixed=False,space=3)
#           ret.addMask(text,pos=pos2)
##            text = self.small.render(decade,fixed=False,space=3)
##            ret.addMask(text,pos=pos3)
    
    
        return ret
    

    def draw(self,**params):


        ret = []

        now = datetime.datetime.now()
        
        next = self.tick(now,**params)

        log("from\n"+str(self.mask))
        log("to\n"+str(next))

        steps = Morph2(self.mask,next)


        for i in range(len(steps)):
            step = steps[i]
            ret += [ step ]
            self.mask = step
        
        return ret

        
    flags = [
        ("l:", "layout=", "layout", LAYOUT.large, "clock layout", lambda x: LAYOUT[x] ),
    ]
    
    
