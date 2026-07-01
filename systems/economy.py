class EconomyManager:
    def __init__(self, initial_gold: int = 100):
        self.gold = initial_gold

    def buy_item(self, cost: int) -> bool:
        if self.gold >= cost:
            self.gold -= cost
            return True
        return False

    def sell_item(self, value: int, speech_multiplier: float = 1.0):
        profit = int(value * speech_multiplier)
        self.gold += profit
        return profit
