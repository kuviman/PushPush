
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

class Object:
    def __init__(self):
        self.alive = True
    def kill(self):
        self.alive = False
        self.onKill()
    def update(self, dt):
        self.onUpdate(dt)
    def render(self, draw):
        self.onRender(draw)

    def onKill(self):
        pass
    def onUpdate(self, dt):
        pass
    def onRender(self, draw):
        pass

class Group:
    def __init__(self):
        self.objects = []
    def __iter__(self):
        for obj in self.objects:
            yield obj
    def __len__(self):
        return len(self.objects)
    def add(self, obj):
        self.objects.append(obj)
    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)
        self.objects = list(filter(
            lambda obj: obj.alive, self.objects))
    def render(self, draw):
        for obj in self.objects:
            obj.render(draw)
