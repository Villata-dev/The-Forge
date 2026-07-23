class DayNightCycle:
    def __init__(self, time_scale=60.0):
        self.time_of_day = 8.0 # Comienza a las 8 AM
        self.time_scale = time_scale # 1 segundo real = 60 segundos in-game
    def update(self, dt):
        self.time_of_day += (dt * self.time_scale) / 3600.0
        if self.time_of_day >= 24.0: self.time_of_day -= 24.0
