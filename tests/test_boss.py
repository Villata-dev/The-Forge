from entities.boss_ai import BossFSM

def test_boss_phase_transition():
    boss = BossFSM(hp_thresholds=[50.0])
    assert boss.current_phase == 1
    
    transitioned = boss.update_phase(49.0)
    assert transitioned == True
    assert boss.current_phase == 2
