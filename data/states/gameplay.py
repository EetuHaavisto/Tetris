import pygame

from .state import State
from data.settings import COLORS
from data.gameobjects.player import Player


class Gameplay(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GAMEOVER"

        self.player = Player(self.screen_rect)
        self.player_group = pygame.sprite.GroupSingle(self.player)

    def handle_events(self, events):
        """Event handler"""
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.done = True
    
    def update(self, dt):
        """Game logic"""
        pass
    
    def draw(self, screen):
        """Renders the graphics"""
        screen.fill(COLORS["BLACK"])
        self.player_group.draw(screen)