import math

class LevelingSystem:
    def __init__(self, base_xp: int = 100):
        self.level = 1
        self.current_xp = 0
        self.base_xp = base_xp
        self.stat_points = 0

    def get_xp_for_next_level(self) -> int:
        # Curva de experiencia exponencial (estilo RPG clasico)
        return int(self.base_xp * math.pow(self.level, 1.5))

    def add_xp(self, amount: int) -> bool:
        self.current_xp += amount
        leveled_up = False
        while self.current_xp >= self.get_xp_for_next_level():
            self.current_xp -= self.get_xp_for_next_level()
            self.level += 1
            self.stat_points += 3
            leveled_up = True
        return leveled_up
