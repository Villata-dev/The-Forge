import pygame
from core.settings import COLOR_UI_PANEL, COLOR_TEXT

class HUD:
    def __init__(self, surface):
        self.display_surface = surface
        self.font = pygame.font.SysFont(None, 28)

    def draw_bar(self, current, max_val, bg_rect, color):
        pygame.draw.rect(self.display_surface, COLOR_UI_PANEL, bg_rect)
        ratio = current / max_val
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        pygame.draw.rect(self.display_surface, color, current_rect)
