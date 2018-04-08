
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

class MTitle(MenuItem):
    clickable = False
    size = 50
    fontsize = 24
    color = (1, 0.5, 0)

    def __init__(self, title):
        MenuItem.__init__(self)
        self.title = title

    def onRender(self, draw):
        draw.color(*self.color)
        draw.text(self.title, (0, self.pos), self.fontsize)
