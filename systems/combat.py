import random

class CombatSystem:
    @staticmethod
    def calculate_damage(attack_power: float, target_armor: float, crit_chance: float = 0.05) -> dict:
        """Calcula el dano final aplicando reduccion de armadura y probabilidad de critico"""
        is_crit = random.random() < crit_chance
        multiplier = 1.5 if is_crit else 1.0
        
        # Formula de reduccion de armadura (estilo Skyrim: cap al 80%)
        damage_reduction = min(target_armor * 0.12, 80.0) / 100.0
        base_damage = attack_power * multiplier
        
        final_damage = max(base_damage * (1.0 - damage_reduction), 1.0)
        
        return {
            "damage": int(final_damage),
            "is_critical": is_crit
        }
