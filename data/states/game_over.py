import pygame

from .state import State
from data.settings import COLORS


class Gameover(State):

    def __init__(self):
        super().__init__()
        self.title = self.font.render("GAME OVER", True, COLORS["WHITE"])
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def handle_events(self, events):
        """Event handler"""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        """Render graphics"""
        screen.fill(COLORS["BLACK"])
        screen.blit(self.title, self.title_rect)