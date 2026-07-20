import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, groups, name):
        super().__init__(groups)
        self.image = pygame.Surface((64, 64))
        self.image.fill((50, 50, 200)) # Azul para NPCs
        self.rect = self.image.get_rect(topleft=pos)
        self.name = name
        self.interaction_radius = 100
