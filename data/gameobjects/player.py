import pygame

from data.settings import COLORS


SPEED_Y = 100
SPEED_X = 20

class Block(pygame.sprite.Sprite):

    def __init__(self, screen_rect, image):
        super().__init__()
        self.screen_rect = screen_rect

        self.image = image
        self.rect = self.image.get_rect(centerx=self.screen_rect.centerx, y=0)

        # Floating point position
        self.true_y = self.rect.y

        self.speed_x = 0

    def move_x(self, dir=1):
        self.speed_x = dir * SPEED_X

    def move(self, dt):
        self.true_y += SPEED_Y * dt

        self.rect.x += self.speed_x
        self.rect.y = round(self.true_y)

        self.speed_x = 0

    def update(self, dt):
        self.move(dt)
