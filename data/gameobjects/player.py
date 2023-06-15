import pygame


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

    def change_x_speed(self, dir=1):
        """Changes speed in x-direction. 
        Called when user presses left or right key"""
        self.speed_x = dir * SPEED_X
    
    def move(self, stopped_blocks_group, dt):
        """Moves the block down and left/right and checks 
        for collisions with other blocks"""
        y_increment = SPEED_Y * dt
        x_increment = self.speed_x
        self.true_y += y_increment
        self.rect.x += x_increment
        self.rect.y = round(self.true_y)

        collided = pygame.sprite.spritecollideany(self, stopped_blocks_group, 
                                                  collided=pygame.sprite.collide_mask)
        self.check_collisions(collided, stopped_blocks_group, 
                              y_increment, x_increment)

        self.speed_x = 0

    def update(self, dt):
        self.move(dt)

    def rotate(self, stopped_blocks_group, rotation_angle = 90):
        rotated_image = pygame.transform.rotate(self.image, rotation_angle)
        rotated_mask = pygame.mask.from_surface(rotated_image)
        rotated_rect = rotated_image.get_rect(x = self.rect.x, y = self.rect.y)

        rotated_sprite = pygame.sprite.Sprite()
        rotated_sprite.rect = rotated_rect

        # Check that the rotated block doesn't collide
        if pygame.sprite.spritecollideany(rotated_sprite,stopped_blocks_group) == None:
            self.image = rotated_image
            self.mask = rotated_mask
            self.rect = rotated_rect

        del rotated_sprite

    def check_collisions(self, collided, stopped_blocks_group, y_increment, x_increment):
        if collided is not None:
            # Stop movement if the collision didn't happen from side of a block
            if self.speed_x == 0:
                self.kill()
                stopped_blocks_group.add(self)
                self.undo_y_movement(y_increment)
            else:
                self.rect.x -= x_increment
        # Block hits the bottom
        elif self.rect.bottom >= self.screen_rect.height:
            self.rect.bottom = self.screen_rect.height
            self.kill()
            stopped_blocks_group.add(self)

    def undo_y_movement(self, increment):
        """Undos last movement in y-direction after collision"""
        self.true_y -= increment
        # Round the y position to nearest ten
        self.true_y = round(self.true_y / 10) * 10
        self.rect.y = round(self.true_y)

