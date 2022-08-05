import os
import pygame
import save_settings as save
pygame.init()
class sound:
    def __init__(self,sound = None, volume = None):
        self.SOUND_NAME = sound
        self.VOLUME = volume
        self.SOUND = None
    def load(self):
        sound_load = save.path()
        sound_load = os.path.join(sound_load, self.SOUND_NAME)
        self.SOUND = pygame.mixer.Sound(self.SOUND_NAME)
        pygame.mixer.Sound.set_volume(self.SOUND,self.VOLUME)
    def play(self):
        self.SOUND = pygame.mixer.Sound.play(self.SOUND)
class music:
    def __init__(self,music = None):
        self.MUSIC_NAME = music
        self.MUSIC = None
    def load(self):
        music_load = save.path()
        music_load = os.path.join(music_load, self.MUSIC_NAME)
        self.MUSIC = pygame.mixer.music.load(self.MUSIC_NAME)
    def play(self):
        self.MUSIC = pygame.mixer.music.play()
    def play_loop(self):
        self.MUSIC = pygame.mixer.music.play(loops=-1)
    def stop(self):
        self.MUSIC = pygame.mixer.music.stop()