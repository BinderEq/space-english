import pygame

class Rocket:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 250
        self.skin = [pygame.image.load("png/rocket_01.png"),
                  pygame.image.load("png/rocket_02.png"),
                  pygame.image.load("png/rocket_03.png"),
                  pygame.image.load("png/rocket_04.png")]
        self.frame = 0

    def move(self, delta, frame):
        self.y -= self.speed * delta

        if frame % 20 == 0:
            self.frame += 1
            if (self.frame >= len(self.skin)):
                self.frame = 0

    def draw(self, scene):
        scene.blit(self.skin[self.frame], (self.x, self.y))