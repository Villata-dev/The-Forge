class EnchantingTable:
    def apply_enchantment(self, weapon, soul_gem, effect):
        if soul_gem['is_filled']:
            weapon['enchantment'] = effect
            weapon['charge'] = soul_gem['capacity']
            return True
        return False
