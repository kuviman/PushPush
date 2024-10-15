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
