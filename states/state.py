from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
