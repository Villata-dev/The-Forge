class WeightSystem:
    def get_speed_penalty(self, current, max_weight): return 0.5 if current > max_weight else 1.0
