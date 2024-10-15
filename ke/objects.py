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
