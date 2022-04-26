import pygame

class Meteor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 250
        self.skin = pygame.image.load("png/mteor.png")

        self.frame = 0

    def move(self, delta, frame):
        self.y += self.speed * delta


    def draw(self, scene):
        scene.blit(self.skin[self.frame], (self.x, self.y))