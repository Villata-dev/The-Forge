import pygame

class CameraGroup(pygame.sprite.Group):
    """A sprite group that handles camera movement and Y-sorting for rendering.

    Inherits from pygame.sprite.Group and overrides the draw method to apply
    a camera offset based on a target sprite and sort sprites by their Y-coordinate.
    """

    def __init__(self):
        """Initializes the CameraGroup."""
        super().__init__()

    def get_offset(self, surface, target_sprite):
        """Calculates the camera offset to center the target sprite on the surface.

        Args:
            surface (pygame.Surface): The surface where the game is being drawn.
            target_sprite (pygame.sprite.Sprite): The sprite to center the camera on.

        Returns:
            pygame.math.Vector2: The calculated camera offset.
        """
        screen_center = pygame.math.Vector2(surface.get_width() // 2, surface.get_height() // 2)
        return screen_center - pygame.math.Vector2(target_sprite.rect.center)

    def draw(self, surface, target_sprite):
        """Renders all sprites in the group with a camera offset and Y-sorting.

        Args:
            surface (pygame.Surface): The surface to draw the sprites on.
            target_sprite (pygame.sprite.Sprite): The sprite to center the camera on.
        """
        # Calculate offset using the helper method
        offset = self.get_offset(surface, target_sprite)

        # Sort sprites by their Y-coordinate (centery) for Y-Sort (pseudo-depth)
        # We use a custom sort to ensure sprites with higher Y are drawn later (on top)
        sorted_sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)

        # Render each sprite with the calculated offset
        for sprite in sorted_sprites:
            offset_pos = sprite.rect.topleft + offset
            surface.blit(sprite.image, offset_pos)
