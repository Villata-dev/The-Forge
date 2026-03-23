import pygame
import sys
from states.state_manager import StateManager
from states.menu_state import MenuState

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

    # Initialize State Manager
    state_manager = StateManager()
    state_manager.push(MenuState(state_manager))

    running = True
    while running:
        # Delta time in seconds
        dt = clock.tick(fps) / 1000.0

        # Event handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        state_manager.handle_events(events)

        # Update
        state_manager.update(dt)

        # Rendering
        state_manager.draw(screen)

        # Refresh screen
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
