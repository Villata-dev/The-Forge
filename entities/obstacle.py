import pygame

class Obstacle(pygame.sprite.Sprite):
    """A static environmental obstacle that blocks player movement.

    Attributes:
        image (pygame.Surface): Visual representation of the obstacle.
        rect (pygame.Rect): Rectangular area of the obstacle sprite.
        hitbox (pygame.Rect): Collision area of the obstacle.
    """

    def __init__(self, groups, x, y, width=50, height=80, color=(0, 0, 255)):
        """Initializes an obstacle with a specific size and color.

        Args:
            groups (list[pygame.sprite.Group]): Sprite groups to add the obstacle to.
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
            width (int): Width of the obstacle. Defaults to 50.
            height (int): Height of the obstacle. Defaults to 80.
            color (tuple[int, int, int]): RGB color of the obstacle. Defaults to blue (0, 0, 255).
        """
        super().__init__(groups)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = self.rect.copy()
