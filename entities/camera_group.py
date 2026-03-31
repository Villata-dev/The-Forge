import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, surface, target_sprite):
        # Calculate offset: screen_center - target_position
        # This keeps the target_sprite in the middle of the screen
        screen_center = pygame.math.Vector2(surface.get_width() // 2, surface.get_height() // 2)
        offset = screen_center - pygame.math.Vector2(target_sprite.rect.center)

        # Sort sprites by their Y-coordinate (centery) for Y-Sort (pseudo-depth)
        # We use a custom sort to ensure sprites with higher Y are drawn later (on top)
        sorted_sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)

        # Render each sprite with the calculated offset
        for sprite in sorted_sprites:
            offset_pos = sprite.rect.topleft + offset
            surface.blit(sprite.image, offset_pos)
