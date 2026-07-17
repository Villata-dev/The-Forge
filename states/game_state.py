import pygame
from entities.player import Player

class GameState:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.player = Player(600, 350)
        self.bg_color = (25, 45, 25) # Verde bosque oscuro

    def update(self, dt):
        self.player.update(dt)

    def draw(self, surface):
        # Limpiar pantalla con el color de fondo
        surface.fill(self.bg_color)
        
        # Dibujar al jugador
        self.player.draw(surface)
        
        # Renderizar HUD basico
        pygame.draw.rect(surface, (45, 45, 55), (20, 20, 250, 40), border_radius=5)
        pygame.draw.rect(surface, (200, 50, 50), (25, 25, 240, 30), border_radius=5) # Barra de vida
