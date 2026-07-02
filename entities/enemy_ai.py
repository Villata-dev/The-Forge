import math

class EnemyAI:
    def __init__(self, patrol_radius: float, aggro_range: float):
        self.state = "IDLE"
        self.patrol_radius = patrol_radius
        self.aggro_range = aggro_range

    def update(self, self_pos: tuple, player_pos: tuple):
        dist = math.hypot(player_pos[0] - self_pos[0], player_pos[1] - self_pos[1])
        
        if dist < self.aggro_range:
            self.state = "CHASE"
        elif dist > self.aggro_range * 1.5:
            self.state = "RETURN"
        else:
            if self.state != "CHASE":
                self.state = "PATROL"
        
        return self.state
