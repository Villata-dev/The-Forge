class FogOfWar:
    def __init__(self, map_width: int, map_height: int, tile_size: int):
        self.visited = set()
        self.tile_size = tile_size

    def reveal(self, player_pos: tuple, radius: int):
        px, py = int(player_pos[0] // self.tile_size), int(player_pos[1] // self.tile_size)
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                if dx*dx + dy*dy <= radius*radius:
                    self.visited.add((px + dx, py + dy))
