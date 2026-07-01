import json
import os

class SaveSystem:
    SAVE_FILE = "data/savegame.json"

    @classmethod
    def save_game(cls, inventory_data: dict, economy_data: dict, skills_data: dict):
        state = {
            "inventory": inventory_data,
            "economy": economy_data,
            "skills": skills_data
        }
        with open(cls.SAVE_FILE, 'w') as f:
            json.dump(state, f, indent=4)

    @classmethod
    def load_game(cls) -> dict:
        if not os.path.exists(cls.SAVE_FILE):
            return {}
        with open(cls.SAVE_FILE, 'r') as f:
            return json.load(f)
