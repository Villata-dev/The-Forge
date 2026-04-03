import pygame
from states.state import State
from states.game_state import GameState

class MenuState(State):
    """Represents the initial menu state.

    Attributes:
        bg_color (tuple[int, int, int]): Background color for the menu state.
    """

    def __init__(self, manager):
        """Initializes the MenuState.

        Args:
            manager (StateManager): The state manager that controls this state.
        """
        super().__init__(manager)
        self.bg_color = (30, 30, 30)  # Dark Gray for Menu

    def handle_events(self, events):
        """Handles menu navigation and selection events.

        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.manager.push(GameState(self.manager))

    def update(self, dt):
        """Updates menu logic.

        Args:
            dt (float): The time passed since the last frame in seconds.
        """
        pass

    def draw(self, surface):
        """Renders the menu to the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the state on.
        """
        surface.fill(self.bg_color)
