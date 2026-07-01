from systems.crafting import SmithingSystem

def test_successful_crafting():
    materials = {"Iron Ingot": 5, "Leather Strips": 2}
    assert SmithingSystem.craft("Iron Dagger", materials) == True

def test_failed_crafting_missing_materials():
    materials = {"Iron Ingot": 0, "Leather Strips": 2}
    assert SmithingSystem.craft("Iron Dagger", materials) == False
