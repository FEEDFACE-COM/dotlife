
from dotlife.buffer import Buffer

class Mode():

    def __init__(self,timer,**params):
        self.timer = timer
        self.timer.fun = lambda: self.step(**params)
        self.debug = False


    def start(self):
        return False

    def draw(self):
        return Mask()

    def step(self,**params):
        pass

    def __str__(self):
        return "mode " + type(self).__name__.lower()
    

    def signal(self):
        self.debug ^= True
        debug("debug {}".format("on" if self.debug else "off") )


    def Init(mode,step):
        pass


