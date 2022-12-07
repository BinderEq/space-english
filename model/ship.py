import pygame
import setup


class Ship:

    def __init__(self):
        self.x = 218
        self.y = 750
        self.skin = [pygame.image.load('png/space_ship.png'),
                     pygame.image.load('png/space_ship brick_01.png'),
                     pygame.image.load('png/space_ship brick_02.png'),
                     pygame.image.load('png/space_ship brick_03.png'),
                     pygame.image.load('png/space_ship brick_04.png'),
                     pygame.image.load('png/space_ship brick_05.png'),
                     pygame.image.load('png/space_ship brick_06.png')]
        self.frame = 0
        self.live = True

    def draw(self, scene):
        if (self.live == True):
            scene.blit(self.skin[self.frame], (self.x, self.y))

    def move_left(self, delta):
        if setup.fuel <= 0:
            return False
        self.x -= 300 * delta

    def move_right(self, delta):
        if setup.fuel <= 0:
            return False
        self.x += 300 * delta

    def dec_frame(self):
        self.frame -= 1
        if self.frame < 0:
            self.frame = 0

    def inc_frame(self):
        self.frame += 1
        if (self.frame == len(self.skin)):
            self.live = False

    def is_dead(self):
        return not self.live

