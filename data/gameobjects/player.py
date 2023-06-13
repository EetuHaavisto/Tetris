import pygame

from data.settings import COLORS


SPEED_Y = 100
SPEED_X = 20

class Block(pygame.sprite.Sprite):

    def __init__(self, screen_rect, image):
        super().__init__()
        self.screen_rect = screen_rect

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
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

    def rotate(self, rotation_angle = 90):
        rotated_image = pygame.transform.rotate(self.image, rotation_angle)
        rotated_mask = pygame.mask.from_surface(rotated_image)

        self.image = rotated_image
        self.mask = rotated_mask


