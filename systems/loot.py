import random

class LootTable:
    def __init__(self):
        self.tables = {
            "bandit": [
                {"item": "Gold Coin", "weight": 60, "amount": (5, 15)},
                {"item": "Iron Dagger", "weight": 30, "amount": (1, 1)},
                {"item": "Minor Healing Potion", "weight": 10, "amount": (1, 2)}
            ]
        }

    def drop_loot(self, entity_type: str) -> list:
        if entity_type not in self.tables: return []
        
        drops = []
        table = self.tables[entity_type]
        roll = random.randint(1, 100)
        
        current_weight = 0
        for entry in table:
            current_weight += entry["weight"]
            if roll <= current_weight:
                amount = random.randint(*entry["amount"])
                drops.append({"item": entry["item"], "amount": amount})
                break
        return drops
