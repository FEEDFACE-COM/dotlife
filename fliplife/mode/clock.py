
import random, datetime

import dotlife
from dotlife import *
from dotlife.util import *
from dotlife.math import *


import fliplife
from fliplife.mode import Mode
from fliplife import Mask, FRAMESIZE
from fliplife.fluepdot import Fluepdot

from dotlife.time import Clock
from dotlife.font import Font, FONT
from dotlife.effects import Morph, Morph2, Axis, Scan

from dotlife import invader

from enum import auto

class Style(Enum):
    large  = auto()
    small  = auto()
    double = auto()  
    detail = auto()
    lyric  = auto() 
    words  = auto()


        
        

class Clock(Mode):
    
    Style = Style
    
    
    def start(self,stamp,**params):
        self.fluepdot.rendering.setMode(Fluepdot.Mode.Full)
        
        self.small = Font(FONT.font3x5) 
        self.fixed = Font(FONT.fix3x5)
        self.large = Font(FONT.font5x5)
        self.full =  Font(FONT.font5x7)
        

        
        self.now = datetime.datetime.now()
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp)
            self.start = datetime.datetime.now()
        
        
        info("start clock: {:s}".format(self.now.strftime("%F %T")))

        self.mask = self.render(**params)
        self.next = self.mask

        self.fluepdot.rendering.setMode(Fluepdot.Mode.Diff)

        self.coocoo = None
        self.hour = self.now.hour
        return True
    
    def coocooc(self,**params):
        info("FIRED FIRED")
    
    def step(self,style,stamp,**params):
        if stamp != "":
            self.now = datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now() - self.start )
        else:
            self.now = datetime.datetime.now()

        for p in params:
            debug(str(p))
        self.next = self.render(style,**params)


    def draw(self,style,stamp,**params):

        if self.coocoo and self.coocoo.active():
            idx = self.coocoo.count % 2
            return Mask().addMask(invader.INVADER.one.Mask(idx))

    
        hour = datetime.datetime.now().hour
        if stamp != "":
            hour = (datetime.datetime.fromisoformat(stamp) + (datetime.datetime.now() - self.start )).hour
        else:
            hour = datetime.datetime.now().hour
            
        if hour != self.hour:
            self.step(style,stamp,**params)
            self.coocoo = time.Clock.Timer(1500.,hour%12,lambda: self.coocooc(**params))
            debug("coocooc {:}".format(self.coocoo))

        self.hour = hour


        if self.next != self.mask:
        
        
            if style in [Style.small,Style.large,Style.double]:
                m = Morph2(self.mask,self.next,steps=1)
                debug("from\n"+str(self.mask))
                debug("to\n"+str(self.next))
                self.mask = m[1]
                
                
            else:
                debug("to\n"+str(self.next))
                self.mask = self.next
                

        return self.mask
        

        
    flags = [
        Mode.FLAG("style",Style.large),
#        ("y:", "style=", "style", Style.large, "clock style", lambda x: Style[x] ),
        ("", "stamp=", "stamp", "", "timestamp", None ),
    ]
    
    



    def render(self,style,**params):
        now = self.now
        ret = Mask()
    
    
        
        debug("render "+now.strftime("%F %T"))
        if style in [ Style.small, Style.large]:
            date_time = now.strftime("%F %T")
            font = self.large
            if style == Style.small:
                font = self.fixed
            w = FRAMESIZE.w - len(date_time)*(font.size.w+1)
            pos0 = Position( int(ceil(w/2)), 6 )
            text = font.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0,wrap=True)
    
    
    
    
        elif style == Style.double:
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
    
    
        elif style == Style.lyric:
            pos0 = Position(0,1)
            pos1 = Position(0,10)
            txt = humanreadable( now ).split("\n")
                
            txt0 = txt[0]
            txt1 = txt[1]
            text0 = self.small.render(txt0.upper(),fixed=False)
            text1 = self.small.render(txt1.upper(),fixed=False)
            ret.addMask(text0,pos=pos0)
            ret.addMask(text1,pos=pos1)
            
    
        elif style == Style.words:
            pos0 = Position(0,4)
            txt0 = humanshort(now).upper()
            
            text0 = self.full.render(txt0,space=2,fixed=False)
            pos0 = Position( 4+int((FRAMESIZE.w - text0.w)/2), 4)
            
            ret.addMask(text0,pos=pos0)
            
    
        elif style == Style.detail:
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
