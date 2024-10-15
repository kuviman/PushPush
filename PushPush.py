
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

import ke, ppgame, sys, traceback
# sys.stdout = open("log.txt", "w")
# sys.stderr = open("error.txt", "w")

# app = ke.App()
# class Test(ke.State):
#     def onRender(self, draw):
#         draw.clear()
#         draw.color(0, 0, 0)
#         # draw.rect((0, 0), (0.5, 1.0))
#         draw.text("hi", (0, 0), 0.1)
# app.load_font("data/font.tga")
# Test(app).run()

try:
    print("hi?")
    ppgame.run()
except ke.shutdown:
    print("app was closed")
