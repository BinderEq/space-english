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
        scene.blit(self.skin, (self.x, self.y))