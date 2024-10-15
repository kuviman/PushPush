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
