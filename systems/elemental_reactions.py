class Elements:
    REACTIONS = {("Water", "Lightning"): "Electrocuted", ("Fire", "Oil"): "Explosion"}
    def check_reaction(self, effect1, effect2): return self.REACTIONS.get((effect1, effect2))
