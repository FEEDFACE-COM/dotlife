
import datetime, dateutil

try:
    import zoneinfo
except ModuleNotFoundError:
    pass

from dotlife import *
from dotlife.util import *
from dotlife.math import *

from dotlife.time import Clock
from dotlife.font import Font, FONT
from dotlife.mask import Mask
from dotlife.effects import Morph, Morph2, Axis, Scan


from enum import auto


#def debug(foo): pass

class Style(Enum):
    small  = auto()
    large  = auto()
    split  = auto()
    stats  = auto()
    words  = auto()
    florid = auto()
    date   = auto() 
    date2  = auto()
    unix   = auto()
    world  = auto()
    invader= auto()




def humanDate(then):    
    ret = ""
    year,month,day,hour,minute,_,weekday,_,_ = then.timetuple()

    ret = "Ein "
    ret += humanWeekday(then)
    ret += " im "
    ret += humanMonth(then)
    return ret

def humanWeekday(then):
    ret = ""
    _,_,_,_,_,_,weekday,_,_ = then.timetuple()
    ret += {
        0: "Montag",
        1: "Dienstag",
        2: "Mittwoch",
        3: "Donnerstag",
        4: "Freitag",
        5: "Samstag",
        6: "Sonntag",
    }[weekday%7]
    return ret

def humanDay(then):
    return then.strftime("%e").strip()


def humanMonth(then):
    ret = ""
    _,month,_,_,_,_,_,_,_ = then.timetuple()
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
    x = 1 if minute >= 20 else 0
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
    elif 11 <= hour+x <= 13:
        ret += ""
    elif 14 <= hour+x <= 17:
        ret += ""
    elif 18 <= hour+x <= 23:
        ret += "Abends"
    elif 24 <= hour+x <= 24:
        ret += "Nachts"
    return ret      




class Clock():

    DefaultSize = Size(115,60)

    def __init__(self):
        self.small = Font(FONT.font3x5) 
        self.fixed = Font(FONT.fix3x5)
        self.large = Font(FONT.font5x5)
        self.full =  Font(FONT.font5x7)
        self.giant = Font(FONT.font10x14)
        self.tiny  = Font(FONT.font3x4)


    def mask(self,now,size=DefaultSize,style=Style.large):
        ret = Mask(size=size)
    
        debug("clock "+now.strftime("%F %T"))

        if style == Style.small:
            date_time = now.strftime("%F %T %Z")
            w = size.w - len(date_time)*(self.fixed.size.w+1)
            pos0 = Position( int(ceil(w/2)), floor(abs(size.h-self.fixed.size.h)/2) )
            text = self.fixed.render(date_time,fixed=True)
            ret = ret.addMask(text,pos=pos0,wrap=True)
            return ret

        elif style == Style.large:
            date = now.strftime("%F")
            time = now.strftime("%T")
            w0 = size.w - len(date)*(self.large.size.w+1)
            w1 = size.w - (len(date)-2)*(self.large.size.w+1)
            pos0 = Position(int(w0/2),1)
            pos1 = Position(int(w1/2),8)
            text = self.large.render(date,fixed=True)
            ret = ret.addMask(text,pos=pos0)
            text = self.large.render(time,fixed=True)
            ret = ret.addMask(text,pos=pos1)
            return ret

        elif style == Style.split:
            time = now.strftime("%H:%M")
            spacer = 0 #self.giant.size.w
            w = size.w - len(time)*(self.giant.size.w+1)
            pos0 = Position( 0  , floor(abs(size.h-self.giant.size.h)/2) )
            text0 = self.giant.render(time)
            ret = ret.addMask(text0,pos=pos0,wrap=True)

            wkd = humanWeekday(now).upper() + ", "
            pos1 = Position(w+spacer, 1)
            text1 = self.large.render(wkd,fixed=False)
            ret = ret.addMask(text1,pos=pos1,wrap=True)

            _,_,d,_,_,_,_,_,_ = now.timetuple()
            day = "{:d}".format(d)
            text2 = self.full.render(day,fixed=True)
            pos2 = Position(w+spacer, (size.h-1)-self.full.size.h)
            ret = ret.addMask(text2,pos=pos2,wrap=True)
            
            mon = ". " + humanMonth(now).upper()
            text3 = self.large.render(mon,fixed=False,space=1)
            pos3 = Position(pos2.x + text2.w - 0, size.h - text3.h + 1)
            ret = ret.addMask(text3,pos=pos3,wrap=True)
            return ret
    
        elif style == Style.words:
            pos0 = Position(0,4)
            txt0 = humanTime(now).upper()
            
            text0 = self.full.render(txt0,space=2,fixed=False)
            pos0 = Position( 4+int((size.w - text0.w)/2), 4)
            
            ret = ret.addMask(text0,pos=pos0)
            return ret
    
        elif style == Style.stats:
            pos0 = Position(0,2)
            pos1 = Position(0,9)
           
            start = Struct()
            start.decade = now.replace(year=(now.year-now.year%10),month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            start.year  = now.replace(month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            start.month = now.replace(day=1,hour=0,minute=0,second=0,microsecond=0)
            start.day   = now.replace(hour=0,minute=0,second=0,microsecond=0)
            start.hour  = now.replace(minute=0)
            

            m = start.month.month+1
            y = start.month.year
            if m > 12:
                m = 1
                y = start.month.year + 1
            next_month = start.month.replace(year=y,month=m)
           
            seconds = Struct() 
            seconds.decade = (start.decade.replace(year=start.decade.year+10) - start.decade).total_seconds()
            seconds.year   = (start.year.replace(year=start.year.year+1) - start.year).total_seconds()
            seconds.month  = (next_month - start.month).total_seconds()
            seconds.day    = datetime.timedelta(days=1).total_seconds()  
            seconds.hour   = datetime.timedelta(hours=1).total_seconds()
           
            fraction = Struct() 
            fraction.decade = (now - start.decade).total_seconds() / seconds.decade * 100.
            fraction.year   = (now - start.year).total_seconds() / seconds.year * 100.
            fraction.month  = (now - start.month).total_seconds() / seconds.month * 100.
            fraction.day    = (now - start.day).total_seconds() / seconds.day * 100.
            fraction.hour   = (now - start.hour).total_seconds() / seconds.hour * 100.
   
            name = Struct() 
            name.decade = "20s"
            name.year = "{:d}".format(now.year)
            name.month = humanMonth(now)
            name.wkd= humanWeekday(now)
            name.day = now.strftime("%d.")
            name.hour = now.strftime("%I")
    
    
            #str1 =  now.strftime("%F  %T")
            #str2 = "DECADE:{:3.0f}% YEAR:{:3.0f}% MON:{:3.0f}%".format(fraction.decade,fraction.year,fraction.month)

            str1 =  now.strftime(" %Y-%m-%d   %H:%M ")
            str2 = "{:3s}:{:3.0f}% '{:2s}:{:3.0f}% {:3s}:{:3.0f}% {:2s}:{:3.0f}%".format(name.decade,fraction.decade,name.year[-2:],fraction.year,name.month[0:3].upper(),fraction.month,name.wkd[0:2].upper(),fraction.day)
            str2 = "{:3s}:{:.0f}% '{:2s}:{:.0f}% {:3s}:{:.0f}% {:2s}:{:.0f}%".format(name.decade,fraction.decade,name.year[-2:],fraction.year,name.month[0:3].upper(),fraction.month,name.wkd[0:2].upper(),fraction.day)

            #str1 =  now.strftime("%Y   %m-%d   %H:%M")
            #str2 = "{:3.0f}% {:3.0f}% MON:{:3.0f}%".format(fraction.decade,fraction.year,fraction.month)


            #str1 = "{:4s}: {:3.0f}%  {:s}: {:3.0f}%".format(name.year,fraction.year,name.month.upper(),fraction.month)
            #str2 = "{:s}: {:3.0f}% {:s}: {:3.0f}%".format(name.day.upper(),fraction.day,name.hour,fraction.hour)


            #str1 = "{:s} {:s} {:9s} {:s}".format(name.wkd[0:2].upper(),name.day,name.month.upper(),name.year)
            #str2 = "{:3.0f}% {:3.0f}% {:3.0f}%".format(fraction.year,fraction.month,100.)

            text1 = self.large.render(str1,fixed=True,space=4)
            ret = ret.addMask(text1,pos=pos0)
            text2 = self.small.render(str2,fixed=True,space=1)
            ret = ret.addMask(text2,pos=pos1)
            return ret

        elif style == Style.florid:
            pos0 = Position(0,3)
            pos1 = Position(0,9)
            txt0 = humanDate(now)+","
            txt1 = humanTime(now) + (" " if len(humanTimeOfDay(now))>0 else "") + humanTimeOfDay(now) + "..."
            text0 = self.small.render(txt0.upper(),fixed=False)
            text1 = self.small.render(txt1.upper(),fixed=False)
            ret = ret.addMask(text0,pos=pos0)
            ret = ret.addMask(text1,pos=pos1)
            return ret

        elif style == Style.date2:
            pos = Position(0,0)
            txt = "{:s}, {:s}. {:s}".format(humanWeekday(now),humanDay(now),humanMonth(now))
            text = self.small.render(txt.upper())
            ret = ret.addMask(text,pos=None)
            return ret
            
            
        elif style == Style.date:
            day = self.giant.render(now.strftime("%e."))
            ret = ret.addMask(day,pos=Position(0,2))
            

            wkd = self.full.render(humanWeekday(now).upper()+",")
            x = ret.size().w - wkd.size().w
            ret = ret.addMask(wkd,pos=Position(x,0))

            mon = self.full.render(humanMonth(now).upper())#+" {:d}".format(now.year) )
            ret = ret.addMask(mon,pos=Position(30,9))
            return ret

        elif style == Style.unix:
            seconds = "{:08x}".format( int(now.timestamp()) - (int(now.timestamp()) % 0x400 ))
            unix = self.giant.render('0x'+seconds.upper())
            ret = ret.addMask(unix)
            return ret

        elif style == Style.world:
            localities = [ 'America/Los_Angeles', 'Europe/Berlin', 'Europe/London', 'UTC', 'Asia/Hong_Kong' ]
            infos = {}
            for locality in localities:
                try:
                    zone = zoneinfo.ZoneInfo(locality)
                except NameError: # name 'zoneinfo' is not defined
                    zone = datetime.timezone.utc
                time = datetime.datetime.now( zone )
                info = Struct()
                info.name = time.strftime("%Z")
                info.time = time.strftime("%H:%M")
                info.offset = time.strftime("%z")
                infos[locality] = info
                debug("{:20s} {:6s} {:6s} {:6s}".format(locality,info.name,info.time,info.offset))

            off = 0
            for locality in localities:
                time = self.small.render(infos[locality].time,fixed=True)
                name = self.small.render(infos[locality].name)
                offset = self.tiny.render(infos[locality].offset,fixed=True)
                x = int( (time.w - name.w)/2)
                ret = ret.addMask(name,pos=Position(off + x,0))
                ret = ret.addMask(time,pos=Position(off + 0,6))
                ret = ret.addMask(offset,pos=Position(off + 0,12))
                off += time.w + 4
            return ret
            
            


        elif style == Style.invader:
            hour = int(now.hour)
            idx = 0
            if int(now.minute) > 30:
              idx = 1
            
            if 1 <= hour <= 4:
                vader = invader.INVADER.one.Mask(idx).double()
                msk = Mask(size=Size((4+vader.w)*hour, vader.h))
                for c in range(hour):
                    pos = Position(c*(4+vader.w),0)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)
            elif 5 <= hour <= 8:
                vader = invader.INVADER.one.Mask(idx)
                msk = Mask(size=Size((2+vader.w)*hour, vader.h))
                for c in range(hour):
                    pos = Position(c*(2+vader.w),0)
                    msk.addMask(vader,pos=pos)
                ret.addMask(msk)
                
            elif 9 <= hour <= 12:
                vader1 = invader.INVADER.one.Mask(idx)
                vader2 = invader.INVADER.two.Mask(idx)
                msk1 = Mask(size=Size((2+vader1.w)*ceil(hour/2), 2 * (vader1.h)))
                msk2 = Mask(size=Size((2+vader1.w)*ceil(hour/2), 2 * (vader2.h)))
                for c in range(hour):
                    pos1 = Position(int(c/2)*(2+vader1.w),0)
                    pos2 = Position(int(c/2)*(2+vader2.w),8)
                    msk1.addMask(vader1,pos=pos1)
                    msk2.addMask(vader2,pos=pos2)
                ret.addMask(msk1)
                ret.addMask(msk2)
                
            return ret
                
        return Mask(size=size)
    






