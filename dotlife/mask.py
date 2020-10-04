
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.util import *




class Mask:

    DefaultSize = (8,8)


    MAP = {
        ((False,False),
         (False,False)): " ",#"⨯",
        ((False,False),
         (False,True )): "▗",
        ((False,False),
         (True, True )): "▄",
        ((False,False),
         (True, False)): "▖",
        ((False,True ),
         (False,False)): "▝",
        ((False,True ),
         (False,True )): "▐",
        ((False,True ),
         (True, False)): "▞",
        ((False,True ),
         (True, True )): "▟",
        ((True, False),
         (False,False)): "▘",
        ((True, False),
         (False,True )): "▚",
        ((True, False),
         (True, False)): "▌",
        ((True, False),
         (True, True )): "▙",
        ((True, True ),
         (False,False)): "▀",
        ((True, True ),
         (False,True )): "▜",
        ((True, True ),
         (True, False)): "▛",
        ((True, True ),
         (True, True )): "█",
        ((None, None ),
         (None, None )): "#",
    }


    def __str__(self):
        if self.h > 8 or self.w > 32:
            return self.str1()
        return self.str0()
    
    
    def str0(self):
        ret = ""
        for y in range(self.h):
            for x in range(self.w):
                p = self.pixel[x][y]
                if p:
                    ret += "[]"
                else:
                    ret += " ·"
            ret += "\n"
        return ret[:-1]
    
    def str1(self):
        ret = ""
        for y in range(0,self.h,2):
            for x in range(0,self.w,2):
                a,b,c,d = False, False, False, False
                a = self.pixel[x  ][y  ]
                if x+1 < self.w: 
                    b = self.pixel[x+1][y  ]
                if y+1 < self.h:
                    c = self.pixel[x  ][y+1]
                if x+1 < self.w and y+1 < self.h: 
                    d = self.pixel[x+1][y+1]
                ret += Mask.MAP[((a,b),(c,d))] 
            ret += "{:1d}\n".format(y%10)

#        for x in range(0,self.w,2):
#            ret += "{:1d}".format(x%10)
#        ret += "\n"

        for x in range(0,self.w,2):
            if x % 10 == 0:
                ret += "{:d}".format( (int((x%100)/10)) )
            else:
                ret += " "
        ret += "\n"

        return ret[:-1]
    
    
    def __init__(self,mask=None,val=False,size=DefaultSize):
        if mask:
            self.w,self.h = mask.w,mask.h
            self.pixel = [ [ mask[x,y] for y in range(self.h) ] for x in range(self.w) ]
        else:
            self.w, self.h = size
            if self.w <= 0 or self.h <= 0:
                raise dotlife.Error("invalid mask dimensions {}x{}".format(self.w,self.h)) 
            self.pixel = [ [ val for y in range(self.h) ] for x in range(self.w) ]
        
    
    def __getitem__(self,pos):
        posx,posy = pos
        x  = (self.w + posx) % self.w
        y =  (self.h + posy) % self.h
        return self.pixel[x][y]

    def __setitem__(self,pos,val):
        posx,posy = pos
        x  = (self.w + posx) % self.w
        y =  (self.h + posy) % self.h
        self.pixel[x][y] = val

    def inverse(self):
        ret = Mask(size=(self.w,self.h))
        for y in range(self.h):
            for x in range(self.w):
                ret.pixel[x][y] = not self.pixel[x][y]
        return ret


    def inv(self):
        for y in range(self.h):
            for x in range(self.w):
                self.pixel[x][y] = not self.pixel[x][y]
        return self

    def flip(self,axis):
        w,h = self.w,self.h
        tmp = Mask(mask=self)
        
        for y in range(self.h):
            for x in range(self.w):
                if axis == Axis.Horizontal:
                    self.pixel[x][y] = tmp[x,h-1-y]
                elif axis == Axis.Vertical:
                    self.pixel[x][y] = tmp[w-1-x,y]

        return self
                

    def add(self,val):
        if type(val) == type( Mask() ):
            return self.addMask(val)
        raise Error("operation {} + {} -> {} not implemented".format(type(self).__name__,type(val).__name__,type(self).__name__) )

    def addMask(self,val):
        for y in range(self.h):
            for x in range(self.w):
                if 0 <= x < val.w and 0 <= y < val.h:
                    self.pixel[x][y] = val[x,y]


    def mask(self,mask,pos=Position(0,0),wrap=False):
        for y in range(mask.h):
            if not wrap and not 0 <= y+pos.y < self.h:
                continue
            for x in range(mask.w):
                if not wrap and not 0 <= x+pos.x < self.w:
                    continue
                if mask[x,y]:
                    self[x+pos.x,y+pos.y] = mask[x,y]
        
        
    def Checkers(size=(4,4)):
        ret = Mask(size=size)
        for y in range(ret.h):
            for x in range(ret.w):
                ret[x,y] = (x%2 != y%2)
        return ret

    
    def Load(pattern):
        w,h = 0,0
        lines = pattern.split("\n")
        # find dimensions        
        for row in lines:
            if row == "":
                continue
            h += 1
            l = 0
            for c in range( len(row) ):
                if c%2 != 0:
                    continue
                l += 1
            if l > w:
                w = l
                
        if w <= 0 or h <= 0:
            raise Error("invalid mask pattern: {}x{}\n{}".format(w,h,lines))
        
        ret = Mask(size=(w,h))

        # read and fill
        x,y = 0,0
        for row in lines:
            if row == "":
                continue
            x = 0
            for c in range( len(row) ):
                if c%2 != 0:
                    continue
                if row[c] != " ":
                    ret[x,y] = True
                x += 1
            y += 1
        
        return ret
    
    
