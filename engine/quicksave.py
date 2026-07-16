import pygame
class QuickStateManager:
    def handle_hotkeys(self, event):
        if event.key == pygame.K_F5: self.save()
        if event.key == pygame.K_F9: self.load()
