import random

import pygame

from .state import State
from data.settings import COLORS
from data.settings import GFX
from data.gameobjects.player import Block


class Gameplay(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GAMEOVER"

        self.images = [pygame.image.load(GFX[image]).convert_alpha() for image in GFX.keys()]

        self.current_block = Block(self.screen_rect, random.choice(self.images))
        self.current_block_group = pygame.sprite.GroupSingle(self.current_block)


    def handle_events(self, events):
        """Event handler"""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.current_block.move_x()
                elif event.key == pygame.K_LEFT:
                    self.current_block.move_x(-1)
                elif event.key == pygame.K_UP:
                    self.current_block.rotate()
    
    def update(self, dt):
        """Game logic"""
        self.current_block_group.update(dt)
    
    def draw(self, screen):
        """Renders the graphics"""
        screen.fill(COLORS["BLACK"])
        self.current_block_group.draw(screen)