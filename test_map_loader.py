import os
import pygame
from engine.map_loader import TiledMap

# Set SDL to dummy drivers for headless testing
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

def test_map_loading():
    pygame.init()
    # Need a screen for some pygame functions (like loading images, though test_map.tmx doesn't have any tilesets yet)
    pygame.display.set_mode((1, 1))

    try:
        map_path = "assets/maps/test_map.tmx"
        tiled_map = TiledMap(map_path)
        print(f"Map loaded successfully! Size: {tiled_map.width}x{tiled_map.height}")

        # Test get_tile_properties (should be None for empty tiles in our dummy map)
        props = tiled_map.get_tile_properties(0, 0, 0)
        print(f"Properties at (0, 0, 0): {props}")

    except Exception as e:
        print(f"Error loading map: {e}")
        exit(1)
    finally:
        pygame.quit()

if __name__ == "__main__":
    test_map_loading()
