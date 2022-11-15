import pygame
WIDTH = 500
HEIGHT = 850
fullScreen = False

help = False

FPS = 120

BLACK = (0, 0, 0)

level = 0

playGame = True    

deltatime = 0

VIEW_SCREEN = 0
PLAY_GAME = 10
END_GAME = 13
NEXT_LEVEL = 20

state = VIEW_SCREEN


level_color = [(255, 255, 0),
               (255, 230, 0),
               (255, 200, 0),
               (255, 170, 0),
               (255, 150, 0),
               (255, 125, 0),
               (255, 100, 0),
               (255, 75, 0),
               (255, 50, 0),
               (255, 0, 0)]