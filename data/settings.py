import os

from data.tools import resource_paths


GAME_CAPTION = "Game title"
SCREEN_SIZE = (800, 600)

# Colors
COLORS ={"WHITE": (255, 255, 255),
         "BLACK": (0, 0, 0),
         "RED": (255, 0, 0)}

# Paths for resources (Dictionaries)
FONTS = resource_paths(os.path.join("resources", "fonts"), (".ttf"))
GFX = resource_paths(os.path.join("resources", "graphics"), (".png", ".jpg"))
