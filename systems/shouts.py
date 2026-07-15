class ShoutSystem:
    def __init__(self):
        self.cooldown = 0.0
    def use_shout(self, power_id: str) -> bool:
        if self.cooldown <= 0:
            self.cooldown = 45.0 # Segundos de recarga
            return True
        return False
