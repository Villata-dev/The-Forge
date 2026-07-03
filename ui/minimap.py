import pygame
from core.settings import COLOR_UI_PANEL

class Minimap:
    def __init__(self, size: int = 150):
        self.size = size
        self.surface = pygame.Surface((size, size))
        self.surface.set_alpha(200)

    def render(self, screen, player_pos: tuple, enemies: list):
        self.surface.fill(COLOR_UI_PANEL)
        pygame.draw.rect(self.surface, (200, 200, 200), (0,0, self.size, self.size), 2)
        
        # Jugador en el centro (simplificado)
        center = self.size // 2
        pygame.draw.circle(self.surface, (0, 255, 0), (center, center), 4)
        
        screen.blit(self.surface, (screen.get_width() - self.size - 20, 20))
