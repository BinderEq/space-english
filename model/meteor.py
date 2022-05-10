import pygame
from random import randint

class Meteor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = randint(150, 200)
        self.skin = pygame.image.load("png/meteor.png")
        self.enabled = True
        self.frame = 0

    def move(self, delta, height):
        self.y += self.speed * delta
        if(self.y > height):
            self.enabled = False

    def draw(self, scene):
        scene.blit(self.skin, (self.x, self.y))

    def is_collision(self, rocket):
        for i in range(len(rocket)):
            a = abs(self.x + 32 - rocket[i].x)
            b = abs(self.y + 32 - rocket[i].y)
            c = (a ** 2 + b ** 2) ** 0.5
            if (c < 25 and self.enabled):
                return rocket[i]
        return None
