
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.util import *




class Mask:

    DefaultSize = (8,8)

    def __str__(self):
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
    
    
    
    def __init__(self,val=False,size=DefaultSize):
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
        

    def add(self,val):
        if type(val) == type( Mask() ):
            return self.addMask(val)
        raise Error("operation {} + {} -> {} not implemented".format(type(self).__name__,type(val).__name__,type(self).__name__) )

    def addMask(self,val):
        for y in range(self.h):
            for x in range(self.w):
                if 0 <= x < val.w and 0 <= y < val.h:
                    self.pixel[x][y] = val[x,y]


    def mask(self,mask,pos=(0,0),wrap=False):
        dx,dy = pos
        for y in range(mask.h):
            if not wrap and not 0 <= y+dy < self.h:
                continue
            for x in range(mask.w):
                if not wrap and not 0 <= x+dx < self.w:
                    continue
                if mask[x,y]:
                    self[x+dx,y+dy] = mask[x,y]
        
        
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
    
    
