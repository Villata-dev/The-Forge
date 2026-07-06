import math

class FastTravelSystem:
    @staticmethod
    def can_travel(enemies_nearby: bool, overencumbered: bool) -> dict:
        if enemies_nearby:
            return {"allowed": False, "reason": "No puedes viajar con enemigos cerca."}
        if overencumbered:
            return {"allowed": False, "reason": "Llevas demasiado peso para viajar."}
        return {"allowed": True, "reason": "Viaje seguro."}

    @staticmethod
    def calculate_travel_time(start_pos: tuple, end_pos: tuple, speed: float) -> float:
        # Devuelve el tiempo simulado (en horas) que toma el viaje
        distance = math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        return distance / speed
