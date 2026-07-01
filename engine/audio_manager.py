import pygame
import os

class AudioManager:
    _sounds = {}
    _ambient = None

    @classmethod
    def play_sfx(cls, path: str, volume: float = 1.0):
        if path not in cls._sounds:
            if os.path.exists(path):
                cls._sounds[path] = pygame.mixer.Sound(path)
            else:
                return # Fail silently in headless/dev mode
        cls._sounds[path].set_volume(volume)
        cls._sounds[path].play()

    @classmethod
    def play_music(cls, path: str):
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)
