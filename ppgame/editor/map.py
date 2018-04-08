
##    PushPush v1.0
##
##    Copyright (C) 2011 kuviman
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##    you can contact me kuviman@gmail.com

import ke
from ke.misc import *
import pickle

EMPTY   = 0
WALL    = 1
BOX     = 2
STORAGE = 3
ENTRY   = 4
STOBOX  = 5
PLASTO  = 6

class Map(ke.Object):
    def __init__(self, path=None, size=20):
        if path is None:
            self.size = size
            self.map = array2d(self.size, self.size, EMPTY)
        else:
            self.load(path)
        self.load_images()

    def load_images(self):
        self.im_empty = ke.Image("data/images/empty.tga", (1, 1))
        self.im_wall = ke.Image("data/images/wall.tga", (1, 1))
        self.im_box = ke.Image("data/images/box.tga", (1, 1))
        self.im_store = ke.Image("data/images/storage.tga", (1, 1))
        self.im_entry = ke.Image("data/images/player.tga", (1, 1))

    def load(self, path):
        self.map = pickle.load(open(path, "rb"))
        self.size = len(self.map)

    def save(self, path):
        print "saving", path
        pickle.dump(self.map, open(path, "wb"))

    def onRender(self, draw):
        draw.color(0, 0, 0, 0.5)
        draw.rect((-1, -1), (self.size, self.size))
        draw.color(1, 1, 1)
        draw.rect((-0.5, -0.5), (self.size-0.5, self.size-0.5))
        for i in xrange(self.size):
            for j in xrange(self.size):
                val = self.map[i][j]
                draw.color(1, 1, 1)
                if val == EMPTY:
                    im = self.im_empty
                elif val == WALL:
                    im = self.im_wall
                elif val == BOX:
                    im = self.im_box
                elif val == STORAGE:
                    im = self.im_store
                elif val == ENTRY:
                    im = self.im_entry
                elif val == STOBOX:
                    draw.color(0.5, 0.5, 0.5)
                    im = self.im_box
                elif val == PLASTO:
                    draw.image(self.im_store, (i, j))
                    im = self.im_entry
                else:
                    raise ValueError
                draw.image(im, (i, j))

    def set_at(self, (i, j), val):
        self.map[i][j] = val
