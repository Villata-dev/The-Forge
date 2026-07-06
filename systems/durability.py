class DurabilitySystem:
    def __init__(self, max_health: float = 100.0):
        self.max_health = max_health
        self.current_health = max_health
        self.broken = False

    def take_damage(self, amount: float):
        if self.broken: return
        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            self.broken = True

    def repair(self, amount: float):
        self.current_health = min(self.max_health, self.current_health + amount)
        if self.current_health > 0:
            self.broken = False
