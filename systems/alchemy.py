class AlchemySystem:
    @staticmethod
    def craft_potion(ingredient1: dict, ingredient2: dict) -> dict:
        # Cada ingrediente debe tener una lista de 4 efectos
        effects1 = set(ingredient1.get("effects", []))
        effects2 = set(ingredient2.get("effects", []))
        
        shared_effects = effects1.intersection(effects2)
        
        if not shared_effects:
            return {"success": False, "item": "Ruined Potion", "value": 0}
            
        return {
            "success": True,
            "item": "Custom Potion",
            "effects": list(shared_effects),
            "value": len(shared_effects) * 50
        }
