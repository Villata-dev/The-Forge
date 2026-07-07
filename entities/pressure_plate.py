class PressurePlate:
    def __init__(self, linked_door_id: str):
        self.is_pressed = False
        self.linked_door_id = linked_door_id

    def on_step(self, weight: float) -> bool:
        if weight > 15.0 and not self.is_pressed:
            self.is_pressed = True
            return True
        return False
