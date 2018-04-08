
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
from OpenGL.GL import *
from image import *
from draw import *
from font import *
from menu import *
from sound import *
from input import *

DEFRESOLUTION = (640, 480)

class App:

    def __init__(self, title="kEngine app", size=None,
                 fullscreen=False, icon=None):
        self.fs = fullscreen
        pygame.mixer.pre_init(buffer=512)
        pygame.init()
        pygame.mixer.set_num_channels(100)
        #pygame.mouse.set_visible(False)
        pygame.display.set_caption(title)
        if icon:
            self.set_icon(icon)
        flags = OPENGL|DOUBLEBUF|HWSURFACE|(FULLSCREEN if fullscreen else 0)
        if size is None:
            if fullscreen:
                size = pygame.display.list_modes()[0]
            else:
                size = DEFRESOLUTION
        self.screen = pygame.display.set_mode(size, flags)
        self.draw = DrawModule(self)
        self.timer = pygame.time.Clock()

    def music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
    def volume(self, music=None, sfx=None):
        if music is not None:
            pygame.mixer.music.set_volume(music)
        if sfx is not None:
            Sound.set_volume(sfx)

    def list_modes(self):
        return pygame.display.list_modes()

    def load_font(self, path):
        self.draw.font = Font(path)

    def aspect(self):
        w, h = self.screen.get_size()
        return float(w)/float(h)

    def get_size(self):
        return self.screen.get_size()

    def set_icon(self, path):
        pygame.display.set_icon(pygame.image.load(path))

    def resize(self, size=None, fullscreen=None):
        if size is None:
            size = self.get_size()
        if fullscreen is None:
            fullscreen = self.fs
        flags = OPENGL|DOUBLEBUF|HWSURFACE|(FULLSCREEN if fullscreen else 0)
        self.screen = pygame.display.set_mode(size, flags)
        self.reload()

    def reload(self):
        glViewport(0, 0, *self.screen.get_size())
        Image.reload_all()
        Font.reload_all()
        self.draw.reload()

    def get_mouse(self, h=None):
        sw, sh = self.get_size()
        if h is None:
            h = sh
        x, y = pygame.mouse.get_pos()
        k = float(h)/float(sh)
        return (x-sw/2)*k, (y-sh/2)*k

    def close(self):
        pygame.quit()

    def input(self, prompt):
        x = Input(self, prompt)
        x.run()
        return x.val
    def choose(self, choice, title, onpage=10):
        ms = [Menu(self)]
        ms[-1].add_title(title)
        ms[-1].add_separator()
        val = [-1, ms[-1]]
        n = 0
        i = 0
        ch = list(reversed(choice))
        def ret(m, v):
            def f():
                val[0] = v
                m.close()
            return f
        while len(ch):
            if n == onpage:
                ms.append(Menu(self))
                ms[-1].add_title(title)
                ms[-1].add_separator()
                n = 0
            ms[-1].add_button(ch[-1], ret(ms[-1], i))
            ch.pop()
            i += 1
            n += 1
        i = 0
        def goto(fr, to):
            def f():
                fr.close()
                val[1] = to
            return f
        for m in ms:
            m.add_separator()
            if i > 0:
                m.add_button("previous", goto(m, ms[i-1]))
            if i < len(ms)-1:
                m.add_button("next", goto(m, ms[i+1]))
            m.add_button("back", m.close)
            i += 1
        while val[1] is not None:
            m = val[1]
            val[1] = None
            m.run()
        return val[0]

    def message(self, text, buttons=('OK',)):
        def f():
            return self.show_message(text, buttons)
        return f
    def show_message(self, text, buttons=('OK',)):
        m = Menu(self)
        for line in text.split('\n'):
            m.add_label(line)
        def ret(n):
            def f():
                m.val = n
                m.close()
            return f
        i = 0
        m.add_separator()
        for b in buttons:
            m.add_button(b, ret(i))
            i += 1
        m.run()
        return m.val
