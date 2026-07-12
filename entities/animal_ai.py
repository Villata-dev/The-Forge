class FleeState:
    def update(self, dist_to_player): return "FLEE" if dist_to_player < 200 else "GRAZE"
