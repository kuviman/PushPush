
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

from menuitem import *

class MButton(MenuItem):
    size = 25
    fontsize = 10
    idlecolor = (0, 0, 0)
    activecolor = (1, 0, 0)

    def __init__(self, label, func):
        MenuItem.__init__(self)
        self.label = label
        self.func = func
        self.color = self.idlecolor
        self.pressed = False

    def onRender(self, draw):
        draw.color(*self.color)
        dy = 5 if self.pressed else 0
        draw.text(self.label, (0, self.pos+dy), self.fontsize)

    def onPress(self, x):
        self.pressed = True

    def onRelease(self):
        self.pressed = False
        apply(self.func)

    def onFocus(self, gain):
        self.color = self.activecolor if gain else self.idlecolor
