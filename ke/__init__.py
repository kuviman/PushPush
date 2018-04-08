
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

from app import App
from image import Image
from state import shutdown, State
from menu import *
from sound import Sound
from objects import Object, Group

if __name__ == "__main__":
    class Test(State):
        def __init__(self, app):
            State.__init__(self, app)
            self.img = Image("test.jpg", (200, 200))
            self.app.load_font("font.tga")
            self.a = 0
        def onUpdate(self, dt):
            self.a += dt
        def onRender(self, draw):
            draw.clear(0, 0, 0)
            draw.flat()
            draw.color(1, 1, 1)
            draw.image(self.img, (0, 0), self.a, align=(-1, 1))
            draw.color(1, 0, 0)
            draw.point((0, 0), 3)
            draw.flat(100, align=(-1, -1))
            draw.color(1, 1, 1)
            draw.text("hello, world!", (10, 10), 2, align=(-1, -1))
        def onKeyUp(self, key):
            if key == K_SPACE:
                self.app.resize(self.app.list_modes()[0], fullscreen=True)
    try:
        app = App()
        menu = Menu(app)
        test = Test(app)
        menu.add_title("kEngine")
        menu.add_label("by kuviman")
        menu.add_separator()
        menu.add_button("run test", test.run)
        menu.run()
    except shutdown:
        pass
    finally:
        app.close()
