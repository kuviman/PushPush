
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

import pygame
from pygame.locals import *

class shutdown(Exception): pass

current = None

class State:
    def __init__(self, app):
        self.app = app

    def run(self):
        self.onStart()
        last = current
        if last:
            last.onPause()
        self.power = True
        while self.power:
            try:
                self.onUpdate(self.app.timer.tick()/1000.0)
                self.onRender(self.app.draw)
                pygame.display.flip()
                for e in pygame.event.get():
                    if e.type == QUIT:
                        self.onQuit()
                    elif e.type == KEYDOWN:
                        self.onKeyDown(e.key)
                    elif e.type == KEYUP:
                        self.onKeyUp(e.key)
                    elif e.type == MOUSEBUTTONDOWN:
                        self.onMouseDown(e.button)
                    elif e.type == MOUSEBUTTONUP:
                        self.onMouseUp(e.button)
                    elif e.type == MOUSEMOTION:
                        self.onMouseMove()
            except Exception as e:
                x = self.app.show_message(
                    "Error:\n%s"%e,('ignore', 'close app'))
                if x == 1:
                    raise Exception("bad")
        if last:
            last.onResume()

    def close(self):
        self.onClose()
        self.power = False

    def onStart(self):
        pass
    def onPause(self):
        pass
    def onResume(self):
        pass
    def onQuit(self):
        raise shutdown
    def onClose(self):
        pass
    def onKeyDown(self, key):
        if key == K_ESCAPE:
            self.close()
    def onKeyUp(self, key):
        pass
    def onMouseDown(self, button):
        pass
    def onMouseUp(self, button):
        pass
    def onMouseMove(self):
        pass
    def onUpdate(self, dt):
        pass
    def onRender(self, draw):
        draw.clear()
