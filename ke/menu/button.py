from .menuitem import *

class MButton(MenuItem):
    size = 25
    fontsize = 10
    idlecolor = (0, 0, 0)
    activecolor = (1, 0, 0)

    def __init__(self, label, func):
        MenuItem.__init__(self)
        self.label = label
        self.func = func
        self.color = self.idlecolor
        self.pressed = False

    def onRender(self, draw):
        draw.color(*self.color)
        dy = 5 if self.pressed else 0
        draw.text(self.label, (0, self.pos+dy), self.fontsize)

    def onPress(self, x):
        self.pressed = True

    def onRelease(self):
        self.pressed = False
        self.func()

    def onFocus(self, gain):
        self.color = self.activecolor if gain else self.idlecolor
