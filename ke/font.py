
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
from OpenGL.GL import *

class Font:
    all = []
    @staticmethod
    def reload_all():
        for font in Font.all:
            font.reload()

    def __init__(self, path, space=0):
        self.path = path
        self.space = space
        self.reload()
        Font.all.append(self)

    def reload(self):
        im = pygame.image.load(self.path)
        self.tex = glGenTextures(1)
        w, h = im.get_size()
        glBindTexture(GL_TEXTURE_2D, self.tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, w, h,
            0, GL_RGBA, GL_UNSIGNED_BYTE,
            pygame.image.tostring(im, "RGBA"))
        self.ws = [0]*256
        size = w//16
        self.dbase = glGenLists(256)
        for x in range(16):
            for y in range(16):
                c = y*16+x
                sub = im.subsurface((x*size, y*size, size, size))
                x1 = None
                for i in range(int(size)):
                    for j in range(int(size)):
                        if sub.get_at((i, j)).a != 0:
                            x1 = x+float(i-1)/size
                            break
                    if x1 is not None:
                        break
                if x1 is None:
                    x1 = x
                x2 = None
                for i in range(size):
                    for j in range(size):
                        if sub.get_at((size-i-1, j)).a != 0:
                            x2 = x+1-float(i-1)/size
                            break
                    if x2 is not None:
                        break
                if x2 is None:
                    x2 = x+0.5
                glNewList(self.dbase+c, GL_COMPILE)
                glBegin(GL_QUADS)
                glTexCoord2f(x1/16.0, y/16.0)
                glVertex2f(0, -1)
                glTexCoord2f(x2/16.0, y/16.0)
                glVertex2f((x2-x1)*2, -1)
                glTexCoord2f(x2/16.0, (y+1)/16.0)
                glVertex2f((x2-x1)*2, 1)
                glTexCoord2f(x1/16.0, (y+1)/16.0)
                glVertex2f(0, 1)
                glEnd()
                glTranslatef((x2-x1)*2+self.space, 0, 0)
                glEndList()
                self.ws[c] = (x2-x1)*2

    def render(self, text, pos, size, align=(0, 0)):
        x, y = pos
        ax, ay = align
        w = self.width(text, size)
        glBindTexture(GL_TEXTURE_2D, self.tex)
        glPushMatrix()
        glTranslatef(x-(ax+1)*w/2.0, y-ay*size, 0)
        glScalef(size, size, 1)
        glListBase(self.dbase)
        for c in text:
            glCallList(self.dbase + ord(c))
        # glCallLists(text)
        glPopMatrix()

    def width(self, text, size):
        s = 0
        for c in text:
            s += self.ws[ord(c)]+self.space
        return size*(s-self.space)
