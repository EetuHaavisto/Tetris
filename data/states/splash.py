import pygame

from .state import State
from data.settings import GAME_CAPTION, COLORS


class Splash(State):

    def __init__(self):
        super().__init__()
        self.title = self.font.render(GAME_CAPTION, True, COLORS["WHITE"])
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        """Controls the duration for which the SPLASH screen is displayed."""
        self.time_active += dt
        if self.time_active >= 4:
            self.done = True

    def draw(self, screen):
        """Render graphics"""
        screen.fill(COLORS["BLACK"])
        screen.blit(self.title, self.title_rect)

    def handle_events(self, events):
        """Event handler"""
        for event in events:
            if event.type == pygame.KEYUP:
                self.done = True
