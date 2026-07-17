import pygame
import sys
from core.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from states.game_state import GameState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("The Forge - Dev Build")
        self.clock = pygame.time.Clock()
        self.game_state = GameState()

    def run(self):
        while True:
            # Delta time para independizar el movimiento de los FPS
            dt = self.clock.tick(FPS) / 1000.0 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Bucle principal
            self.game_state.update(dt)
            self.game_state.draw(self.screen)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
