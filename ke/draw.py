from OpenGL.GL import *
from math import *

class DrawModule:
    def __init__(self, app):
        self.app = app
        self.reload()

    def reload(self):
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.build_quad()

    def build_quad(self):
        self.quad = glGenLists(1)
        glNewList(self.quad, GL_COMPILE)
        glBegin(GL_QUADS)
        glTexCoord2i(0, 0)
        glVertex2i(-1, -1)
        glTexCoord2i(1, 0)
        glVertex2i(+1, -1)
        glTexCoord2i(1, 1)
        glVertex2i(+1, +1)
        glTexCoord2i(0, 1)
        glVertex2i(-1, +1)
        glEnd()
        glEndList()

    def clear(self, r=1, g=1, b=1):
        glClearColor(r, g, b, 1)
        glClear(GL_COLOR_BUFFER_BIT)

    def flat(self, h=None, align=(0, 0)):
        if h is None:
            h = self.app.get_size()[1]
        h /= 2.0
        w = h*self.app.aspect()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-w, w, h, -h, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        ax, ay = align
        glTranslatef(w*ax, h*ay, 0)
        return w*2

    def notex(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def point(self, p, size=1):
        x, y = p
        self.notex()
        glPushMatrix()
        glTranslatef(x, y, 0)
        glScalef(size, size, 1)
        glCallList(self.quad)
        glPopMatrix()

    def translate(self, dx, dy):
        glTranslatef(dx, dy, 0)

    def scale(self, sx, sy=None):
        if sy is None:
            sy = sx
        glScalef(sx, sy, 1)

    def rotate(self, a):
        glRotatef(degrees(a), 0, 0, 1)

    def color(self, r, g, b, a=1):
        glColor4f(r, g, b, a)

    def image(self, im, pos, rot=0, align=(0, 0)):
        x, y = pos
        w, h = im.size
        glPushMatrix()
        glTranslatef(x, y, 0)
        glRotatef(degrees(rot), 0, 0, 1)
        glScalef(w, h, 1)
        ax, ay = align
        glTranslatef(-ax, -ay, 0)
        glBindTexture(GL_TEXTURE_2D, im.tex)
        glCallList(self.quad)
        glPopMatrix()

    def rect(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        self.notex()
        glPushMatrix()
        glTranslatef((x1+x2)/2.0, (y1+y2)/2.0, 0)
        glScalef(abs(x1-x2)/2.0, abs(y1-y2)/2.0, 1)
        glCallList(self.quad)
        glPopMatrix()

    def text(self, text, pos, size, align=(0, 0)):
        self.font.render(text, pos, size, align)

    def text_width(self, text, size):
        return self.font.width(text, size)
