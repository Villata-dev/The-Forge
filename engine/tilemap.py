import pygame
class TileMap:
    def __init__(self, width, height, tile_size=64):
        self.tile_size = tile_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
    def draw(self, surface, camera_offset): pass
