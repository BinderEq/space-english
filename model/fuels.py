import setup
import pygame


class Fuels:

    def __init__(self):
        self.fuel_on = pygame.image.load("png/fuel_indicator_on.png")
        self.fuel_off = pygame.image.load("png/fuel_indicator_off.png")

    def draw(self, scene):
        cf = int(setup.fuel + 100) // 100
        if setup.fuel <= 0:
            return False

        for i in range(cf):
            scene.blit(self.fuel_on, (setup.WIDTH - 32, setup.HEIGHT * 0.75 - i * 16))

        for i in range(cf, 10):
            scene.blit(self.fuel_off, (setup.WIDTH - 32, setup.HEIGHT * 0.75 - i * 16))

    def dec_fuel(self, deltatime):
        setup.fuel -= setup.fuel_decrease_sec * deltatime