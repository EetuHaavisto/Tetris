import random

import pygame

from .state import State
from data.settings import COLORS
from data.settings import GFX
from data.settings import GAME_CAPTION, TILE_SIZE
from data.settings import FONTS
from data.gameobjects.player import Block



PLAY_SCREEN_WIDTH = 10 * TILE_SIZE


class Gameplay(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GAMEOVER"
        self.play_surface = pygame.surface.Surface((PLAY_SCREEN_WIDTH, self.screen_rect.height))
        self.play_surface.fill(COLORS["WHITE"])
        self.play_rect = self.play_surface.get_rect()

        center_x = self.screen_rect.width - (self.screen_rect.width-self.play_rect.width)/2
        self.title_surface = pygame.font.Font.render(self.font_header, GAME_CAPTION, True, COLORS["WHITE"])
        self.title_rect = self.title_surface.get_rect(centerx=center_x, y=50)
        self.next_piece_surface = pygame.font.Font.render(self.font_text, "Next Block", True, COLORS["WHITE"])
        self.next_piece_rect = self.next_piece_surface.get_rect(centerx=center_x, y=self.title_rect.y + 100)
        self.score_surface = pygame.font.Font.render(self.font_text, "Score:", True, COLORS["WHITE"])
        self.score_rect = self.score_surface.get_rect(centerx=center_x, y=self.next_piece_rect.y + 100)
        
        self.images = [pygame.image.load(GFX[image]).convert_alpha() for image in GFX.keys()]

        self.current_block = Block(self.play_rect, random.choice(self.images))
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
            self.current_block = Block(self.play_rect, random.choice(self.images))
            self.current_block_group.add(self.current_block)

            if self.__is_game_over():
                self.done = True
    
    def draw(self, screen):
        """Renders the graphics"""
        self.draw_game_screen(screen)
        self.current_block_group.draw(screen)
        self.stopped_blocks_group.draw(screen)

    def draw_game_screen(self, screen):
        screen.fill(COLORS["BLACK"])
        screen.blit(self.play_surface, self.play_rect)
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.score_surface, self.score_rect)
        screen.blit(self.next_piece_surface, self.next_piece_rect)

    def __is_game_over(self):
        # This is a private method meant to be used inside this class
        # The game ends when a newly generated block collides with the old
        if pygame.sprite.spritecollideany(self.current_block, self.stopped_blocks_group):
            return True

        return False