from pytmx.util_pygame import load_pygame
import pygame

class MapLoader:
    def __init__(self, tmx_file):
        self.tmx_data = load_pygame(tmx_file)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight

    def render(self, surface):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight)
                    surface.blit(surf, pos)
