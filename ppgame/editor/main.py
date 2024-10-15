import ke
from ke.locals import *
from ke.misc import *
from .map import *
import os

HOWTO = '''PushPush editor howto

LMB - put a wall
RMB - clear cell
w/a/s/d or arrow keys - look around
1 - place a box
2 - place storage
3 - already stored box
4 - entry & storage togather
P - entry point'''
#0 - increase map size'''

class Editor(ke.State):
    scrollspeed = 20
    bound = 2
    vh = 14

    def __init__(self, app):
        ke.State.__init__(self, app)
        self.build_menu()
        self.new_map()
        self.pressed = None
        self.dx, self.dy = 0, 0

    def new_map(self, path=None):
        self.map = Map(path)
        self.px, self.py = (self.map.size-1)/2.0, (self.map.size-1)/2.0
        self.sel = None
        self.menu.close()

    def save(self):
        x = self.app.input("enter name")
        if x is not None:
            self.map.save("levels/user levels/%s.ppl"%x)
            self.app.show_message("level saved successfully")

    def load(self):
        lst = os.listdir("levels/user levels")
        print(lst)
        x = self.app.choose([s.split('.')[0] for s in lst], "Load Level")
        if x >= 0:
            self.new_map("levels/user levels/%s"%lst[x])
            self.menu.close()

    def build_menu(self):
        em = ke.Menu(self.app)
        em.add_title("Editor")
        em.add_separator()
        em.add_button("continue", em.close)
        em.add_button("new map", self.new_map)
        em.add_button("save", self.save)
        em.add_button("load", self.load)
        em.add_button("howto", self.app.message(HOWTO, ("back",)))
        em.add_separator()
        def exit():
            em.close()
            self.close()
        em.add_button("exit editor", exit)
        self.menu = em

    def onUpdate(self, dt):
        self.px = clamp(self.px+self.scrollspeed*self.dx*dt, 0, self.map.size-1)
        self.py = clamp(self.py+self.scrollspeed*self.dy*dt, 0, self.map.size-1)

    def onRender(self, draw):
        draw.clear()
        draw.flat(self.vh)
        draw.translate(-self.px, -self.py)
        self.map.render(draw)
        if self.sel is not None:
            x, y = self.sel
            draw.color(1, 0, 0, 0.5)
            draw.point((x, y), 0.5)
        w = draw.flat(6)
        draw.color(1, 1, 1, 0.5)
        draw.rect((-w/2.0, 2), (w/2.0, 3))
        draw.color(0, 0, 0)
        draw.text("press ESC to open editor menu", (0, 2.5), 0.1)

    def onMouseDown(self, button):
        self.pressed = button
        self.put()
    def onMouseUp(self, button):
        self.pressed = None

    def onKeyDown(self, key):
        if key == K_ESCAPE:
            self.menu.run()
        elif key == K_w or key == K_UP:
            self.dy -= 1
        elif key == K_s or key == K_DOWN:
            self.dy += 1
        elif key == K_a or key == K_LEFT:
            self.dx -= 1
        elif key == K_d or key == K_RIGHT:
            self.dx += 1
        elif key == K_1:
            if self.sel is not None:
                self.map.set_at(self.sel, BOX)
        elif key == K_2:
            if self.sel is not None:
                self.map.set_at(self.sel, STORAGE)
        elif key == K_3:
            if self.sel is not None:
                self.map.set_at(self.sel, STOBOX)
        elif key == K_4:
            if self.sel is not None:
                self.map.set_at(self.sel, PLASTO)
        elif key == K_p:
            if self.sel is not None:
                self.map.set_at(self.sel, ENTRY)

    def onKeyUp(self, key):
        if key == K_w or key == K_UP:
            self.dy += 1
        elif key == K_s or key == K_DOWN:
            self.dy -= 1
        elif key == K_a or key == K_LEFT:
            self.dx += 1
        elif key == K_d or key == K_RIGHT:
            self.dx -= 1

    def put(self):
        if self.sel is None:
            return
        if self.pressed == 1:
            self.map.set_at(self.sel, WALL)
        elif self.pressed == 3:
            self.map.set_at(self.sel, EMPTY)

    def onMouseMove(self):
        mx, my = self.app.get_mouse(self.vh)
        mx += self.px+0.5
        my += self.py+0.5
        if mx < 0:
            mx -= 1
        if my < 0:
            my -= 1
        mx, my = int(mx), int(my)
        if (0 <= mx < self.map.size and 0 <= my < self.map.size):
            self.sel = (mx, my)
        else:
            self.sel = None
        self.put()
