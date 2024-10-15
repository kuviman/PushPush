from .menuitem import *

class MLabel(MenuItem):
    clickable = False
    size = 20
    fontsize = 7
    color = (0.3, 0.3, 0.3)

    def __init__(self, label):
        MenuItem.__init__(self)
        self.label = label

    def onRender(self, draw):
        draw.color(*self.color)
        draw.text(self.label, (0, self.pos), self.fontsize)
