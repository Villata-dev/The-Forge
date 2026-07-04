class CrimeSystem:
    CRIMES = {
        "theft": 50,
        "assault": 1000,
        "murder": 5000,
        "trespassing": 10
    }

    def __init__(self):
        self.bounties = {} # { "faction_id": amount }

    def report_crime(self, faction: str, crime_type: str):
        if crime_type in self.CRIMES:
            if faction not in self.bounties:
                self.bounties[faction] = 0
            self.bounties[faction] += self.CRIMES[crime_type]

    def clear_bounty(self, faction: str):
        if faction in self.bounties:
            self.bounties[faction] = 0
