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
