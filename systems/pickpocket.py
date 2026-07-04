import random

class PickpocketSystem:
    @staticmethod
    def attempt_theft(stealth_skill: int, item_weight: float, item_value: int) -> dict:
        # Objetos pesados o valiosos son mas dificiles de robar
        difficulty = (item_weight * 5) + (item_value * 0.1)
        success_chance = 90 - difficulty + (stealth_skill * 0.5)
        success_chance = max(5.0, min(95.0, success_chance)) # Cap al 5% min, 95% max
        
        roll = random.uniform(0, 100)
        is_success = roll <= success_chance
        
        return {
            "success": is_success,
            "chance_had": success_chance,
            "detected": not is_success and roll > success_chance + 10 # Detectado si falla por mucho
        }
