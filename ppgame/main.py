
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

import webbrowser
import ke
from settings import *
from editor import *
from game import *
from constants import *
import sys, os, pickle

ICONPATH = None #"data/icon.tga"
FONTPATH = "data/font.tga"
MUSICPATH = "data/music.mp3"

def run():
    print "running", TITLE, "version", VERSION
    settings = Settings("settings.pp")
    app = ke.App(FULL_TITLE, settings['size'],
                 settings['fullscreen'], ICONPATH)
    settings['size'] = app.get_size()
    app.load_font(FONTPATH)

    editor = Editor(app)
    game = Game(app)

    def mute(b):
        settings.set('mute', b)
        if b:
            app.volume(0, 0)
        else:
            app.volume(settings['music'], settings['sfx'])
    mute(settings['mute'])
    app.music(MUSICPATH)

    not_implemented = app.message(
        "sorry\nnot impemented yet", ('back',))

    vm = ke.Menu(app)
    vm.add_title("Volume")
    vm.add_separator()
    def set_music(vol):
        if not settings['mute']:
            app.volume(music=vol)
        settings['music'] = vol
    def_snd = ke.Sound("data/default.wav")
    def set_sfx(vol):
        if not settings['mute']:
            app.volume(sfx=vol)
            def_snd.play()
        settings['sfx'] = vol
    vm.add_scale("music", set_music, settings['music'], True)
    vm.add_scale("SFX", set_sfx, settings['sfx'])
    vm.add_check("mute", mute, settings['mute'])
    vm.add_separator()
    vm.add_button("back", vm.close)

    dm = ke.Menu(app)
    dm.add_title("Display")
    dm.add_separator()
    def resize():
        app.resize(settings['size'], settings['fullscreen'])
    dlist = app.list_modes()
    dm.add_choice("resolution", ["%d x %d"%x for x in dlist],
                  lambda i: settings.set('size', dlist[i]),
                  dlist.index(settings['size']))
    dm.add_check("fullscreen", lambda fs: settings.set('fullscreen', fs),
                 settings['fullscreen'])
    dm.add_separator()
    dm.add_button("apply", resize)
    dm.add_separator()
    dm.add_button("back", dm.close)

    gm = ke.Menu(app)
    gm.add_title("Game")
    gm.add_separator()
    def reset():
        if app.show_message("Are you sure?", ("yes", "no")) == 0:
            settings['progress'] = {}
    gm.add_button("reset progress", reset)
    gm.add_separator()
    gm.add_button("back", gm.close)

    sm = ke.Menu(app)
    sm.add_title("Settings")
    sm.add_separator()
    sm.add_button("display", dm.run)
    sm.add_button("volume", vm.run)
    sm.add_button("game", gm.run)
##    sm.add_check("exit confirmation", lambda ec: settings.set(
##        'exitconfirm', ec))
    sm.add_separator()
    sm.add_button("back", sm.close)

    am = ke.Menu(app)
    am.add_title("About")
    am.add_separator()
    def visit():
        webbrowser.open_new_tab(HOMEPAGE)
        raise ke.shutdown
    am.add_label("%s game"%TITLE)
    am.add_label("version %s"%VERSION)
    am.add_label("released under GNU GPLv3")
    am.add_label(COPYRIGHT)
    am.add_separator()
    am.add_button("visit homepage", visit)
    am.add_button("back", am.close)

    mm = ke.Menu(app)
    mm.add_title(TITLE)
    mm.add_label("version %s"%VERSION)
    mm.add_label("by kuviman")
    mm.add_separator()
    def play():
        lst = [s.split('.')[0] for s in
               filter(lambda s: os.path.splitext(s)[1] == '.ppo',
                     os.listdir("levels"))]
        x = app.choose([s.split('.')[0] for s in lst], "Choose levelset")
        if x == -1:
            return
        if not settings['progress'].has_key(lst[x]):
            settings['progress'][lst[x]] = 0
        levels = pickle.load(open('levels/%s.ppo'%lst[x], 'rb'))
        while True:
            if settings['progress'][lst[x]] == len(levels):
                app.show_message('you have completed all levels')
                break
            game.load("levels/%s/%s.ppl"%(
                lst[x], levels[settings['progress'][lst[x]]]),
                      levels[settings['progress'][lst[x]]])
            game.run()
            if game.success:
                settings['progress'][lst[x]] += 1
                settings.save()
            elif game.success is None:
                break
    def custom():
        lst = filter(lambda s: os.path.isdir("levels/%s"%s),
                     os.listdir("levels"))
        x = app.choose([s.split('.')[0] for s in lst], "Choose levelset")
        if x == -1:
            return
        lst2 = [s.split('.')[0] for s in
                filter(lambda s: os.path.splitext(s)[1] == '.ppl',
                      os.listdir("levels/%s"%lst[x]))]
        y = app.choose(lst2, "Choose level")
        if y == -1:
            return
        while True:
            game.load("levels/%s/%s.ppl"%(lst[x], lst2[y]), lst2[y])
            game.run()
            if game.success != False:
                break
    mm.add_button("play", play)
    mm.add_button("custom level", custom)
    mm.add_button("level editor", editor.run)
    mm.add_button("settings", sm.run)
    mm.add_button("about", am.run)
    mm.add_separator()
    def on_exit():
        if not settings['exitconfirm']:
            mm.close()
            return
        if app.show_message("do you really\nwant to exit?",
                            ('yes', 'no')) == 0:
            mm.close()
    mm.add_button("exit", on_exit)
    mm.run()
