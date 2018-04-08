
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

class MLabel(MenuItem):
    clickable = False
    size = 20
    fontsize = 7
    color = (0.3, 0.3, 0.3)

    def __init__(self, label):
        MenuItem.__init__(self)
        self.label = label

    def onRender(self, draw):
        draw.color(*self.color)
        draw.text(self.label, (0, self.pos), self.fontsize)
