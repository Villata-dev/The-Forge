class BossFSM:
    def __init__(self, hp_thresholds: list):
        self.phases = hp_thresholds # ej. [75.0, 50.0, 25.0]
        self.current_phase = 1

    def update_phase(self, current_hp_percentage: float):
        if self.phases and current_hp_percentage <= self.phases[0]:
            self.phases.pop(0)
            self.current_phase += 1
            return True # Trigger phase change animation
        return False
