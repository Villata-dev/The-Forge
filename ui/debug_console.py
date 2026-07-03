import pygame
from core.settings import WINDOW_WIDTH

class DebugConsole:
    def __init__(self, font):
        self.font = font
        self.logs = []
        self.visible = False

    def log(self, message: str):
        self.logs.append(message)
        if len(self.logs) > 10:
            self.logs.pop(0)

    def draw(self, surface):
        if not self.visible: return
        
        bg = pygame.Surface((WINDOW_WIDTH, 200))
        bg.set_alpha(150)
        bg.fill((0, 0, 0))
        surface.blit(bg, (0, 0))
        
        for i, msg in enumerate(self.logs):
            text = self.font.render(msg, True, (0, 255, 0))
            surface.blit(text, (10, 10 + i * 18))
