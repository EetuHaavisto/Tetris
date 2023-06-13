import os

from data.tools import resource_paths


GAME_CAPTION = "Game title"
SCREEN_SIZE = (800, 600)

TILE_SIZE = 20
GAME_HUB_SIZE = (10*TILE_SIZE, SCREEN_SIZE[1])
# Colors
COLORS ={"WHITE": (255, 255, 255),
         "BLACK": (0, 0, 0),
         "RED": (255, 0, 0)}

# Paths for resources (Dictionaries)
FONTS = resource_paths(os.path.join("resources", "fonts"), (".ttf"))
