import random

class LockpickingMinigame:
    def __init__(self, difficulty_level: int):
        self.sweet_spot = random.uniform(0, 180) # Angulo de 0 a 180 grados
        # Tolerancia basada en dificultad (1 = facil, 100 = maestro)
        self.tolerance = max(2.0, 30.0 - (difficulty_level * 0.25))
        self.pick_health = 100.0

    def test_angle(self, current_angle: float) -> str:
        distance = abs(self.sweet_spot - current_angle)
        if distance <= self.tolerance:
            return "UNLOCKED"
        elif distance <= self.tolerance * 3:
            self.pick_health -= 15.0
            return "TENSION"
        else:
            self.pick_health -= 35.0
            return "BROKEN" if self.pick_health <= 0 else "LOCKED"
