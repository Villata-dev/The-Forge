class SmithingSystem:
    # Arbol de progresion
    TIERS = ["Iron", "Steel", "Dwarven", "Orcish", "Ebony"]
    
    RECIPES = {
        "Iron Dagger": {"Iron Ingot": 1, "Leather Strips": 1},
        "Steel Sword": {"Steel Ingot": 2, "Leather Strips": 1, "Iron Ingot": 1},
        "Dwarven Bow": {"Dwarven Metal Ingot": 3, "Iron Ingot": 1}
    }

    @classmethod
    def craft(cls, item_name: str, available_materials: dict) -> bool:
        if item_name not in cls.RECIPES: return False
        recipe = cls.RECIPES[item_name]
        
        for material, cost in recipe.items():
            if available_materials.get(material, 0) < cost:
                return False
                
        # Consumo deducido logicamente (simulado)
        return True
