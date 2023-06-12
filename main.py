import sys

import pygame
from pygame.locals import *

from data.controller import Controller
from data.states.splash import Splash
from data.states.menu import Menu
from data.states.gameplay import Gameplay
from data.states.game_over import Gameover


def main():
    # Initialize game
    pygame.init()

    # Create a controller
    game_controller = Controller()

    # Game states
    states = {"SPLASH": Splash(),
              "MENU": Menu(),
              "GAMEPLAY": Gameplay(),
              "GAMEOVER": Gameover()}
    game_controller.setup_states(states, "SPLASH")

    # Run the game
    game_controller.run()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()