
from dotlife import *
from dotlife.util import *



class Buffer:

    DefaultSize = Size(8,8)
    
    def __str__(self):
        ret = ""
        for y in range(self.h):
            for x in range(self.w):
                p = self.pixel[x][y]
                if p < 0x00:
                    ret += "¿?"
                elif p == 0x00:
                    ret += "  "
                elif p <= 0x01:
                    ret += " ."
                elif p <= 0x02:
                    ret += " ."
                elif p <= 0x10:
                    ret += " ▫︎"
                elif p <= 0x20:
                    ret += " □"
                elif p <= 0x40:
                    ret += " ◻︎"
                elif p <= 0x80:
                    ret += " ☐"
                elif p < 0xff:
                    ret += " ◼︎"
                else:
                    ret += "?¿"
            ret += "\n"
        return ret[:-1]


    def num(self):
        ret = ""
        for y in range(self.h):
            for x in range(self.w):
                p = self.pixel[x][y]
                if p < 0x00:
                    ret += "¿?"
                elif p <= 0xff:
	                ret += " {:02x}".format(p)
                else:
                    ret += "?¿"
            ret += "\n"
        return ret[:-1]
        

    def __init__(self,val=0x00,size=DefaultSize):
        self.w, self.h = size.w,size.h
        if self.w <= 0 or self.h <= 0:
            raise dotlife.Error("invalid buffer dimensions {}x{}".format(self.w,self.h)) 
        val = Clamp(val)
        self.pixel = [ [ val for yy in range(self.h) ] for xx in range(self.w) ]
    
    
    def __getitem__(self,pos):
        posx,posy = pos
        x  = (self.w + posx) % self.w
        y =  (self.h + posy) % self.h            
        return self.pixel[x][y]

    def __setitem__(self,pos,val):
        posx,posy = pos
        x  = (self.w + posx) % self.w
        y =  (self.h + posy) % self.h            
        p = val
        if val < 0: p = 0
        if val > 0xff: p = 0xff
        self.pixel[x][y] = Clamp(p)


    def size(self):
        return Size(self.w,self.h)

    def palette(self,palette):
        ret = Buffer(size=(self.w,self.h))
        for y in range(self.h):
            for x in range(self.w):
                ret[x,y] = palette[ self[x,y] ]
        return ret
                

    def add(self,val):
        if type(val) in [type(0), type(0.0)]:
            return self.addScalar(val)
        if type(val) == type( Buffer() ):
            return self.addBuffer(val)
        raise Error("operation {} + {} -> {} not implemented".format(type(self).__name__,type(val).__name__,type(self).__name__) )

    def addScalar(self,val):
        for y in range(self.h):
            for x in range(self.w):
                self.pixel[x][y] = Clamp( self.pixel[x][y] + val )

    def addBuffer(self,val):
        for y in range(self.h):
            for x in range(self.w):
                if 0 <= x < val.w and 0 <= y < val.h:
                    self.pixel[x][y] += val[x,y]


    def mul(self,val):
        if type(val) in [type(0), type(0.0)]:
            return self.mulScalar(val)
        raise Error("operation {} * {} -> {} not implemented".format(type(self).__name__,type(val).__name__,type(self).__name__) )

    def mulScalar(self,val):
        for y in range(self.h):
            for x in range(self.w):
                self.pixel[x][y] = Clamp( self.pixel[x][y] * val )
    

        
                
    def tile(self,mask,light=0x1):
        for y in range(self.h):
            for x in range(self.w):
                if mask[x,y]:
                    self[x,y] = light


    def mask(self,mask,pos=(0,0),wrap=False,light=LIGHT):
        dx,dy = pos
        for y in range(mask.h):
            if not wrap and not 0 <= y+dy < self.h:
                continue
            for x in range(mask.w):
                if not wrap and not 0 <= x+dx < self.w:
                    continue
                if mask[x,y]:
                    self[x+dx,y+dy]= light
        


    def buffer(self,size=DefaultSize,pos=(0,0)):
        w,h = size.w,size.h
        dx,dy = pos
        ret = Buffer(size=size)
        for y in range(h):
            for x in range(w):
                ret[x,y] = self[x+dx,y+dy]
        return ret
        

# fillers



    def Fill(gray=0x1, size=DefaultSize ):
        w,h = size
        ret = Buffer(size=size)
        for y in range(h):
            for x in range(w):
                ret[x,y] = gray
        return ret

    def Gradient(heading=Direction.North, size=DefaultSize):
        ret = Buffer(size=size)
        w,h = size
        u,v = heading.value
        for y in range(h):
            for x in range(w):
                if u > 0:
                    ret[x,y] += x+1
                if u < 0:
                    ret[x,y] += (w-1-x+1)
                if v > 0:
                    ret[x,y] += y+1
                if v < 0:
                    ret[x,y] += (h-1-y+1)
        return ret                        
    
    
    def SixtyFourShadesOfGrey(mul=0x1):
        w,h = 8,8
        ret = Buffer( size=(w,h) )
        c = 0x1
        for y in range(h):
            for x in range(w):
                if y % 2 == 0:
                    ret.pixel[x][y] = Clamp(c * mul)
                else:
                    ret.pixel[w-1-x][y] = Clamp(c * mul)
                c += 1
        return ret
    
    def Checkers(black=0x00,white=0x20, size=DefaultSize):
        ret = Buffer()
        w,h = size
        for y in range(h):
            for x in range(w):
                if x % 2 != y % 2:
                    ret[x,y] = black
                else:
                    ret[x,y] = white
        return ret

    def Ranges(size=DefaultSize, mul=1):
        ret = Buffer()
        w,h = size
        c = 1
        for y in range(h):
            for x in range(w):
                if y < 4:
                    ret.pixel[x][y] = (x+1) + y*w
                else:
                    ret.pixel[x][y] = ( (x+1) + (y-4)*w ) * mul
        return ret        
