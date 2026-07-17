import pygame
class CombatBoxes:
    def __init__(self, x, y, width, height):
        self.hurtbox = pygame.Rect(x, y, width, height)
        self.hitbox = pygame.Rect(x, y, width + 20, height + 20)
