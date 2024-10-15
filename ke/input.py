from .state import *
import pygame
from pygame.locals import *

class Input(State):
    blink = 0.5

    def __init__(self, app, prompt):
        State.__init__(self, app)
        self.label = prompt
        self.val = ""
        self.t = self.blink*2

    def onUpdate(self, dt):
        self.t -= dt
        while self.t < 0:
            self.t += self.blink*2

    def onRender(self, draw):
        draw.clear()
        draw.flat(20)
        draw.color(0.5, 0.5, 0.5)
        draw.text(self.label, (0, -2), 0.5)
        draw.color(0, 0, 0)
        draw.text(self.val, (0, 1), 1)
        w = draw.text_width(self.val, 1)/2.0
        if self.t < self.blink:
            draw.rect((w+0.2, 0), (w+0.7, 2))

    def onKeyDown(self, key):
        nm = pygame.key.name(key)
        if key == K_ESCAPE:
            self.val = None
            self.close()
        elif key == K_RETURN:
            self.close()
        elif len(nm) == 1:
            self.val += nm
        elif key == K_BACKSPACE:
            self.val = self.val[:-1]
