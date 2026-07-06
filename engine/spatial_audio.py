import math

class SpatialAudio:
    def __init__(self, max_distance: float = 500.0):
        self.max_distance = max_distance

    def calculate_volume(self, player_pos: tuple, sound_pos: tuple) -> float:
        dist = math.hypot(sound_pos[0] - player_pos[0], sound_pos[1] - player_pos[1])
        if dist > self.max_distance:
            return 0.0
        return 1.0 - (dist / self.max_distance)
