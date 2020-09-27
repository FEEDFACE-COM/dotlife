
from dotlife.buffer import Buffer

class Mode():

    def __init__(self,timer):
        self.timer = timer
        self.timer.fun = lambda : self.step()
        self.last = Buffer()
        self.debug = False


    def draw(self):
        return Buffer()

    def step(self):
        self.last = self.draw()

    def __str__(self):
        return "mode " + type(self).__name__.lower()
    

    def signal(self):
        self.debug ^= True
        debug("debug {}".format("on" if self.debug else "off") )


    def Init(mode,step):
        pass


