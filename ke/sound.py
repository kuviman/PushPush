import pygame

class Sound:
    volume = 1

    @staticmethod
    def set_volume(vol):
        Sound.volume = vol
    
    def __init__(self, path):
        self.snd = pygame.mixer.Sound(path)

    def play(self):
        self.snd.set_volume(Sound.volume)
        self.snd.play()
