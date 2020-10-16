
from dotlife import *
from dotlife.buffer import Buffer
from dotlife.util import *




class Mask:

    DefaultSize = Size(8,8)



    
    def __init__(self,mask=None,val=False,size=DefaultSize):
        if mask:
            self.w,self.h = mask.w,mask.h
            self.pixel = [ [ mask[x,y] for y in range(self.h) ] for x in range(self.w) ]
        else:
            self.w, self.h = size.w,size.h
            if self.w <= 0 or self.h <= 0:
                raise Error("invalid mask dimensions {}x{}".format(self.w,self.h)) 
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

    def size(self):
        return Size(self.w,self.h)

#    def inverse(self):
#        ret = Mask(size=Size(self.w,self.h))
#        for y in range(self.h):
#            for x in range(self.w):
#                ret.pixel[x][y] = not self.pixel[x][y]
#        return ret

    
    def set(self,val=True):
        for y in range(self.h):
            for x in range(self.w):
                self.pixel[x][y] = True
    

    def inv(self):
        for y in range(self.h):
            for x in range(self.w):
                self.pixel[x][y] ^= True
        return self

    def flip(self,flip):
        w,h = self.w,self.h
        tmp = Mask(mask=self)
        
        for y in range(self.h):
            for x in range(self.w):
                if flip == Flip.horizontal:
                    self.pixel[x][y] = tmp[x,h-1-y]
                elif flip == Flip.vertical:
                    self.pixel[x][y] = tmp[w-1-x,y]
                elif flip == Flip.point:
                    self.pixel[x][y] = tmp[w-1-x,h-1-y]

        return self
                

#    def __add__(self,val):
#        if type(val) == type( Mask() ):
#            return self.addMask(val)
#        raise Error("operation {} + {} -> {} not implemented".format(type(self).__name__,type(val).__name__,type(self).__name__) )
#
#    def addMask(self,val):
#        for y in range(self.h):
#            for x in range(self.w):
#                if 0 <= x < val.w and 0 <= y < val.h:
#                    self.pixel[x][y] = val[x,y]
#        return self
#

    


    def addMask(self,mask,pos=Position(0,0),wrap=False):
        for y in range(mask.h):
            if not wrap and not 0 <= y+pos.y < self.h:
                continue
            for x in range(mask.w):
                if not wrap and not 0 <= x+pos.x < self.w:
                    continue
                if mask[x,y]:
                    self[x+pos.x,y+pos.y] = mask[x,y]
        return self
        
        
    def subMask(self,pos=Position(0,0),size=Size(1,1)):
        ret = Mask(size=size)
        for y in range(ret.h):
            if y+pos.y >= self.h:
                continue
            for x in range(ret.w):
                if x+pos.x >= self.w:
                    continue
                if self[x+pos.x,y+pos.y]:
                    ret[x,y] = True
        return ret


    def trimMask(self):
        size = self.size()
        pos = Position(0,0)
        keep = False
        for y in range(self.size.h):
            if self[0,y]:
                keep = True
        if not keep:
            size.w -= 1
            pos.x += 1
        keep = False
        for y in range(self.size.h):
            if self[self.size.w-1,y]:
                keep = True
        if not keep:
            size.w -= 1
        
        
        
        
        return ret
        
    @classmethod    
    def Load(self,pattern):
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
        
        ret = Mask(size=Size(w,h))

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
    
    
    def __eq__(self,other):
        if self.w != other.w or self.h != other.h:
            return False
        for y in range(self.h):
            for x in range(self.w):
                if self[x,y] != other[x,y]:
                    return False
        return True
    

    def __str__(self):
        MAP = {
            (False,False,False,False): " ",
            (False,False,False,True ): "▗",
            (False,False,True, False): "▖",
            (False,False,True, True ): "▄",
            (False,True ,False,False): "▝",
            (False,True ,False,True ): "▐",
            (False,True ,True, False): "▞",
            (False,True ,True, True ): "▟",
            (True, False,False,False): "▘",
            (True, False,False,True ): "▚",
            (True, False,True, False): "▌",
            (True, False,True, True ): "▙",
            (True, True ,False,False): "▀",
            (True, True ,False,True ): "▜",
            (True, True ,True, False): "▛",
            (True, True ,True, True ): "█",
            (None, None ,None, None ): "#",
        }

        ret = ""

        # large mask
        if self.h > 8 or self.w > 24:

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
                    ret += MAP[(a,b,c,d)] 
                ret += "{:1d}\n".format(y%10)
            for x in range(0,self.w,2):
                if x % 10 == 0:
                    ret += "{:d}".format( (int((x%100)/10)) )
                else:
                    ret += " "
            ret += "\n"

        elif self.w == 1 and self.h == 1:
            if self[0,0]:
                return "⬛︎0\n0   \n"
            else:
                return "⬜︎0\n0   \n"


        # small mask
        else:
            for y in range(self.h):
                for x in range(self.w):
                    p = self.pixel[x][y]
                    if p:
                        ret += "██"
                    else:
                        ret += " ̣ "
                ret += " {:01d}\n".format(y%10)
            for x in range(self.w):
                ret += " {:01d}".format(x%10)
    
        return ret[:-1]
    
