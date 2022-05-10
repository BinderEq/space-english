import pygame

class Explosions:
    """Класс, отрисовывающий и контролирующий взрывы."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.skin = [pygame.image.load("png/boom_01.png"),
                     pygame.image.load("png/boom_02.png"),
                     pygame.image.load("png/boom_03.png"),
                     pygame.image.load("png/boom_04.png")]

        self.frame = 0
        self.time_frame = 0
        self.enabled = True

    def draw(self, scene, deltatime):

        scene.blit(self.skin[self.frame], (self.x, self.y))

        self.time_frame += deltatime
        if (self.time_frame > 0.25):
            self.frame += 1
            self.time_frame = 0
            if (self.frame >= len(self.skin)):
                self.frame = 0
                self.enabled = False
