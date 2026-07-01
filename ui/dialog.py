import pygame
from core.settings import COLOR_UI_PANEL, COLOR_TEXT, WINDOW_WIDTH, WINDOW_HEIGHT

class DialogBox:
    def __init__(self, font):
        self.font = font
        self.rect = pygame.Rect(100, WINDOW_HEIGHT - 150, WINDOW_WIDTH - 200, 100)

    def draw(self, surface, text: str, speaker_name: str):
        pygame.draw.rect(surface, COLOR_UI_PANEL, self.rect, border_radius=5)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2, border_radius=5)
        
        name_surf = self.font.render(speaker_name, True, (255, 200, 50))
        text_surf = self.font.render(text, True, COLOR_TEXT)
        
        surface.blit(name_surf, (self.rect.x + 20, self.rect.y + 15))
        surface.blit(text_surf, (self.rect.x + 20, self.rect.y + 50))
