from .app import App
from .image import Image
from .state import shutdown, State
from .menu import *
from .sound import Sound
from .objects import Object, Group

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
