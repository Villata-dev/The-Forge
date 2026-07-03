class SpellSystem:
    SPELLS = {
        "Fireball": {"mana_cost": 25, "damage": 40, "type": "destruction"},
        "Healing": {"mana_cost": 30, "healing": 50, "type": "restoration"},
        "Oakflesh": {"mana_cost": 40, "armor_buff": 20, "duration": 60, "type": "alteration"}
    }

    def __init__(self, max_mana: float):
        self.max_mana = max_mana
        self.current_mana = max_mana

    def cast_spell(self, spell_name: str) -> dict:
        if spell_name not in self.SPELLS:
            return {"success": False, "reason": "Unknown spell"}
            
        spell = self.SPELLS[spell_name]
        if self.current_mana >= spell["mana_cost"]:
            self.current_mana -= spell["mana_cost"]
            return {"success": True, "effect": spell}
            
        return {"success": False, "reason": "Insufficient mana"}
