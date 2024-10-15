
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

import pickle, os

class Settings:
    dict = {
        'size': None,
        'fullscreen': True,
        'exitconfirm': True,
        'music': 0.5,
        'sfx': 0.75,
        'mute': False,
        'progress': {}}

    def __init__(self, path):
        self.path = path
        if os.path.isfile(path):
            self.reload()
        else:
            print("using standart settings")
            self.save()

    def reload(self):
        print("settings loaded from", self.path)
        self.dict = pickle.load(open(self.path, "rb"))
    def save(self):
        pickle.dump(self.dict, open(self.path, "wb"))
    def __getitem__(self, key):
        return self.dict[key]
    def __setitem__(self, key, val):
        self.dict[key] = val
        self.save()
    def set(self, key, val):
        self.__setitem__(key, val)
    def get(self, key):
        return self.__getitem__(key)
