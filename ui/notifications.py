import pygame
from core.settings import COLOR_TEXT

class NotificationHUD:
    def __init__(self, font):
        self.font = font
        self.messages = []

    def push(self, text: str):
        self.messages.append({"text": text, "timer": 180}) # 3 segundos a 60 FPS

    def render(self, surface):
        y_offset = 20
        for msg in self.messages[:]:
            alpha = min(255, msg['timer'] * 3)
            surf = self.font.render(msg['text'], True, COLOR_TEXT)
            surf.set_alpha(alpha)
            surface.blit(surf, (20, y_offset))
            y_offset += 30
            
            msg['timer'] -= 1
            if msg['timer'] <= 0:
                self.messages.remove(msg)
