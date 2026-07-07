class TrapSystem:
    def __init__(self):
        self.active_traps = []

    def trigger_trap(self, trap_id: str, target_entity):
        # Aplica dano y efectos de estado instantaneos
        target_entity.take_damage(50)
        target_entity.apply_status("Bleeding", duration=5.0)
