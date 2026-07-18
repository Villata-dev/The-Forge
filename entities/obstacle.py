import pygame
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.rect = pygame.Rect(pos[0], pos[1], 64, 64)
        self.hitbox = self.rect.inflate(-10, -10)
