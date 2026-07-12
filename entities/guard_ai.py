class ArrestState:
    def check_bounty(self, player_bounty): return "ARREST" if player_bounty > 0 else "PATROL"
