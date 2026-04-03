from abc import ABC, abstractmethod

class State(ABC):
    """Abstract base class for all game states.

    Attributes:
        manager (StateManager): The state manager that controls this state.
    """

    def __init__(self, manager):
        """Initializes the state with a reference to the state manager.

        Args:
            manager (StateManager): The state manager that controls this state.
        """
        self.manager = manager

    @abstractmethod
    def handle_events(self, events):
        """Handles Pygame events for this state.

        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process.
        """
        pass

    @abstractmethod
    def update(self, dt):
        """Updates the state logic.

        Args:
            dt (float): The time passed since the last frame in seconds.
        """
        pass

    @abstractmethod
    def draw(self, surface):
        """Renders the state to the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the state on.
        """
        pass
