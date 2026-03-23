import pygame
from states.state import State
from states.game_state import GameState

class MenuState(State):
    def __init__(self, manager):
        super().__init__(manager)
        self.bg_color = (30, 30, 30)  # Dark Gray for Menu

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.manager.push(GameState(self.manager))

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(self.bg_color)
