class QuestLog:
    def __init__(self):
        self.active_quests = {}
        self.completed_quests = set()

    def add_quest(self, quest_id: str, objectives: dict):
        if quest_id not in self.completed_quests:
            self.active_quests[quest_id] = objectives

    def update_objective(self, quest_id: str, objective_key: str, amount: int = 1):
        if quest_id in self.active_quests:
            obj = self.active_quests[quest_id].get(objective_key)
            if obj:
                obj['current'] = min(obj['current'] + amount, obj['required'])
                self._check_completion(quest_id)

    def _check_completion(self, quest_id: str):
        quest = self.active_quests[quest_id]
        if all(obj['current'] >= obj['required'] for obj in quest.values()):
            self.completed_quests.add(quest_id)
            del self.active_quests[quest_id]
