import pygame
from random import randint

class Meteor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = randint(100, 200)
        self.skin = pygame.image.load("png/meteor.png")
        self.enabled = True
        self.frame = 0

    def move(self, delta, height):
        self.y += self.speed * delta
        if(self.y > height):
            self.enabled = False

    def draw(self, scene):
        if (self.enabled):
            scene.blit(self.skin, (self.x, self.y))

    def is_collision(self, rocket):
        for i in range(len(rocket)):
            a = abs(self.x - 16 - rocket[i].x + 16)
            b = abs(self.y - rocket[i].y)
            c = (a ** 2 + b ** 2) ** 0.5
            if (c < 32 and self.enabled):
                return rocket[i]
        return None
