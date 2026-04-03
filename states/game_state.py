import pygame
from states.state import State
from entities.player import Player
from entities.camera_group import CameraGroup
from entities.obstacle import Obstacle

class GameState(State):
    """Represents the main gameplay state.

    This state handles game logic, entity updates, camera management,
    and rendering of the game world and UI.

    Attributes:
        bg_color (tuple[int, int, int]): Background color for the gameplay state.
        all_sprites (CameraGroup): A sprite group with camera and sorting functionality.
        obstacle_sprites (pygame.sprite.Group): A group containing all obstacle sprites.
        player (Player): The player entity instance.
    """

    def __init__(self, manager):
        """Initializes the GameState.

        Args:
            manager (StateManager): The state manager that controls this state.
        """
        super().__init__(manager)
        self.bg_color = (0, 100, 0)  # Dark Green for Gameplay

        # Initialize camera group
        self.all_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Initialize player and add to group
        self.player = Player(400, 300, self.obstacle_sprites)
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
            Obstacle([self.all_sprites, self.obstacle_sprites], x, y, w, h, color)

    def handle_events(self, events):
        """Handles gameplay events such as movement and combat.

        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.pop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    self.player.attack(self.all_sprites)

    def update(self, dt):
        """Updates all game entities and logic.

        Args:
            dt (float): The time passed since the last frame in seconds.
        """
        self.all_sprites.update(dt)

    def draw(self, surface):
        """Renders the game world and UI.

        Args:
            surface (pygame.Surface): The surface to draw the state on.
        """
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
