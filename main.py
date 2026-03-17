import pygame
import sys
from player import Player

def main():
    # Pygame initialization
    pygame.init()

    # Screen configuration
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Forge")

    # Clock configuration
    clock = pygame.time.Clock()
    fps = 60

    # Initialize Player
    player = Player(screen_width // 2, screen_height // 2)

    running = True
    while running:
        # Delta time in seconds
        dt = clock.tick(fps) / 1000.0

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        player.update(dt)

        # Rendering
        screen.fill((0, 0, 0))  # Black background
        player.draw(screen)

        # Refresh screen
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
