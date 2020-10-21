
import datetime

from dotlife import *
from dotlife.util import *
from dotlife.math import *

from dotlife.time import Clock
from dotlife.font import Font, FONT
from dotlife.mask import Mask
from dotlife.effects import Morph, Morph2, Axis, Scan


from enum import auto

class Style(Enum):
    large  = auto()
    small  = auto()
    double = auto()  
    stats  = auto()
    lyric  = auto() 
    words  = auto()
    mini   = auto()


class Clock():

    DefaultSize = Size(115,60)

    def __init__(self):
        self.small = Font(FONT.font3x5) 
        self.fixed = Font(FONT.fix3x5)
        self.large = Font(FONT.font5x5)
        self.full =  Font(FONT.font5x7)


    def mask(self,now,size=DefaultSize,style=Style.large):
        ret = Mask(size=size)
    
    
        debug("clock "+now.strftime("%F %T"))
        if style in [ Style.small, Style.large]:
            date_time = now.strftime("%F %T")
            font = self.large
            if style == Style.small:
                date_time = now.strftime("%F %T")
                font = self.fixed
            w = size.w - len(date_time)*(font.size.w+1)
            pos0 = Position( int(ceil(w/2)), floor(abs(size.h-font.size.h)/2) )
            text = font.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0,wrap=True)
    
    
    
    
        elif style == Style.double:
            date = now.strftime("%F")
            time = now.strftime("%T")
            w0 = size.w - len(date)*(self.large.size.w+1)
            w1 = size.w - (len(date)-2)*(self.large.size.w+1)
            pos0 = Position(int(w0/2),1)
            pos1 = Position(int(w1/2),8)
            text = self.large.render(date,fixed=True)
            ret.addMask(text,pos=pos0)
            text = self.large.render(time,fixed=True)
            ret.addMask(text,pos=pos1)
    
    
        elif style == Style.lyric:
            pos0 = Position(0,1)
            pos1 = Position(0,10)
            txt0 = humanDate(now)+","
            txt1 = humanTime(now)+ " " + humanTimeOfDay(now)+"..."
            text0 = self.small.render(txt0.upper(),fixed=False)
            text1 = self.small.render(txt1.upper(),fixed=False)
            ret.addMask(text0,pos=pos0)
            ret.addMask(text1,pos=pos1)
            
    
        elif style == Style.words:
            pos0 = Position(0,4)
            txt0 = humanTime(now).upper()
            
            text0 = self.full.render(txt0,space=2,fixed=False)
            pos0 = Position( 4+int((FRAMESIZE.w - text0.w)/2), 4)
            
            ret.addMask(text0,pos=pos0)
            
    
        elif style == Style.stats:
            date_time = now.strftime("%F %T")
            pos0 = Position(0,1)
            pos1 = Position(0,10)
            
            start_decade = now.replace(year=(now.year-now.year%10),month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            start_year   = now.replace(                            month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            start_month  = now.replace(                                    day=1,hour=0,minute=0,second=0,microsecond=0)
            start_day    = now.replace(                                          hour=0,minute=0,second=0,microsecond=0)

            m = start_month.month+1
            y = start_month.year
            if m > 12:
                m = 1
                y = start_month.year + 1
            next_month = start_month.replace(year=y,month=m)
            
            seconds_decade = (start_decade.replace(year=start_decade.year+10) - start_decade).total_seconds()
            seconds_year   = (start_year.replace(year=start_year.year+1) - start_year).total_seconds()
            seconds_month  = (next_month - start_month).total_seconds()
            seconds_day    = datetime.timedelta(days=1).total_seconds()  
            
            fraction_decade = (now - start_decade).total_seconds() / seconds_decade * 100.
            fraction_year   = (now - start_year).total_seconds() / seconds_year * 100.
            fraction_month  = (now - start_month).total_seconds() / seconds_month * 100.
            fraction_day    = (now - start_day).total_seconds() / seconds_day * 100.
    
            detail = "DECADE:{:3.0f}% YEAR:{:3.0f}% MON:{:3.0f}%".format(fraction_decade,fraction_year,fraction_month)
    
            text = self.large.render(date_time,fixed=True)
            ret.addMask(text,pos=pos0)
            text = self.small.render(detail,fixed=False,space=3)
            ret.addMask(text,pos=pos1)
    
    
        elif style == Style.mini:
            _,_,_,hour,minute,_,_,_,_ = now.timetuple()
            h0 = int(hour / 10)
            h1 = hour % 10
            m0 = int(minute/10)
            m1 = minute%10
    
            H0 = Mask.Load( Clock.font[ h0%10 ] )
            H1 = Mask.Load( Clock.font[ h1%10 ] )
            M0 = Mask.Load( Clock.font[ m0%10 ] )
            M1 = Mask.Load( Clock.font[ m1%10 ] )

            ret.addMask(H0,Position(0,0))
            ret.addMask(H1,Position(4,0))
            ret.addMask(M0,Position(0,4))
            ret.addMask(M1,Position(4,4))
    
        return ret


    def humanDate(then):    
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


    def humanTime(then):
        ret = ""
        year,month,day,hour,minute,_,weekday,_,_ = then.timetuple()
        if 0 <= minute <= 1:
            ret += ""
        elif 2 <= minute <= 9:
            ret += "kurz nach "
        elif 10 <= minute <= 19:
            ret += "viertel nach "
        elif 20 <= minute <= 28:
            ret += "kurz vor halb "
        elif 29 <= minute <= 31:
            ret += "halb "
        elif 32 <= minute <= 39:
            ret += "kurz nach halb "
        elif 40 <= minute <= 49:
            ret += "viertel vor "
        elif 50 <= minute <= 58:
            ret += "kurz vor "
        elif 59 <= minute <= 60:
            ret += ""
        x = 1 if minute >= 29 else 0
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
        if minute <= 1 or minute >= 59:
            if (hour+x)%12 == 1: #FIXUP:  Eins<>Ein
                ret = ret[:-1]
            ret += " Uhr"
        return ret


    def humanTimeOfDay(then):
        ret = ""
        _,_,_,hour,minute,_,_,_,_ = then.timetuple()
        x = 1 if minute >= 29 else 0
        if 0 <= hour+x <= 4:
            ret += "Nachts"
        elif  5 <= hour+x <= 10:
            ret += "Morgens"
        elif 10 <= hour+x <= 18:
            ret += ""
        elif 19 <= hour+x <= 23:
            ret += "Abends"
        elif 24 <= hour+x <= 24:
            ret += "Nachts"
        return ret      


    font = [ """
[][][][]
[]    []
[]    []
[][][][]
""","""
    []  
  [][]  
    []  
    []  
""","""
[][]    
    [][]
  []    
[][][][]
""","""
[][][][]
    [][]
      []
[][][][]
""","""
[]    []
[]    []
[][][][]
      []
""","""
[][][][]
[]     
    [][]
[][]  
""","""
[]      
[][][][]
[]    []
[][][][]
""","""
[][][][]
      []
    []  
    []  
""","""
  [][]
[][][][]
[]    []
[][][][]
""","""
[][][][]
[]    []
[][][][]
      []
"""]

