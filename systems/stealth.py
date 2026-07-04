import math

class StealthSystem:
    def __init__(self):
        self.base_visibility = 1.0

    def calculate_detection_chance(self, player_stealth_skill: int, light_level: float, noise_level: float, enemy_perception: int) -> float:
        # La oscuridad reduce la visibilidad, el ruido la aumenta
        visibility = self.base_visibility * light_level + noise_level
        skill_factor = player_stealth_skill / 100.0
        
        chance = (visibility * enemy_perception) - (skill_factor * 50)
        return max(0.0, min(100.0, chance))
