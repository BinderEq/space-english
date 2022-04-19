import pygame

class Rocket:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 60
        self.skin = [pygame.image.load("png/rocket_01.png"),
                  pygame.image.load("png/rocket_02.png"),
                  pygame.image.load("png/rocket_03.png"),
                  pygame.image.load("png/rocket_04.png")]
        self.frame = 0

    def move(self, delta):
        self.y -= self.speed * delta

    def draw(self, scene):
        scene.blit(self.skin[self.frame], (self.x, self.y))