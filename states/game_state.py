import pygame
import pytmx
from states.state import State
from entities.player import Player
from entities.camera_group import CameraGroup
from entities.obstacle import Obstacle
from engine.map_loader import TiledMap
from entities.tile import Tile

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

        # Load Map
        self.map = TiledMap("assets/maps/test_map.tmx")

        # Initialize player and add to group
        self.player = Player(400, 300, self.obstacle_sprites)
        self.all_sprites.add(self.player)

        # Process Map Layers for Y-Sort (Objetos)
        for layer in self.map.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer) and "Objetos" in layer.name:
                for x, y, gid in layer:
                    tile_image = self.map.tmx_data.get_tile_image_by_gid(gid)
                    if tile_image:
                        pos = (x * self.map.tmx_data.tilewidth, y * self.map.tmx_data.tileheight)
                        Tile(pos, tile_image, [self.all_sprites])

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

        # Update map offset
        offset = self.all_sprites.get_offset(surface, self.player)
        self.map.offset = offset

        # Draw Background Layers (e.g., Suelo)
        self.map.render(surface, layer_type="Suelo")

        # Draw all sprites with camera offset and Y-sorting (Player, Obstacles, Objetos)
        self.all_sprites.draw(surface, self.player)

        # Draw Foreground Layers
        self.map.render(surface, layer_type="Foreground")

        # Stamina UI (Keep it fixed on screen)
        ui_x, ui_y = 20, 20
        ui_width, ui_height = 200, 20
        # Background bar
        pygame.draw.rect(surface, (50, 50, 50), (ui_x, ui_y, ui_width, ui_height))
        # Current stamina bar
        stamina_ratio = self.player.stamina_actual / self.player.stamina_max
        current_width = int(ui_width * stamina_ratio)
        pygame.draw.rect(surface, (0, 200, 255), (ui_x, ui_y, current_width, ui_height))
