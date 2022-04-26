import pygame.image


class Background:


    def __init__(self, y):
        self.y = y
        self.skin = pygame.image.load("png/background.png")
        self.skin_x = self.skin.get_width()

    def draw(self, scene, x):
        scene.blit(self.skin, (-self.skin_x / 6 - x / 4, self.y))

    def move(self, delta, height):
        self.y += 100 * delta
        if self.y >= height:
            self.y = -self.skin.get_height()