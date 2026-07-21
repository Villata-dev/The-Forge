class QuestManager:
    def __init__(self, event_bus):
        self.active_quests = {}
        self.completed_quests = set()
        event_bus.subscribe("ENEMY_KILLED", self.update_kill_objectives)
    def update_kill_objectives(self, enemy_id): pass
