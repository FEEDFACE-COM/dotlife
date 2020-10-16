
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

class Layout(Enum):
    large  = auto()
    small  = auto()
    double = auto()  
    detail = auto()
    lyric  = auto() 
    words  = auto()



        
        

class Clock(Mode):
    
    
    
    def start(self,stamp,**params):
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        
        self.small = Font(FONT.font3x5) 
        self.fixed = Font(FONT.fix3x5)
        self.large = Font(FONT.font5x5)
        self.full = Font(FONT.font5x7)
        

        
        self.now = datetime.datetime.now()
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp)
        
        
        info("start clock: {:s}".format(self.now.strftime("%F %T")))

        self.mask = self.render(**params)
        self.next = self.mask

        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)

        return True
    
    
    def step(self,stamp,**params):
        log("tick tick")
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp)
        else:
            self.now = datetime.datetime.now()

        self.next = self.render(**params)


    def draw(self,**params):


        if self.next != self.mask:
            m = Morph2(self.mask,self.next,steps=1)

            log("from\n"+str(self.mask))
            log("to\n"+str(self.next))
            
            self.mask = m[1]

        return self.mask
        

        
    flags = [
        ("l:", "layout=", "layout", Layout.large, "clock layout", lambda x: Layout[x] ),
        ("", "stamp=", "stamp", "", "timestamp", None ),
    ]
    
    



    def render(self,layout,**params):
        now = self.now
        ret = Mask()
    
    
        
        log("render "+now.strftime("%F %T"))
        if layout in [ Layout.small, Layout.large]:
            date_time = now.strftime("%F %T")
            font = self.large
            if layout == Layout.small:
                font = self.fixed
            w = FRAMESIZE.w - len(date_time)*(font.size.w+1)
            pos0 = Position( int(ceil(w/2)), 6 )
            text = font.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0,wrap=True)
    
    
    
    
        elif layout == Layout.double:
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
    
    
        elif layout == Layout.lyric:
            pos0 = Position(0,1)
            pos1 = Position(0,10)
            txt = humanreadable( now ).split("\n")
                
            txt0 = txt[0]
            txt1 = txt[1]
            text0 = self.small.render(txt0.upper(),fixed=False)
            text1 = self.small.render(txt1.upper(),fixed=False)
            ret.addMask(text0,pos=pos0)
            ret.addMask(text1,pos=pos1)
            
    
        elif layout == Layout.words:
            pos0 = Position(0,4)
            txt0 = humanshort(now).upper()
            
            text0 = self.full.render(txt0,space=2,fixed=False)
            pos0 = Position( 4+int((FRAMESIZE.w - text0.w)/2), 4)
            
            ret.addMask(text0,pos=pos0)
            
    
        elif layout == Layout.detail:
            date_time = now.strftime("%F %T")
            pos0 = Position(0,1)
            pos1 = Position(0,10)
            
            start_decade = now.replace(year=(now.year-now.year%10),month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            start_year   = now.replace(                            month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            start_day    = now.replace(                                          hour=0,minute=0,second=0,microsecond=0)
            
            seconds_decade = (start_decade.replace(year=start_decade.year+10) - start_decade).total_seconds()
            seconds_year   = (start_year.replace(year=start_year.year+1) - start_year).total_seconds()
            seconds_day    = datetime.timedelta(days=1).total_seconds()             
            
            fraction_decade = (now - start_decade).total_seconds() / seconds_decade * 100.
            fraction_year   = (now - start_year).total_seconds() / seconds_year * 100.
            fraction_day    = (now - start_day).total_seconds() / seconds_day * 100.
    
            detail = "DECADE:{:3.0f}% YEAR:{:3.0f}% DAY:{:3.0f}%".format(fraction_decade,fraction_year,fraction_day)
    
            text = self.large.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0)
            text = self.small.render(detail,fixed=False,space=3)
            ret.addMask(text,pos=pos1)
    
    
        return ret





def humanreadable(then):
    return humandate(then) + ", \n" + humantime(then) + "..."

def humandate(then):
    ret = ""
    year,month,day,hour,minute,_,weekday,_,_ = then.timetuple()

    ret = "Ein "
    ret += {
        0: "Montag",
        1: "Dienstag",
        2: "Mittwoch",
        3: "Donnerstag",
        4: "Freitag",
        5: "Samstag",
        6: "Sonntag",
    }[weekday%7]

    ret += " im "
    ret += {
         1: "Januar",
         2: "Februar",
         3: "März",
         4: "April",
         5: "Mai",
         6: "Juni",
         7: "Juli",
         8: "August",
         9: "September",
        10: "Oktober",
        11: "November",
         0: "Dezember",
    }[month%12]
    
    return ret

def humantime(then):
    ret = ""
    year,month,day,hour,minute,_,weekday,_,_ = then.timetuple()

    x = 0
    if minute < 2:
        ret += ""
    elif minute < 10:
        ret += "kurz nach "
    elif minute < 20:
        ret += "viertel nach "
    elif minute < 29:
        ret += "kurz vor halb "
        x = 1
    elif minute < 32:
        ret += "halb "
        x = 1
    elif minute < 40:
        ret += "kurz nach halb "
        x = 1
    elif minute < 50:
        ret += "viertel vor "
        x = 1
    elif minute < 59:
        ret += "kurz vor "
        x = 1
    else:
        ret = ""
        x = 1

    ret += {
        1: "Eins",
        2: "Zwei",
        3: "Drei",
        4: "Vier",
        5: "Fünf",
        6: "Sechs",
        7: "Sieben",
        8: "Acht",
        9: "Neun",
       10: "Zehn",
       11: "Elf",
        0: "Zwölf",
    }[(hour+x)%12]
    if minute < 2 or minute > 58:
        if (hour+x)%12 == 1: #FIXUP:  Eins<>Ein
            ret = ret[:-1]
        ret += " Uhr"

    if hour+x >= 22:
        ret += " Nachts"
    elif hour+x >= 19:
        ret += " Abends"
    elif hour+x >= 11:
        ret += ""
    elif hour+x >= 6:
        ret += " Morgens"
    else:
        ret += " Nachts"

    return ret

def humanshort(then):
    ret = ""
    year,month,day,hour,minute,_,weekday,_,_ = then.timetuple()

    x = 0
    if minute < 2:
        ret += ""
    elif minute < 10:
        ret += "kurz nach "
    elif minute < 20:
        ret += "viertel nach "
    elif minute < 29:
        ret += "kurz vor halb "
        x = 1
    elif minute < 32:
        ret += "halb "
        x = 1
    elif minute < 40:
        ret += "kurz nach halb "
        x = 1
    elif minute < 50:
        ret += "viertel vor "
        x = 1
    elif minute < 59:
        ret += "kurz vor "
        x = 1
    else:
        ret = ""
        x = 1

    ret += {
        1: "Eins",
        2: "Zwei",
        3: "Drei",
        4: "Vier",
        5: "Fünf",
        6: "Sechs",
        7: "Sieben",
        8: "Acht",
        9: "Neun",
       10: "Zehn",
       11: "Elf",
        0: "Zwölf",
    }[(hour+x)%12]
    if minute < 2 or minute > 58:
        if (hour+x)%12 == 1: #FIXUP:  Eins<>Ein
            ret = ret[:-1]
        ret += " Uhr"
        
    return ret
