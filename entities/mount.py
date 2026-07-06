class Mount:
    def __init__(self, name: str, speed_multiplier: float, stamina: float):
        self.name = name
        self.speed_multiplier = speed_multiplier
        self.max_stamina = stamina
        self.current_stamina = stamina
        self.is_mounted = False

    def mount_up(self) -> float:
        self.is_mounted = True
        return self.speed_multiplier

    def dismount(self) -> float:
        self.is_mounted = False
        return 1.0 # Velocidad base del jugador
