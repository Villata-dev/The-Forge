import pygame
from core.settings import COLOR_UI_PANEL, COLOR_TEXT

class Tooltip:
    def __init__(self, font):
        self.font = font

    def render(self, surface, text: str, pos: tuple):
        text_surf = self.font.render(text, True, COLOR_TEXT)
        rect = text_surf.get_rect(topleft=(pos[0] + 15, pos[1] + 15))
        
        # Draw background
        bg_rect = rect.inflate(10, 10)
        pygame.draw.rect(surface, COLOR_UI_PANEL, bg_rect)
        pygame.draw.rect(surface, (200, 200, 200), bg_rect, 1) # Border
        
        surface.blit(text_surf, rect)
