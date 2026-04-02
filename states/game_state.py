import pygame
from states.state import State
from entities.player import Player
from entities.camera_group import CameraGroup
from entities.obstacle import Obstacle

class GameState(State):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = (0, 100, 0)  # Dark Green for Gameplay

        # Initialize camera group
        self.all_sprites = CameraGroup()

        # Initialize player and add to group
        self.player = Player(400, 300)
        self.all_sprites.add(self.player)

        # Add some obstacles for Y-Sorting testing
        # Some are placed relative to the player's initial position
        obstacles_data = [
            (300, 200, 60, 100, (0, 0, 200)),  # Top-left from player
            (500, 350, 80, 60, (0, 50, 150)),  # Bottom-right from player
            (400, 150, 50, 50, (20, 20, 100)), # Directly above player's initial pos
            (200, 500, 100, 100, (0, 0, 180)), # Bottom-left
            (600, 100, 40, 40, (10, 10, 80))   # Top-right
        ]

        for x, y, w, h, color in obstacles_data:
            obstacle = Obstacle(x, y, w, h, color)
            self.all_sprites.add(obstacle)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.pop()

    def update(self, dt):
        self.all_sprites.update(dt)

    def draw(self, surface):
        surface.fill(self.bg_color)

        # Draw all sprites with camera offset and Y-sorting
        self.all_sprites.draw(surface, self.player)

        # Stamina UI (Keep it fixed on screen)
        ui_x, ui_y = 20, 20
        ui_width, ui_height = 200, 20
        # Background bar
        pygame.draw.rect(surface, (50, 50, 50), (ui_x, ui_y, ui_width, ui_height))
        # Current stamina bar
        stamina_ratio = self.player.stamina_actual / self.player.stamina_max
        current_width = int(ui_width * stamina_ratio)
        pygame.draw.rect(surface, (0, 200, 255), (ui_x, ui_y, current_width, ui_height))
