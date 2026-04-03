import pygame

class WeaponHitbox(pygame.sprite.Sprite):
    """A temporary sprite representing the area of a player's attack.

    This hitbox has a short lifetime and is used to detect collisions with enemies.

    Attributes:
        direction (pygame.math.Vector2): Direction of the attack.
        image (pygame.Surface): Visual representation (for debugging).
        rect (pygame.Rect): Rectangular area of the hitbox.
        lifetime (float): Duration the hitbox exists in seconds.
        timer (float): Remaining time for the hitbox.
    """

    def __init__(self, player, groups):
        """Initializes the weapon hitbox in front of the player.

        Args:
            player (Player): The player instance performing the attack.
            groups (list[pygame.sprite.Group]): Sprite groups to add the hitbox to.
        """
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
        """Updates the hitbox's lifetime and removes it when expired.

        Args:
            dt (float): The time passed since the last frame in seconds.
        """
        self.timer -= dt
        if self.timer <= 0:
            self.kill()
