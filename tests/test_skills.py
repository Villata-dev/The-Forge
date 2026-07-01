from systems.skills import PerkTree

def test_perk_unlocking():
    tree = PerkTree()
    tree.level = 30
    assert tree.unlock_perk("Dwarven Smithing", 30) == True
    assert tree.unlock_perk("Ebony Smithing", 80) == False
