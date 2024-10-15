import ke
from ke.misc import *
from ke.locals import *
from OpenGL.GL import *
import pickle
import pygame

EMPTY = 0
WALL = 1
BOX = 2
STORAGE = 3
PLAYER = 4
STOBOX = 5
PLASTO = 6

class Game(ke.State):

    def __init__(self, app):
        ke.State.__init__(self, app)
        self.im_empty = ke.Image("data/images/empty.tga", (1, 1))
        self.im_wall = ke.Image("data/images/wall.tga", (1, 1))
        self.im_box = ke.Image("data/images/box.tga", (1, 1))
        self.im_store = ke.Image("data/images/storage.tga", (1, 1))
        self.im_player = ke.Image("data/images/player.tga", (1, 1))
        self.snd_lose = ke.Sound("data/sfx/lose.wav")
        self.snd_push = ke.Sound("data/sfx/push.wav")
        self.snd_min = ke.Sound("data/sfx/min.wav")
        self.snd_sec = ke.Sound("data/sfx/sec.wav")
        self.snd_store = ke.Sound("data/sfx/store.wav")
        self.snd_win = ke.Sound("data/sfx/win.wav")

    def load(self, path, title):
        self.title = title
        self.boxes = []
        mp = pickle.load(open(path, "rb"))
        fi = fj = max(len(mp), len(mp[0]))
        for i in range(len(mp)):
            for j in range(len(mp[0])):
                if mp[i][j] != EMPTY:
                    fi = min(fi, i)
                    li = i
        for j in range(len(mp[0])):
            for i in range(len(mp)):
                if mp[i][j] != EMPTY:
                    fj = min(fj, j)
                    lj = j
        self.map = []
        for i in range(li-fi+1):
            self.map.append([])
            for j in range(lj-fj+1):
                self.map[-1].append(mp[fi+i][fj+j])
        for i in range(li-fi+1):
            for j in range(lj-fj+1):
                if self.map[i][j] == BOX:
                    self.boxes.append((i, j))
                elif self.map[i][j] == PLAYER:
                    self.player = (i, j)
                elif self.map[i][j] == STOBOX:
                    self.boxes.append((i, j))
                    self.map[i][j] = STORAGE
                    continue
                elif self.map[i][j] == PLASTO:
                    self.player = (i, j)
                    self.map[i][j] = STORAGE
                    continue
                else:
                    continue
                self.map[i][j] = EMPTY
        self.size = max(li-fi+1, lj-fj+1)
        w, h = self.app.get_size()
        self.vh = max(2.0*(lj-fj+1), 10/9.0*(li-fi+1)/self.app.aspect())
        self.px, self.py = (li-fi)/2.0, (lj-fj)/2.0
        self.build_map(self.app.draw)
        self.time = 0
        self.moves = 0
        self.pushes = 0
        self.success = None
        self.stack = []

    def onUpdate(self, dt):
        if int(self.time+dt) != int(self.time):
            if int(self.time)%60 == 59:
                self.snd_min.play()
            else:
                pass#self.snd_sec.play()
        self.time += dt

    def go(self, dx, dy):
        x, y = self.player
        x += dx; y += dy
        if self.map[x][y] in (EMPTY, STORAGE):
            if (x, y) in self.boxes:
                if self.map[x+dx][y+dy] in (EMPTY, STORAGE) and \
                   (x+dx, y+dy) not in self.boxes:
                    self.stack.append((self.player, (x, y), (x+dx, y+dy)))
                    self.boxes.remove((x, y))
                    self.boxes.append((x+dx, y+dy))
                    if self.map[x+dx][y+dy] == STORAGE:
                        self.snd_store.play()
                    self.snd_push.play()
                    self.player = x, y
                    self.pushes += 1
                    self.moves += 1
            else:
                self.stack.append((self.player, None, None))
                self.player = x, y
                self.moves += 1
        for i, j in self.boxes:
            if self.map[i][j] != STORAGE:
                return
        self.success = True
        self.snd_win.play()
        self.app.show_message("level complete\n\n"
                              "time - %02d:%02d\n"
                              "moves - %d\n"
                              "pushes - %d"%(int(self.time)/60, int(self.time)%60,
                                             self.moves, self.pushes))
        self.close()

    def onClose(self):
        glDeleteLists(self.map_dlist, 1)

    def onRender(self, draw):
        draw.clear()
        draw.flat(self.vh)
        draw.translate(-self.px, -self.py)
        glCallList(self.map_dlist)
        draw.image(self.im_player, self.player)
        for box in self.boxes:
            i, j = box
            if self.map[i][j] == EMPTY:
                draw.color(1, 1, 1)
            else:
                draw.color(0.5, 0.5, 0.5)
            draw.image(self.im_box, box)
        w = draw.flat(12)/2.0
        draw.color(1, 1, 1, 0.5)
        draw.rect((-w, -4), (-w, -6))
        draw.rect((-w, 4), (w, 6))
        draw.color(0, 0, 0)
        tw = draw.text_width(self.title, 1)/2.0
        draw.text(self.title, (0, -5), min(w/(tw+10), 0.8))
        draw.text("time", (0, 4), 0.3)
        draw.text("%02d:%02d"%(int(self.time)/60, int(self.time)%60), (0, 5), 0.7)
        draw.text("moves", (-w*0.7, 4), 0.2)
        draw.text(str(self.moves), (-w*0.7, 5), 0.5)
        draw.text("pushes", (w*0.7, 4), 0.2)
        draw.text(str(self.pushes), (w*0.7, 5), 0.5)

    def onKeyDown(self, key):
        if key == K_ESCAPE:
            self.close()
        elif key == K_UP or key == K_w:
            self.go(0, -1)
        elif key == K_DOWN or key == K_s:
            self.go(0, 1)
        elif key == K_LEFT or key == K_a:
            self.go(-1, 0)
        elif key == K_RIGHT or key == K_d:
            self.go(1, 0)
        elif key == K_F2:
            self.success = False
            self.close()
        elif key == K_BACKSPACE:
            if len(self.stack):
                self.player, np, lp = self.stack.pop()
                self.moves += 1
                if np is not None:
                    self.boxes.remove(lp)
                    self.boxes.append(np)

    def build_map(self, draw):
        self.map_dlist = glGenLists(1)
        glNewList(self.map_dlist, GL_COMPILE)
        draw.color(1, 1, 1)
        i = 0
        for row in self.map:
            j = 0
            for x in row:
                if x == EMPTY:
                    im = self.im_empty
                elif x == WALL:
                    im = self.im_wall
                elif x == STORAGE:
                    im = self.im_store
                else:
                    raise ValueError
                draw.image(im, (i, j))
                j += 1
            i += 1
        glEndList()
