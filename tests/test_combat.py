from systems.combat import CombatSystem

def test_damage_reduction():
    result = CombatSystem.calculate_damage(100, 500, crit_chance=0.0) # 500 armor = 60% reduction
    assert result["damage"] == 40
    
def test_armor_cap():
    result = CombatSystem.calculate_damage(100, 1000, crit_chance=0.0) # Cap at 80%
    assert result["damage"] == 20
