import pygame
from setup import *
from random import randint
from model.ship import Ship
from services.sound import Sound

class Heart:

    def __init__(self, x, y, snd):
        self.x = x
        self.y = y
        self.snd = snd
        self.number = []

        self.speed_y = randint(150, 250)
        self.speed_x = randint(-100, 100)

        self.skin = pygame.image.load("png/heart.png")
        self.enabled = True

    def move(self, delta, height):
        self.x += self.speed_x * delta
        if self.x < 0 or self.x > WIDTH - self.skin.get_width():
            self.speed_x = -self.speed_x
            self.x += self.speed_x * delta

        self.y += self.speed_y * delta
        if(self.y > height):
            self.enabled = False

    def draw(self, scene):
        if (self.enabled):
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

        if (c < 24 and self.enabled == True):
            ship.dec_frame()
            self.enabled = False
            self.snd.play(Sound.BOOM)
            return True

        return False

