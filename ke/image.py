
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

class Image:
    all = []
    @staticmethod
    def reload_all():
        for image in Image.all:
            image.reload()

    def __init__(self, path, size=None):
        self.path = path
        if size is None:
            self.size = None
        else:
            w, h = size
            self.size = (w/2.0, h/2.0)
        self.reload()
        Image.all.append(self)

    def reload(self):
        im = pygame.image.load(self.path)
        if self.size is None:
            w, h = im.get_size()
            self.size = (w/2.0, h/2.0)
        self.tex = glGenTextures(1)
        w, h = im.get_size()
        glBindTexture(GL_TEXTURE_2D, self.tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, w, h,
            0, GL_RGBA, GL_UNSIGNED_BYTE,
            pygame.image.tostring(im, "RGBA"))

    def free(self):
        glDeleteTextures([self.tex])

