import pygame
import os

class AssetManager:
    _images = {}
    _sounds = {}

    @classmethod
    def get_image(cls, path: str) -> pygame.Surface:
        if path not in cls._images:
            if not os.path.exists(path):
                # Placeholder fallback
                surf = pygame.Surface((64, 64))
                surf.fill((255, 0, 255))
                cls._images[path] = surf
            else:
                cls._images[path] = pygame.image.load(path).convert_alpha()
        return cls._images[path]
