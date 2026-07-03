from systems.progression import LevelingSystem

def test_level_up():
    sys = LevelingSystem(base_xp=100)
    assert sys.level == 1
    # Nivel 2 requiere 100 * (1^1.5) = 100 XP
    leveled = sys.add_xp(150)
    assert leveled == True
    assert sys.level == 2
    assert sys.current_xp == 50
    assert sys.stat_points == 3
