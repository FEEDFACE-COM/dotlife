
import datetime 

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



class Style(Enum):

    class small():
        def fun(self,now,size):
            ret = Mask(size=size)
            date_time = now.strftime("%F %T %Z")
            w = size.w - len(date_time)*(self.fixed.size.w+1)
            pos0 = Position( int(ceil(w/2)), floor(abs(size.h-self.fixed.size.h)/2) )
            text = self.fixed.render(date_time,fixed=True)
            ret = ret.addMask(text,pos=pos0,wrap=True)
            return ret


    class large():
        def fun(self,now,size):
            ret = Mask(size=size)
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

    class split():
        def fun(self,now,size):
            ret = Mask(size=size)
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

    class words():
        def fun(self,now,size):
            ret = Mask(size=size)
            pos0 = Position(0,4)
            txt0 = humanTime(now).upper()

            text0 = self.full.render(txt0,space=2,fixed=False)
            pos0 = Position( 4+int((size.w - text0.w)/2), 4)

            ret = ret.addMask(text0,pos=pos0)
            return ret

    class stats():
        def fun(self, now, size):
            ret = Mask(size=size)
            decade,year,month,day,hour = Struct(), Struct(), Struct(), Struct(), Struct()

            decade.start = now.replace(year=(now.year-now.year%10),month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            year.start   = now.replace(month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
            month.start  = now.replace(day=1,hour=0,minute=0,second=0,microsecond=0)
            day.start    = now.replace(hour=0,minute=0,second=0,microsecond=0)
            hour.start   = now.replace(minute=0)
            

            m = month.start.month+1
            y = month.start.year
            if m > 12:
                m = 1
                y = month.start.year + 1
            next_month = month.start.replace(year=y,month=m)
           
           
            decade.seconds = (decade.start.replace(year=decade.start.year+10) - decade.start).total_seconds()
            year.seconds   = (year.start.replace(year=year.start.year+1) - year.start).total_seconds()
            month.seconds  = (next_month - month.start).total_seconds()
            day.seconds    = datetime.timedelta(days=1).total_seconds()  
            hour.seconds   = datetime.timedelta(hours=1).total_seconds()
           
            decade.fraction = (now - decade.start).total_seconds() / decade.seconds * 100.
            year.fraction   = (now - year.start).total_seconds() / year.seconds * 100.
            month.fraction  = (now - month.start).total_seconds() / month.seconds * 100.
            day.fraction    = (now - day.start).total_seconds() / day.seconds * 100.
            hour.fraction   = (now - hour.start).total_seconds() / hour.seconds * 100.
   
            decade.name = "    "
            year.name = "'"+"{:d}".format(now.year)[-2:]
#            year.name = "YEAR"
            month.name = humanMonth(now).upper()[0:]
            day.name = humanWeekday(now).upper()[0:]
#            day.name = now.strftime("%d.")
            hour.name = now.strftime("%I")
    
            decade.name = "DECADE"
            year.name = "YEAR"
            #year.name = now.strftime("%Y")
            month.name = "MONTH"
            #month.name = humanMonth(now).upper()[0:3]
            day.name = "DAY"
            #day.name = humanWeekday(now).upper()[0:2] + " " + now.strftime("%e")
            hour.name = "HOUR"
    
    
            str0 =  now.strftime("%Y-%m-%d")
            str1 =  now.strftime("%H:%M%z")

            pos0 = Position(0,0)

            text0 = self.tiny.render(str0,fixed=True,space=4)
            ret = ret.addMask(text0,pos=Position(0,0))
            text1 = self.tiny.render(str1,fixed=True,space=4)
            ret = ret.addMask(text1,pos=Position(76,0))

#            for s in ( decade, year, month, day ):
#              log("{:16s}  {:.0f}%".format(s.name,s.fraction))

            o = 1
            for s in ( decade, year, month, day ):
                name = self.small.render(s.name,fixed=True)
                frac = self.large.render("{:5.1f}%".format(s.fraction),fixed=False,space=4)
                x = int( (frac.w-name.w)) -1
                if s == decade:
                    frac = self.large.render("{:4.1f}%".format(s.fraction),fixed=False,space=4)
                    x = int( (frac.w-name.w)) -0
                ret.addMask(frac, pos=Position(o,11))
                ret.addMask(name, pos=Position(o+x, 5))
                o += frac.w + 2

            return ret

    class florid():
        def fun(self, now, size):
            ret = Mask(size=size)
            pos0 = Position(0,3)
            pos1 = Position(0,9)
            txt0 = humanDate(now)+","
            txt1 = humanTime(now) + (" " if len(humanTimeOfDay(now))>0 else "") + humanTimeOfDay(now) + "..."
            text0 = self.small.render(txt0.upper(),fixed=False)
            text1 = self.small.render(txt1.upper(),fixed=False)
            ret = ret.addMask(text0,pos=pos0)
            ret = ret.addMask(text1,pos=pos1)
            return ret

    class date2():
        def fun(self, now, size):
            ret = Mask(size=size)
            pos = Position(0,0)
            txt = "{:s}, {:s}. {:s}".format(humanWeekday(now),humanDay(now),humanMonth(now))
            text = self.small.render(txt.upper())
            ret = ret.addMask(text,pos=None)
            return ret
            
    class date():
        def fun(self, now, size):
            ret = Mask(size=size)
            day = self.giant.render(now.strftime("%e."))
            ret = ret.addMask(day,pos=Position(0,2))
            

            wkd = self.full.render(humanWeekday(now).upper()+",")
            x = ret.size().w - wkd.size().w
            ret = ret.addMask(wkd,pos=Position(x,0))

            mon = self.full.render(humanMonth(now).upper())#+" {:d}".format(now.year) )
            ret = ret.addMask(mon,pos=Position(30,9))
            return ret

    class unix():
        def fun(self, now, size):
            ret = Mask(size=size)
            seconds = "{:08x}".format( int(now.timestamp()) - (int(now.timestamp()) % 0x400 ))
            unix = self.full.render('0x'+seconds.upper())
            ret = ret.addMask(unix,pos=Position(28,8))
            #ret = ret.addMask( self.tiny.render(now.strftime("%Y-%m-%d %H:%M%z")), pos=Position(16,0))
            ret = ret.addMask( self.small.render(now.strftime("%Y-%m-%d %H:%M%z")), pos=Position(16,0))
#            ret = ret.addMask( self.tiny.render(now.strftime("%H:%M")),pos=Position(ret.w-18,0))  
#            ret = ret.addMask( self.tiny.render(now.strftime("%m-%d")),pos=Position(0,0)) 
            return ret

    class world():
        def fun(self, now, size):
            ret = Mask(size=size)
            localities = [ 'UTC', 'Europe/London', 'Europe/Berlin', 'Asia/Hong_Kong' , 'Australia/Melbourne' ]
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
            
            

    class invader():
        def fun(self, now, size):
            ret = Mask(size=size)
            hour = int(now.hour)
            if hour > 12:
                hour -= 12
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
                msk = Mask(size=Size((2+vader1.w)*ceil(hour/2), 2 * (vader1.h)))
                for c in range(hour):
                    if c % 2 == 0:
                        pos = Position(int(c/2)*(2+vader1.w),0)
                        msk.addMask(vader1,pos=pos)
                    else:
                        pos = Position(int(c/2)*(2+vader1.w),8)
                        msk.addMask(vader2,pos=pos)
                ret.addMask(msk)
                
            return ret
                


## clock #################################################################################

class Clock():

    DefaultSize = Size(115,60)

    def __init__(self):
        self.small = Font(FONT.font3x5)
        self.fixed = Font(FONT.fix3x5)
        self.large = Font(FONT.font5x5)
        self.full =  Font(FONT.font5x7)
        self.giant = Font(FONT.font10x14)
        self.tiny  = Font(FONT.font3x4)


    def mask(self,now,size=DefaultSize,style=Style.small):
        debug("clock "+now.strftime("%F %T"))
        ret = style.value.fun(self,now,size)
        return ret


## helper functions ######################################################################

def humanDate(then):
    ret = ""
    year, month, day, hour, minute, _, weekday, _, _ = then.timetuple()

    ret = "Ein "
    ret += humanWeekday(then)
    ret += " im "
    ret += humanMonth(then)
    return ret


def humanWeekday(then):
    ret = ""
    _, _, _, _, _, _, weekday, _, _ = then.timetuple()
    ret += {
        0: "Montag",
        1: "Dienstag",
        2: "Mittwoch",
        3: "Donnerstag",
        4: "Freitag",
        5: "Samstag",
        6: "Sonntag",
    }[weekday % 7]
    return ret


def humanDay(then):
    return then.strftime("%e").strip()


def humanMonth(then):
    ret = ""
    _, month, _, _, _, _, _, _, _ = then.timetuple()
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
    }[month % 12]
    return ret


def humanTime(then):
    ret = ""
    year, month, day, hour, minute, _, weekday, _, _ = then.timetuple()
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
    }[(hour + x) % 12]
    if minute <= 1 or minute >= 59:
        if (hour + x) % 12 == 1:  # FIXUP:  Eins<>Ein
            ret = ret[:-1]
        ret += " Uhr"

    return ret


def humanTimeOfDay(then):
    ret = ""
    _, _, _, hour, minute, _, _, _, _ = then.timetuple()
    x = 1 if minute >= 29 else 0
    if 0 <= hour + x <= 4:
        ret += "Nachts"
    elif 5 <= hour + x <= 10:
        ret += "Morgens"
    elif 11 <= hour + x <= 13:
        ret += ""
    elif 14 <= hour + x <= 17:
        ret += ""
    elif 18 <= hour + x <= 23:
        ret += "Abends"
    elif 24 <= hour + x <= 24:
        ret += "Nachts"
    return ret



