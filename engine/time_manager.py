class TimeSystem:
    def __init__(self, day_length_seconds: int = 600):
        self.day_length = day_length_seconds
        self.current_time = 0.0  # 0 to 1 (0 = medianoche, 0.5 = mediodia)

    def tick(self, dt: float):
        self.current_time += dt / self.day_length
        if self.current_time >= 1.0:
            self.current_time = 0.0

    def get_ambient_tint(self) -> tuple:
        """Devuelve un valor RGB para oscurecer la pantalla de noche"""
        if 0.2 < self.current_time < 0.8:
            return (255, 255, 255) # Dia claro
        elif self.current_time <= 0.2 or self.current_time >= 0.8:
            return (50, 50, 100) # Noche azulada
        return (150, 100, 100) # Amanecer/Atardecer
