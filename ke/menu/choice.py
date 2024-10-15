from .menuitem import *

class MChoice(MenuItem):
    size = 45
    fontsize = 10
    labelsize = 7
    idlecolor = (0, 0, 0)
    activecolor = (1, 0, 0)

    def __init__(self, label, choice, func, init):
        MenuItem.__init__(self)
        self.label = label
        self.choice = choice
        self.func = func
        self.idx = init
        self.color = self.idlecolor
        self.pressed = False

    def onRender(self, draw):
        draw.color(*self.color)
        dy = 5 if self.pressed else 0
        draw.text(self.label, (0, self.pos-self.labelsize-5),
                  self.labelsize)
        draw.text(self.choice[self.idx],
                  (0, self.pos+dy+self.fontsize),
                  self.fontsize)

    def onPress(self, x):
        self.pressed = True

    def onRelease(self):
        self.pressed = False
        self.idx = (self.idx+1)%len(self.choice)
        self.func(self.idx,)

    def onFocus(self, gain):
        self.color = self.activecolor if gain else self.idlecolor
