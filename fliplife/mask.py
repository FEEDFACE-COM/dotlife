
import dotlife
from dotlife.mask import Mask as dotMask
from dotlife.util import *


from fliplife import FRAMEWIDTH,FRAMEHEIGHT, FRAMESIZE

class Mask(dotMask):

    DefaultSize = FRAMESIZE


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


    def __init__(self,mask=None,val=False,size=DefaultSize):
        super().__init__(mask=mask,val=val,size=size)
    
    def __str__(self):
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
    
#    def __getitem__(self,pos):
#        posx,posy = pos
#        x  = (self.w + posx) % self.w
#        y =  (self.h + posy) % self.h
#        return self.pixel[x][y]
#
#    def __setitem__(self,pos,val):
#        posx,posy = pos
#        x  = (self.w + posx) % self.w
#        y =  (self.h + posy) % self.h
#        self.pixel[x][y] = val

    @classmethod 
    def FromMask(self,mask):
        ret = Mask()
        if mask.w != FRAMEWIDTH or mask.h != FRAMEHEIGHT:
            raise dotlife.Error("invalid mask size {}x{}".format(mask.w,mask.h)) 
        for y in range(0,FRAMEHEIGHT):
            for x in range(0,FRAMEWIDTH):
                ret.pixel[x][y] = mask[x,y]

    @classmethod
    def MaskFromResponse(self,rsp):
        ret = Mask(size=FRAMESIZE)
        x,y = 0,0
        if rsp == None:
            return
        for row in rsp:
            if y >= FRAMEHEIGHT:
                raise dotlife.Error("invalid response line count {}x{}".format(x,y))                 
            x = 0
            for col in row:
                if x > FRAMEWIDTH:
                    raise dotlife.Error("invalid response column count {}x{}".format(x,y))                 
                if col == 0x0A:
                    pass
                elif col == 0x20:
                    ret[x,y] = False
                else:
                    ret[x,y] = True
                x+=1
            y+=1
        return ret

        
    def toData(self):
        ret = ""
        for y in range(0,self.h):
            row = ""
            for x in range(0,self.w):
                if self.pixel[x][y]:
                    row += "X"
                else:
                    row += " "
            row += "\n"
            ret += row 
        return ret

    def deltaBright(self,msk2):
        ret = []
        for y in range(0,self.h):
            for x in range(0,self.w):
                if self[x,y] == True and msk2[x,y] == False:
                    ret += [(x,y)]
        return ret
        
    def deltaDark(self,msk2):
        ret = []
        for y in range(0,self.h):
            for x in range(0,self.w):
                if self[x,y] == False and msk2[x,y] == True:
                    ret += [(x,y)]
        return ret
                
