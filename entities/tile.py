import pygame

class Tile(pygame.sprite.Sprite):
    """A sprite representing a single tile from the map, used for Y-sorting.

    Attributes:
        image (pygame.Surface): The tile's graphic.
        rect (pygame.Rect): The tile's position and size.
    """

    def __init__(self, pos, surface, groups):
        """Initializes the Tile.

        Args:
            pos (tuple[int, int]): The top-left position of the tile in world coordinates.
            surface (pygame.Surface): The tile's image.
            groups (list[pygame.sprite.Group]): The sprite groups to add the tile to.
        """
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
