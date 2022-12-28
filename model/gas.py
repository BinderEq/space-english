import pygame

import setup
from setup import *
from random import randint
from model.ship import Ship
from services.sound import Sound


class Gas:

    def __init__(self, x, y, snd):
        self.x = x
        self.y = y
        self.speed = randint(100, 200)
        self.skin = pygame.image.load("png/fuel.png")
        self.enabled = True
        self.frame = 0
        self.snd = snd

    def move(self, delta, height):
        if setup.fuel > 0:
            self.y += self.speed * delta
        else:
            self.y += self.speed * 2 * delta

        if self.y > height:
            self.enabled = False

    def draw(self, scene):
        if self.enabled:
            scene.blit(self.skin, (self.x, self.y))

    def is_collision(self, rocket):
        for i in range(len(rocket)):
            a = abs(self.x - 16 - rocket[i].x + 16)
            b = abs(self.y - rocket[i].y)
            c = (a ** 2 + b ** 2) ** 0.5
            if (c < 25 and self.enabled):
                return rocket[i]
        return None

    def is_collision_ship(self, ship: Ship):
        a = abs((self.x + 16) - (ship.x + 32))
        b = abs((self.y + 16) - (ship.y + 32))
        c = (a ** 2 + b ** 2) ** 0.5

        if (c < 48 and self.enabled == True):
            self.enabled = False
            self.snd.play(Sound.BOOM)
            return True
