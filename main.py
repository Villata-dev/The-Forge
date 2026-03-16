import pygame
import sys

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

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update (placeholder for future logic)

        # Rendering
        screen.fill((0, 0, 0))  # Black background

        # Refresh screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
