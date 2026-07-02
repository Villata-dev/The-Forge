from systems.quests import QuestLog

def test_quest_completion():
    log = QuestLog()
    log.add_quest("q_test", {"gather_wood": {"current": 0, "required": 5}})
    log.update_objective("q_test", "gather_wood", 3)
    assert "q_test" in log.active_quests
    log.update_objective("q_test", "gather_wood", 2)
    assert "q_test" in log.completed_quests
    assert "q_test" not in log.active_quests
