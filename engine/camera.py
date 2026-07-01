import pygame
from core.settings import WINDOW_WIDTH, WINDOW_HEIGHT

class SmoothCamera:
    def __init__(self):
        self.offset = pygame.math.Vector2(0, 0)

    def update(self, target_rect):
        target_x = target_rect.centerx - int(WINDOW_WIDTH / 2)
        target_y = target_rect.centery - int(WINDOW_HEIGHT / 2)
        
        # LERP (Linear Interpolation) para movimiento suave
        self.offset.x += (target_x - self.offset.x) * 0.05
        self.offset.y += (target_y - self.offset.y) * 0.05
