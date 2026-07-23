import pygame
class AmbientTint:
    def get_tint_color(self, time_of_day):
        if time_of_day < 6 or time_of_day > 20: return (10, 10, 30, 150) # Noche
        if 18 <= time_of_day <= 20: return (200, 100, 50, 50) # Atardecer
        return (255, 255, 255, 0) # Mediodia
