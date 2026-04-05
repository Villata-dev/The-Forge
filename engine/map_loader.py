import pytmx

class TiledMap:
    """
    Class to load and handle TMX maps created with Tiled.
    """
    def __init__(self, filename):
        """
        Initializes the TiledMap by loading the TMX file.

        Args:
            filename (str): The path to the TMX file.
        """
        self.tmx_data = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
        self.offset = (0, 0)

    def render(self, surface, layer_type=None):
        """Renders the map layers to the surface, considering the camera offset.

        Args:
            surface (pygame.Surface): The surface to draw the tiles on.
            layer_type (str, optional): Filters layers by name (e.g., 'Suelo' or 'Foreground').
                                        If None, renders all visible non-object layers.
        """
        for layer in self.tmx_data.visible_layers:
            # We only draw non-object layers here (e.g., Background/Foreground)
            # Layers that need Y-sort are handled by sprites in the GameState.
            if isinstance(layer, pytmx.TiledTileLayer) and "Objetos" not in layer.name:
                if layer_type and layer_type not in layer.name:
                    continue
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        pos = (x * self.tmx_data.tilewidth + self.offset[0],
                               y * self.tmx_data.tileheight + self.offset[1])
                        surface.blit(tile, pos)

    def get_tile_properties(self, x, y, layer):
        """
        Gets the properties of a tile at a specific location and layer.

        Args:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            layer (int): The layer index.

        Returns:
            dict: The properties of the tile, or None if no properties exist.
        """
        try:
            properties = self.tmx_data.get_tile_properties(x, y, layer)
            return properties
        except (ValueError, IndexError):
            return None
