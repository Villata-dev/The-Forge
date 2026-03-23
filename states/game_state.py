import pygame
from states.state import State

class GameState(State):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = (0, 100, 0)  # Dark Green for Gameplay

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.pop()

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(self.bg_color)
