# Подключаем pygame
from setup import *
from model.ship import Ship
from model.rocket import Rocket
from model.background import Background
from model.meteor import Meteor
from model.explosions import Explosions
from dict.dict import Dict
from services.font import Font
from random import randint

pygame.init()
size = [WIDTH, HEIGHT]
pygame.display.set_caption("Space English")

if (fullScreen):
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h
    scene = pygame.display.set_mode(flags=pygame.FULLSCREEN)
else:
    scene = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# Фоновый рисунок
background01 = Background(0)
background02 = Background(-HEIGHT)

font = Font()
dict = Dict()

frame = 0
ship = Ship()
rocket = []
pause = False

meteor = []
explosions = []


# ГЛАВНЫЙ ЦИКЛ
while (playGame):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            playGame = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                playGame = False
            elif (event.key == pygame.K_LEFT and not pause):
                ship.move_left(deltatime)
            elif (event.key == pygame.K_RIGHT and not pause):
                ship.move_right(deltatime)
            elif (event.key == pygame.K_UP):
                print("ВВЕРХ")
            elif (event.key == pygame.K_DOWN):
                print("ВНИЗ")
            elif (event.key == pygame.K_i):
                pause = not pause
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1 and not pause):
                rocket.append(Rocket(ship.x, ship.y))
            if (event.button == 3 and not pause):
                rocket.append(Rocket(ship.x + 48, ship.y))

    if (pygame.mouse.get_pos()[0] < ship.x and not pause):
        ship.move_left(deltatime)
    elif (pygame.mouse.get_pos()[0] > ship.x + 64 and not pause):
        ship.move_right(deltatime)

    # Очищаем сцену
    scene.fill(BLACK)

    background01.draw(scene, ship.x)
    background02.draw(scene, ship.x)

    ship.draw(scene)

    for i in range(len(meteor)):
        meteor[i].draw(scene)
        res = meteor[i].is_collision(rocket)
        if (res != None):
            explosions.append(Explosions(meteor[i].x - 16, meteor[i].y - 16))
            res.enabled = False
            meteor[i].enabled = False

    for i in range(len(rocket)):
        rocket[i].draw(scene)

    for i in range(len(explosions)):
        explosions[i].draw(scene, deltatime)

    scene.blit(font.getBigText("WORD", dict.dict[dict.current_word][1], (255, 255, 255)), (10, 10))

    for i in range(len(dict.marker_chars)):
        if (dict.marker_chars[i]):
            scene.blit(font.getBigText("CH", dict.dict[dict.current_word][0][i], (255, 255, 255)), (10 + i * 20, 50))
        else:
            scene.blit(font.getBigText("CH2", "*", (255, 255, 255)), (10 + i * 20, 50))

    # Отрисовываем изображения
    pygame.display.flip()

    # Расчёты:
    # ...
    if not pause:
        for i in range(len(rocket)):
            rocket[i].move(deltatime, frame)

        for i in range(len(meteor)):
            meteor[i].move(deltatime, HEIGHT)

        background01.move(deltatime, HEIGHT)
        background02.move(deltatime, HEIGHT)

    # Удаляем ракеты
    if frame % 25 == 0:
        for i in range(len(rocket) - 1, -1, -1):
            if rocket[i].enabled == False:
                del rocket[i]

        for i in range(len(meteor) - 1, -1, -1):
            if meteor[i].enabled == False:
                del meteor[i]

        for i in range(len(explosions) - 1, -1, -1):
            if explosions[i].enabled == False:
                del explosions[i]

        if (randint(0, 100) < 30 and not pause):
            meteor.append(Meteor(randint(0, WIDTH), -40, font, dict.dict[dict.current_word][0]))


    # Количество кадров
    frame += 1
    if frame > 10000:
        frame = 0

    # Задержка для синхронизации FPS
    # Время, прошедшее между кадрами
    deltatime = clock.tick(FPS) / 1000


# Конец истории
pygame.quit()