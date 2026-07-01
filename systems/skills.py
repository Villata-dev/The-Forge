class PerkTree:
    def __init__(self):
        self.level = 15
        self.perks = {
            "Steel Smithing": False,
            "Dwarven Smithing": False,
            "Orcish Smithing": False,
            "Ebony Smithing": False,
            "Daedric Smithing": False
        }

    def unlock_perk(self, perk_name: str, req_level: int) -> bool:
        if perk_name in self.perks and self.level >= req_level:
            self.perks[perk_name] = True
            return True
        return False
