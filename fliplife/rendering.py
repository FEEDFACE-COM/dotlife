
from dotlife.util import *
from fliplife import http


class Rendering():



    def __init__(self,address,nowrite,noread):
        super().__init__()
        self.address = address
        self.nowrite, self.noread = nowrite,noread


    
    def getMode(self):
        debug("rendering mode get {:s}".format(self.address))
        if self.noread:
            return None
        rsp = http.get(self.address,"rendering/mode",None)
        if rsp == None:
            return None
        val = rsp.read()
        if val == Rendering.Mode.Full.value:
            return Rendering.Mode.Full
        if val == Rendering.Mode.Diff.value:
            return Rendering.Mode.Diff
        return None


    def setMode(self,mode):
        debug("rendering mode {:s} {:s}".format(mode.name,self.address))
        data = mode.value
        if self.nowrite:
            return None 
        rsp = http.put(self.address,"rendering/mode",None,data)
        if rsp == None:
            return None
        val = rsp.read()
        return val



    def GetTiming(self): #TODO
        debug("rendering timings get {:s}".format(self.address))
        if self.noread:
            return None
        rsp = http.get(self.address,"rendering/timings",None)
        if rsp == None:
            return None
        val = rsp.read()
        # todo
        return None



