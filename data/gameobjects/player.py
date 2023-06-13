import pygame

from data.settings import COLORS


class Player(pygame.sprite.Sprite):

    def __init__(self, screen_rect):
        super().__init__()
        self.screen_rect = screen_rect

        self.image = pygame.surface.Surface((40, 40))
        self.image.fill(COLORS["RED"])
        self.rect = self.image.get_rect(center=self.screen_rect.center)