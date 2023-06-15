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
        self.stopped_blocks_group = pygame.sprite.Group()


    def handle_events(self, events):
        """Event handler"""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.current_block.change_x_speed()
                elif event.key == pygame.K_LEFT:
                    self.current_block.change_x_speed(-1)
                elif event.key == pygame.K_UP:

                    self.current_block.rotate(self.stopped_blocks_group)

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.current_block.y_speed_up()
        else:
            self.current_block.y_speed_normal()


    
    def update(self, dt):
        """Game logic"""
        self.current_block.move(self.stopped_blocks_group, dt)

        # Generating new block after collision
        if not self.current_block_group:
            self.current_block = Block(self.screen_rect, random.choice(self.images))
            self.current_block_group.add(self.current_block)

            if self.__is_game_over():
                self.done = True
    
    def draw(self, screen):
        """Renders the graphics"""
        screen.fill(COLORS["BLACK"])
        self.current_block_group.draw(screen)
        self.stopped_blocks_group.draw(screen)

    def __is_game_over(self):
        # This is a private method meant to be used inside this class
        # The game ends when a newly generated block collides with the old
        if pygame.sprite.spritecollideany(self.current_block, self.stopped_blocks_group):
            return True

        return False