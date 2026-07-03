class AchievementTracker:
    def __init__(self):
        self.achievements = {
            "FIRST_BLOOD": {"desc": "Defeat your first enemy", "unlocked": False},
            "MASTER_SMITH": {"desc": "Craft an Ebony weapon", "unlocked": False},
            "WEALTHY": {"desc": "Accumulate 1000 gold", "unlocked": False}
        }

    def unlock(self, achievement_id: str) -> bool:
        if achievement_id in self.achievements and not self.achievements[achievement_id]["unlocked"]:
            self.achievements[achievement_id]["unlocked"] = True
            # Aqui se emitiria un evento al EventBus para mostrar en la UI
            return True
        return False
