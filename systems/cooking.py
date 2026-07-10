class CookingSystem:
    RECIPES = {
        "Cooked Salmon": {"Salmon": 1, "Salt Pile": 1},
        "Venison Stew": {"Venison": 1, "Potato": 2, "Leek": 1}
    }

    @classmethod
    def cook(cls, recipe_name: str, inventory: dict) -> bool:
        if recipe_name not in cls.RECIPES: return False
        
        for ing, qty in cls.RECIPES[recipe_name].items():
            if inventory.get(ing, 0) < qty: return False
        return True
