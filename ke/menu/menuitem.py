from ..objects import *

class MenuItem(Object):
    clickable = True
    def onPress(self, x):
        pass
    def onRelease(self):
        pass
    def onFocus(self, gain):
        pass
    def onMouseMove(self, x):
        pass

class MSeparator(MenuItem):
    clickable = False
    size = 30
