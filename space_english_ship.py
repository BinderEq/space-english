import pygame

class Ship:
    def __init__(self):
        self.x = 218
        self.y = 500
        self.skin = pygame.image.load('png/space_ship.png')

    def draw(self, scene):
        scene.blit(self.skin, (self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
