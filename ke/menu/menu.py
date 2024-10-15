from ..state import *
from ..objects import *
from ..sound import *
from .menuitem import *
from .button import *
from .title import *
from .label import *
from .check import *
from .choice import *
from .scale import *

class Menu(State):
    border = 50
    space = 5
    minsize = 400

    def __init__(self, app, sndpath="data/menu.wav"):
        State.__init__(self, app)
        self.items = Group()
        self.size = self.border*2-self.space
        self.y = self.border
        self.focus = None
        self.pressed = False
        self.snd = Sound(sndpath)

    def add_item(self, item):
        self.items.add(item)
        item.pos = self.y+item.size/2.0
        self.size += item.size+self.space
        self.y += item.size+self.space

    def add_button(self, label, func=None):
        self.add_item(MButton(label, func))
    def add_separator(self):
        self.add_item(MSeparator())
    def add_label(self, label):
        self.add_item(MLabel(label))
    def add_title(self, title):
        self.add_item(MTitle(title))
    def add_check(self, label, func=None, init=True):
        self.add_item(MCheck(label, func, init))
    def add_choice(self, label, choice, func=None, init=0):
        self.add_item(MChoice(label, choice, func, init))
    def add_scale(self, label, func=None, init=0.5, dragupdate=False):
        self.add_item(MScale(label, func, init, dragupdate))

    def onUpdate(self, dt):
        self.items.update(dt)

    def onRender(self, draw):
        draw.clear()
        draw.flat(max(self.minsize, self.size))
        draw.translate(0, -self.size/2.0)
        # print(self.items.objects)
        self.items.render(draw)

    def onMouseDown(self, button):
        if button != 1:
            return
        self.pressed = True
        self.mselect()
        if self.focus:
            self.focus.onPress(self.app.get_mouse(
                max(self.minsize, self.size))[0])

    def onMouseUp(self, button):
        if button != 1:
            return
        self.pressed = False
        if self.focus:
            self.focus.onRelease()

    def onMouseMove(self):
        if self.focus:
            self.focus.onMouseMove(self.app.get_mouse(
                max(self.minsize, self.size))[0])
        if self.pressed:
            return
        self.mselect()

    def onKeyDown(self, key):
        if key == K_ESCAPE:
            self.close()
        elif key == K_UP or key == K_w:
            self.kselect(-1)
        elif key == K_DOWN or key == K_s:
            self.kselect(+1)
        elif key in (K_SPACE, K_RETURN, K_KP_ENTER):
            if self.focus is None or not self.focus.clickable:
                for item in self.items:
                    if item.clickable:
                        self.focus = item
                        self.focus.onFocus(True)
                        break
            self.pressed = True
            self.focus.onPress(0)

    def onKeyUp(self, key):
        if key in (K_SPACE, K_RETURN, K_KP_ENTER):
            self.pressed = False
            if self.focus:
                self.focus.onRelease()

    def kselect(self, d):
        focus = None
        if self.focus:
            i = self.items.objects.index(self.focus)+len(self.items.objects)+d
            while not self.items.objects[i%len(self.items.objects)].clickable:
                i += d
            focus = self.items.objects[i%len(self.items.objects)]
        else:
            for item in (self.items if d > 0 else reversed(list(self.items.objects))):
                if item.clickable:
                    focus = item
                    break
        if focus != self.focus:
            if focus:
                if focus.clickable:
                    self.snd.play()
                focus.onFocus(True)
            if self.focus:
                self.focus.onFocus(False)
            self.focus = focus

    def mselect(self):
        mx, my = self.app.get_mouse(max(self.minsize, self.size))
        my += self.size/2.0
        y = self.border
        focus = None
        for item in self.items:
            if y < my < y+item.size:
                focus = item
            y += item.size+self.space
        if focus != self.focus:
            if focus:
                if focus.clickable:
                    self.snd.play()
                focus.onFocus(True)
            if self.focus:
                self.focus.onFocus(False)
            self.focus = focus
