import pygame
from states.state import State
from entities.player import Player

class GameState(State):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = (0, 100, 0)  # Dark Green for Gameplay
        # Initialize player at center of the screen
        self.player = Player(400, 300)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.pop()

    def update(self, dt):
        self.player.update(dt)

    def draw(self, surface):
        surface.fill(self.bg_color)
        self.player.draw(surface)

        # Stamina UI
        ui_x, ui_y = 20, 20
        ui_width, ui_height = 200, 20
        # Background bar
        pygame.draw.rect(surface, (50, 50, 50), (ui_x, ui_y, ui_width, ui_height))
        # Current stamina bar
        stamina_ratio = self.player.stamina_actual / self.player.stamina_max
        current_width = int(ui_width * stamina_ratio)
        pygame.draw.rect(surface, (0, 200, 255), (ui_x, ui_y, current_width, ui_height))
