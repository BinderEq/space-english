import pygame
from setup import *
from random import randint
from model.ship import Ship
class Meteor:

    def __init__(self, x, y, font, word):
        self.x = x
        self.y = y
        self.font = font
        self.word = word

        self.number = []
        self.color = (0, 255, 210)


        # Придумываем букву
        self.char = ""
        if randint(0, 100) > 60:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.char = alphabet[randint(0, len(alphabet) - 1)]

            # Буква, которая ТОЧНО есть
            if randint(0, 100) < 60:
                self.char = word[randint(0, len(word) - 1)]
            for i in range(len(self.word)):
                if (self.word[i] == self.char):
                    self.number.append(i)

            if (help):
                if (len(self.number) == 0):
                    self.color = (255, 200, 128)


        self.speed = randint(100, 200)
        self.skin = pygame.image.load("png/meteor.png")
        self.enabled = True
        self.frame = 0

    def move(self, delta, height):
        self.y += self.speed * delta
        if(self.y > height):
            self.enabled = False

    def draw(self, scene):
        if (self.enabled):
            scene.blit(self.skin, (self.x, self.y))
            if (self.char != ""):
                txt = self.font.getSystemText(self.char, self.char, self.color)
                scene.blit(txt, (self.x + (32 - txt.get_width()) / 2, self.y))

    def is_collision(self, rocket):
        for i in range(len(rocket)):
            a = abs(self.x - 16 - rocket[i].x + 16)
            b = abs(self.y - rocket[i].y)
            c = (a ** 2 + b ** 2) ** 0.5
            if (c < 25 and self.enabled):
                return rocket[i]
        return None

    def is_collision_ship(self, ship: Ship):
        a = abs(self.x - 16 - ship.x + 16)
        b = abs(self.y - 16 - ship.y + 16)
        c = (a **  2 + b ** 2) ** 0.5


        if (c < 32 and self.enabled == True):
            ship.inc_frame()
            self.enabled = False
            return True

