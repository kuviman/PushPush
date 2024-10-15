from .menuitem import *

class MTitle(MenuItem):
    clickable = False
    size = 50
    fontsize = 24
    color = (1, 0.5, 0)

    def __init__(self, title):
        MenuItem.__init__(self)
        self.title = title

    def onRender(self, draw):
        draw.color(*self.color)
        draw.text(self.title, (0, self.pos), self.fontsize)
