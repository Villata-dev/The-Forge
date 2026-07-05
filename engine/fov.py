import math

class FieldOfView:
    @staticmethod
    def is_in_sight(observer_pos: tuple, observer_angle: float, target_pos: tuple, fov_angle: float = 90.0, max_dist: float = 300.0) -> bool:
        dx = target_pos[0] - observer_pos[0]
        dy = target_pos[1] - observer_pos[1]
        
        distance = math.hypot(dx, dy)
        if distance > max_dist: return False
        
        angle_to_target = math.degrees(math.atan2(dy, dx))
        angle_diff = (angle_to_target - observer_angle + 180) % 360 - 180
        
        return abs(angle_diff) <= fov_angle / 2.0
