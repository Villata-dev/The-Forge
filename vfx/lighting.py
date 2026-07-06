import pygame

class LightingEngine:
    def __init__(self, width: int, height: int):
        self.fog = pygame.Surface((width, height))
        self.fog.fill((10, 10, 15)) # Oscuridad base

    def render_light_source(self, surface, pos: tuple, radius: int):
        light = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(light, (255, 255, 255, 50), (radius, radius), radius)
        surface.blit(light, (pos[0] - radius, pos[1] - radius), special_flags=pygame.BLEND_RGBA_ADD)
