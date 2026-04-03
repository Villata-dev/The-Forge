class StateManager:
    """Manages the stack of game states.

    The StateManager handles pushing, popping, and changing states,
    and delegates event handling, updates, and drawing to the active state.

    Attributes:
        states (list[State]): A stack of active game states.
    """

    def __init__(self):
        """Initializes the StateManager with an empty stack of states."""
        self.states = []

    def push(self, state):
        """Pushes a new state onto the stack.

        Args:
            state (State): The state to push onto the stack.
        """
        self.states.append(state)

    def pop(self):
        """Pops the top state from the stack.

        Returns:
            State: The state that was popped, or None if the stack was empty.
        """
        if self.states:
            return self.states.pop()
        return None

    def change(self, state):
        """Replaces the top state on the stack with a new state.

        Args:
            state (State): The new state to replace the current top state.
        """
        self.pop()
        self.push(state)

    def handle_events(self, events):
        """Delegates event handling to the active state at the top of the stack.

        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process.
        """
        if self.states:
            self.states[-1].handle_events(events)

    def update(self, dt):
        """Delegates logic update to the active state at the top of the stack.

        Args:
            dt (float): The time passed since the last frame in seconds.
        """
        if self.states:
            self.states[-1].update(dt)

    def draw(self, surface):
        """Delegates rendering to the active state at the top of the stack.

        Args:
            surface (pygame.Surface): The surface to draw the state on.
        """
        if self.states:
            self.states[-1].draw(surface)
