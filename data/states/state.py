import pygame

from data.settings import FONTS


class State():
    """Represents a state of the game. All states should inherit this class 
    and the methods (handle_events, update, draw) must be overwritten 
    in each sub-class."""

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(FONTS["fixedsys"], 48)
        self.graphics = {}
        self.sounds = {}

    def start(self, persistent):
        """Add variables passed in persistent."""
        self.persist = persistent

    def cleanup(self):
        """Return variables that should persists."""
        self.done = False
        print("Cleaned")
        return self.persist

    def handle_events(self, events):
        raise NotImplementedError("handle_event method must be defined on "
                                  "the subclass")
    
    def update(self, dt):
        raise NotImplementedError("update method must be defined on "
                                  "the subclass")
    
    def draw(self, screen):
        raise NotImplementedError("draw method must be defined on the subclass")