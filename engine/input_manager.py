import pygame

class InputManager:
    def __init__(self):
        self.bindings = {
            "MOVE_UP": pygame.K_w,
            "MOVE_DOWN": pygame.K_s,
            "MOVE_LEFT": pygame.K_a,
            "MOVE_RIGHT": pygame.K_d,
            "ATTACK": pygame.K_SPACE,
            "INVENTORY": pygame.K_i
        }
        self.state = {action: False for action in self.bindings}

    def handle_event(self, event):
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            is_pressed = event.type == pygame.KEYDOWN
            for action, key in self.bindings.items():
                if event.key == key:
                    self.state[action] = is_pressed
