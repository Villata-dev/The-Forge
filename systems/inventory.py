class Inventory:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.current_weight = 0.0
        self.items = {
            "Weapons": [],
            "Apparel": [],
            "Ingredients": [],
            "Misc": []
        }

    def add_item(self, category: str, item_id: str, weight: float) -> bool:
        if self.current_weight + weight > self.capacity:
            return False
        if category in self.items:
            self.items[category].append(item_id)
            self.current_weight += weight
            return True
        return False
