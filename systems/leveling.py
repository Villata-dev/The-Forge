class Progression:
    def __init__(self):
        self.level = 1
        self.xp = 0
    def add_xp(self, amount):
        self.xp += amount
        if self.xp >= self.get_xp_required(): self.level_up()
    def get_xp_required(self): return int(100 * (self.level ** 1.5))
    def level_up(self): self.level += 1
