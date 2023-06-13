import pygame

from .state import State
from data.settings import COLORS


class Menu(State):

    def __init__(self):
        super().__init__()
        self.active_index = 0
        self.options = ["Start Game", "Quit"]
        self.next_state = "GAMEPLAY"

    def render_text(self, index):
        """Create text surfaces"""
        color = COLORS["RED"] if index == self.active_index else COLORS["WHITE"]
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        """Returns position for text surface"""
        center = (self.screen_rect.centerx, self.screen_rect.centery + index * 50)
        return text.get_rect(center=center)
    
    def handle_action(self):
        """Determines the action when the user presses ENTER (transition to 
        the next state or quit)"""
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.quit = True

    def handle_events(self, events):
        """Event handler"""
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.active_index = 1 if self.active_index <= 0 else 0
                elif event.key == pygame.K_DOWN:
                    self.active_index = 0 if self.active_index >= 1 else 1
                elif event.key == pygame.K_RETURN:
                    self.handle_action()

    def update(self, dt):
        pass

    def draw(self, screen):
        """Render graphics"""
        screen.fill(COLORS["BLACK"])
        for index, option in enumerate(self.options):
            text = self.render_text(index)
            screen.blit(text, self.get_text_position(text, index))