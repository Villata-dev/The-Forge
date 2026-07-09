import random

class FishingSystem:
    def attempt_catch(self, bait_quality: int, water_type: str) -> dict:
        chance = 30 + (bait_quality * 10)
        if random.uniform(0, 100) <= chance:
            return {"success": True, "fish": "Salmon" if water_type == "River" else "Bass"}
        return {"success": False}
