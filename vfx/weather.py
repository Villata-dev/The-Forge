import pygame
import random
from core.settings import WINDOW_WIDTH, WINDOW_HEIGHT

class WeatherSystem:
    def __init__(self):
        self.raindrops = []

    def update_rain(self, surface):
        # Generar nuevas gotas
        if random.random() < 0.3:
            x = random.randint(0, WINDOW_WIDTH)
            self.raindrops.append([x, -10])

        # Actualizar y dibujar
        for drop in self.raindrops[:]:
            drop[1] += 15 # Velocidad de caida rapida
            drop[0] += 2  # Viento ligero
            pygame.draw.line(surface, (150, 150, 200), (drop[0], drop[1]), (drop[0] + 2, drop[1] + 10), 1)
            
            if drop[1] > WINDOW_HEIGHT:
                self.raindrops.remove(drop)
