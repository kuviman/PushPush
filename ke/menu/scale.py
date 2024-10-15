from .menuitem import *
from ..misc import *

class MScale(MenuItem):
    size = 55
    fontsize = 10
    labelsize = 7
    idlecolor = (0, 0, 0)
    activecolor = (1, 0, 0)
    width = 100

    def __init__(self, label, func, init, dragupdate):
        MenuItem.__init__(self)
        self.label = label
        self.func = func
        self.val = init
        self.dup = dragupdate
        self.color = self.idlecolor
        self.pressed = False

    def onRender(self, draw):
        draw.color(*self.color)
        dy = 5 if self.pressed else 0
        draw.text(self.label, (0, self.pos-self.labelsize-5),
                  self.labelsize)
        draw.rect((-self.width-5, self.pos),
                  (self.width+5, self.pos+self.fontsize*2+10))
        draw.color(1, 1, 1)
        draw.rect((-self.width, self.pos+2),
                  (self.width, self.pos+self.fontsize*2+8))
        draw.color(1 if self.pressed else 0.7, 0.7, 0.7)
        draw.rect((-self.width, self.pos+2),
                  (-self.width+2*self.val*self.width,
                   self.pos+self.fontsize*2+8))
        draw.color(*((0, 0, 0) if self.pressed else self.color))
        draw.text("%d %%"%int(self.val*100),
                  (0, self.pos+self.fontsize+5),
                  self.fontsize)

    def drag(self, x):
        self.val = clamp(0.5*(x+self.width)/self.width, 0, 1)
        if self.dup:
            self.func (self.val,)

    def onPress(self, x):
        self.pressed = True
        self.drag(x)

    def onMouseMove(self, x):
        if self.pressed:
            self.drag(x)

    def onRelease(self):
        self.pressed = False
        self.func (self.val,)

    def onFocus(self, gain):
        self.color = self.activecolor if gain else self.idlecolor
