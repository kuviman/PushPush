from .menuitem import *

class MCheck(MenuItem):
    size = 25
    fontsize = 10
    idlecolor = (0, 0, 0)
    activecolor = (1, 0, 0)
    linewidth = 2
    lineoff = 25

    def __init__(self, label, func, init):
        MenuItem.__init__(self)
        self.label = label
        self.func = func
        self.val = init
        self.color = self.idlecolor
        self.pressed = False

    def onRender(self, draw):
        draw.color(*self.color)
        dy = 5 if self.pressed else 0
        draw.text(self.label, (0, self.pos+dy), self.fontsize)
        w = draw.text_width(self.label, self.fontsize)/2.0
        if not self.val:
            draw.rect((-w-self.lineoff, self.pos+dy-self.linewidth),
                      (w+self.lineoff, self.pos+dy+self.linewidth))

    def onPress(self, x):
        self.pressed = True

    def onRelease(self):
        self.pressed = False
        self.val = not self.val
        self.func(self.val,)

    def onFocus(self, gain):
        self.color = self.activecolor if gain else self.idlecolor

