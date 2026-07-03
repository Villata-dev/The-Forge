from systems.magic import SpellSystem

def test_spell_casting():
    sys = SpellSystem(max_mana=50)
    # Fireball cuesta 25
    res = sys.cast_spell("Fireball")
    assert res["success"] == True
    assert sys.current_mana == 25
    
    # Intento de segundo Fireball sin mana suficiente
    res2 = sys.cast_spell("Oakflesh") # Cuesta 40
    assert res2["success"] == False
