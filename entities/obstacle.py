import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=80, color=(0, 0, 255)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
