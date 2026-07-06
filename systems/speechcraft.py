import random

class SpeechcraftSystem:
    @staticmethod
    def attempt_persuasion(player_charisma: int, npc_willpower: int, difficulty_modifier: float = 1.0) -> bool:
        # Probabilidad base influenciada por la diferencia entre carisma y fuerza de voluntad
        base_chance = 50.0 + (player_charisma - npc_willpower)
        final_chance = base_chance * difficulty_modifier
        
        # Limites logicos (siempre hay un 5% de exito o fallo catastrofico)
        final_chance = max(5.0, min(95.0, final_chance))
        
        roll = random.uniform(0, 100)
        return roll <= final_chance
