class CheckpointSystem:
    def __init__(self): self.active_bonfire = None
    def rest(self, player, world_state):
        player.refill_health()
        world_state.respawn_enemies()
