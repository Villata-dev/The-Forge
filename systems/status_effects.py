class StatusEffects:
    def __init__(self):
        self.active_effects = []

    def apply_effect(self, name: str, duration: float, tick_damage: int = 0):
        self.active_effects.append({
            "name": name,
            "timer": duration,
            "tick_damage": tick_damage
        })

    def update(self, dt: float) -> int:
        total_damage = 0
        for effect in self.active_effects[:]:
            effect["timer"] -= dt
            total_damage += effect["tick_damage"]
            
            if effect["timer"] <= 0:
                self.active_effects.remove(effect)
        return total_damage
