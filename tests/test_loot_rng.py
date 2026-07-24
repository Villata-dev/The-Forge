from systems.loot_tables import LootGenerator
def test_100_percent_drop():
    generator = LootGenerator({"Test": {"ItemA": 100.0, "ItemB": 0.0}})
    drops = generator.roll_loot("Test")
    assert "ItemA" in drops
    assert "ItemB" not in drops
