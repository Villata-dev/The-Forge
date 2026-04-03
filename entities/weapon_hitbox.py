import pygame

class WeaponHitbox(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)

        # Attack direction
        self.direction = player.facing_direction.copy()

        # Dimensions and distance from player
        width, height = 40, 40
        distance = 35

        # Setup image for debug visualization (semi-transparent red)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((255, 0, 0, 150))

        # Position the hitbox in front of the player
        pos = player.hitbox.center + self.direction * distance
        self.rect = self.image.get_rect(center=pos)

        # Lifetime in seconds
        self.lifetime = 0.1
        self.timer = self.lifetime

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.kill()
