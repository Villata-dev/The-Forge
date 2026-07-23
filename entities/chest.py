import pygame
class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, loot_table_id):
        super().__init__()
        self.is_open = False
        self.loot_table_id = loot_table_id
    def interact(self):
        if not self.is_open:
            self.is_open = True
            return True
        return False
