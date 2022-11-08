import pygame

class View:

    def __init__(self, file):
        self.skin = pygame.image.load(file)

    def draw(self, scene):
        scene.blit(self.skin, (0, 0))
