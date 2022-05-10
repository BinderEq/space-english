import pygame

class Rocket:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Существует ли ракета
        self.enabled = True

        self.speed = 125
        self.skin = [pygame.image.load("png/rocket_01.png"),
                  pygame.image.load("png/rocket_02.png"),
                  pygame.image.load("png/rocket_03.png"),
                  pygame.image.load("png/rocket_04.png")]

        # Изменение размера ракет
        for i in range(len(self.skin)):
            self.skin[i] = pygame.transform.scale(self.skin[i], (8, 16))


        self.frame = 0

    def move(self, delta, frame):
        self.y -= self.speed * delta

        if self.y < 0:
            self.enabled = False

        if frame % 20 == 0:
            self.frame += 1
            if (self.frame >= len(self.skin)):
                self.frame = 0

    def draw(self, scene):
        if (self.enabled):
            scene.blit(self.skin[self.frame], (self.x, self.y))