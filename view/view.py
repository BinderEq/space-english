import pygame

class View:

    def __init__(self):
        self.skin = pygame.image.load("png/obloshka.png")

    def draw(self, scene):
        scene.blit(self.skin, (0, 0))
