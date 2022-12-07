import pygame.image

import setup


class Background:

    def __init__(self, y):
        self.y = y
        self.skin = pygame.image.load("png/background.png")
        self.skin_x = self.skin.get_width()
        self.current_speed_y = 100

    def draw(self, scene, x):
        scene.blit(self.skin, (-self.skin_x / 6 - x / 4, self.y))

    def move(self, delta, height):
        if setup.fuel > 0:
            self.y += 100 * delta
            if self.y >= height:
                self.y = -self.skin.get_height()
        else:
            if self.current_speed_y > 0:
                self.current_speed_y += 100 * delta
                if self.current_speed_y > 2000:
                    self.current_speed_y = 0
                    print("Конец игры")

            self.y -= self.current_speed_y * delta
            if self.y + self.skin.get_height() <= 0:
                self.y = self.skin.get_height()





