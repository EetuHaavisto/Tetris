import os

from data.tools import resource_paths


GAME_CAPTION = "TETRIS"
SCREEN_SIZE = (400, 400)
TILE_SIZE = 20
# Colors
COLORS ={"WHITE": (255, 255, 255),
         "BLACK": (0, 0, 0),
         "RED": (255, 0, 0)}

# Paths for resources (Dictionaries)
FONTS = resource_paths(os.path.join("resources", "fonts"), (".ttf"))
GFX = resource_paths(os.path.join("resources", "graphics"), (".png"))
