class Equipment:
    def __init__(self):
        self.slots = {
            "head": None,
            "chest": None,
            "hands": None,
            "feet": None,
            "weapon": None
        }

    def equip(self, slot: str, item_data: dict):
        if slot in self.slots:
            self.slots[slot] = item_data

    def get_total_armor(self) -> float:
        total = 0.0
        for slot in ["head", "chest", "hands", "feet"]:
            if self.slots[slot]:
                total += self.slots[slot].get("armor_value", 0)
        return total
