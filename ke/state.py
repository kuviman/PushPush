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
