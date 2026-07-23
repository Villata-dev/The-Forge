import random
class LootGenerator:
    def __init__(self, tables_config):
        self.tables = tables_config
    def roll_loot(self, table_id):
        drops = []
        for item, chance in self.tables.get(table_id, {}).items():
            if random.uniform(0, 100) <= chance: drops.append(item)
        return drops
