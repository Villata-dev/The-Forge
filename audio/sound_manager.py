import pygame
class AudioManager:
    def __init__(self):
        pygame.mixer.init(channels=16)
        self.sfx_volume = 0.8
    def play_sfx(self, sound_obj):
        channel = pygame.mixer.find_channel()
        if channel:
            sound_obj.set_volume(self.sfx_volume)
            channel.play(sound_obj)
