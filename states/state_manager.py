class StateManager:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        if self.states:
            return self.states.pop()
        return None

    def change(self, state):
        self.pop()
        self.push(state)

    def handle_events(self, events):
        if self.states:
            self.states[-1].handle_events(events)

    def update(self, dt):
        if self.states:
            self.states[-1].update(dt)

    def draw(self, surface):
        if self.states:
            self.states[-1].draw(surface)
