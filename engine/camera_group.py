import pygame
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
    def custom_draw(self, player):
        # Ordena los sprites por su posicion en Y para efecto de profundidad
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            pass
