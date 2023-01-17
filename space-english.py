# Подключаем pygame
import pygame
import setup

from setup import *
from model.ship import Ship
from model.fuels import Fuels
from model.rocket import Rocket
from model.background import Background
from model.meteor import Meteor
from model.explosions import Explosions
from dict.dict import Dict
from services.font import Font
from random import randint
from services.sound import Sound
from view import View
from model.heart import Heart
from model.gas import Gas

pygame.init()
size = [WIDTH, HEIGHT]

pygame.display.set_caption("Space English")

if fullScreen:
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
sound = Sound(pygame)

frame = 0
ship = Ship()
rocket = []
pause = False

meteor = []
heart = []
gas = []
fuels = Fuels()


explosions = []
v = View('png/obloshka.png')
obj = View('png/end.png')

# ГЛАВНЫЙ ЦИКЛ
while playGame:

    if state == VIEW_SCREEN:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                playGame = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    playGame = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    state = PLAY_GAME
                    dict = Dict(level, sound)
                    sound.play(Sound.OKGO)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sound/music.mp3')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
        scene.fill(BLACK)
        v.draw(scene)
        pygame.display.flip()

    elif state == END_GAME:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                playGame = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    playGame = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    playGame = False
        scene.fill(BLACK)
        obj.draw(scene)
        pygame.display.flip()

    elif state == NEXT_LEVEL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playGame = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playGame = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dict = Dict(level, sound)
                    frame = 0
                    ship = Ship()
                    rocket = []
                    pause = False

                    meteor = []
                    explosions = []
                    state = PLAY_GAME

        scene.fill(BLACK)

        background01.draw(scene, ship.x)
        background02.draw(scene, ship.x)

        scene.blit(font.getBigText("HAPPY", f"ПОЗДРАВЛЯЕМ!", level_color[level]), (138, 400))
        scene.blit(font.getSystemText("NEXTLEVEL", f"Следующий уровень: {level + 1}", (200, 200, 200)), (115, 450))

        pygame.display.flip()

    elif state == PLAY_GAME:
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
                elif (event.key == pygame.K_1):
                    i = 0
                    while i < len(dict.marker_chars):
                        if (dict.marker_chars[i] == False):
                            dict.marker_chars[i] = True
                            i = len(dict.marker_chars)
                        i += 1

            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1 and not pause):
                    rocket.append(Rocket(ship.x, ship.y))
                    sound.play(Sound.SHOOT)
                if (event.button == 3 and not pause):
                    rocket.append(Rocket(ship.x + 48, ship.y))
                    sound.play(Sound.SHOOT)
        if (pygame.mouse.get_pos()[0] < ship.x and not pause):
            ship.move_left(deltatime)
        elif (pygame.mouse.get_pos()[0] > ship.x + 64 and not pause):
            ship.move_right(deltatime)
        # Очищаем сцену
        scene.fill(BLACK)

        background01.draw(scene, ship.x)
        background02.draw(scene, ship.x)

        fuels.draw(scene)

        ship.draw(scene)

        for i in range(len(meteor)):
            meteor[i].draw(scene)
            res = meteor[i].is_collision_ship(ship)

            # Отображаем картинку финала
            if (ship.is_dead()):
                state = END_GAME

            if (res == True):
                explosions.append(Explosions(meteor[i].x - 16, meteor[i].y - 16))

            res = meteor[i].is_collision(rocket)
            if (res != None):
                sound.play(Sound.EXPL)
                if (len(meteor[i].number) > 0):
                    for j in range(len(meteor[i].number)):
                        dict.marker_chars[meteor[i].number[j]] = not dict.marker_chars[meteor[i].number[j]]
                    sound.play(Sound.TAKE)
                explosions.append(Explosions(meteor[i].x - 16, meteor[i].y - 16))
                res.enabled = False
                meteor[i].enabled = False

        for i in range(len(heart)):
            heart[i].draw(scene)
            heart[i].move(deltatime, HEIGHT)

            res = heart[i].is_collision_ship(ship)
            if (res == True):
                explosions.append(Explosions(heart[i].x - 16, heart[i].y - 16))

        for i in range(len(rocket)):
            rocket[i].draw(scene)

        for i in range(len(gas)):
            gas[i].draw(scene)
            res = gas[i].is_collision_ship(ship)

            if (res == True):
                setup.fuel += 1000
                if (setup.fuel > 1000):
                    setup.fuel = 1000


        for i in range(len(explosions)):
            explosions[i].draw(scene, deltatime)

        scene.blit(font.getBigText("WORD", dict.get_word(1), (255, 255, 255)), (10, 10))
        scene.blit(font.getBigText("LVL", f"Уровень: {level + 1}", level_color[level]), (300, 10))
        scene.blit(font.getSystemText("NUMWORD", f"Слово: {dict.current_word + 1} из 5", (200, 200, 200)), (10, 815))

        for i in range(len(dict.marker_chars)):
            if (dict.marker_chars[i]):
                scene.blit(font.getBigText("CH", dict.get_word(0)[i], (255, 255, 255)), (10 + i * 20, 50))
            else:
                scene.blit(font.getBigText("CH2", "*", (255, 255, 255)), (10 + i * 20, 50))

        # Когда слово собрано ПОЛНОСТЬЮ
        if (dict.is_word_complete()):
            # Увеличиваем номер слова
            # Если увеличить не получилось, значит,
            # в этой позиции всё прошли
            if (not dict.inc_number_word()):
                level += 1
                state = NEXT_LEVEL

        # Отрисовываем изображения
        pygame.display.flip()

        # Расчёты:
        # ...

        if not pause:

            # Уменьшаем топливо
            fuels.dec_fuel(deltatime)

            for i in range(len(rocket)):
                rocket[i].move(deltatime, frame)

            for i in range(len(meteor)):
                meteor[i].move(deltatime, HEIGHT)

            for i in range(len(gas)):
                gas[i].move(deltatime, HEIGHT)

            background01.move(deltatime, HEIGHT)
            background02.move(deltatime, HEIGHT)

        # Удаляем ракеты и добавляем метеоры
        if frame % 25 == 0:
            for i in range(len(rocket) - 1, -1, -1):
                if rocket[i].enabled == False:
                    del rocket[i]

            for i in range(len(gas) - 1, -1, -1):
                if gas[i].enabled == False:
                    del gas[i]

            for i in range(len(meteor) - 1, -1, -1):
                if meteor[i].enabled == False:
                    del meteor[i]

            for i in range(len(explosions) - 1, -1, -1):
                if explosions[i].enabled == False:
                    del explosions[i]

            for i in range(len(heart) - 1, -1, -1):
                if heart[i].enabled == False:
                    del heart[i]

            if (randint(0, 100) < 30 and not pause):
                meteor.append(Meteor(randint(0, WIDTH - 32), -40, font, dict.get_word(0), sound))

            # if (randint(0, 100) < 20):
            if (randint(0, 100) < 20 and len(heart) == 0 and ship.frame > 0 and not pause):
                heart.append(Heart(randint(0, WIDTH - 32), -40, sound))

            if (randint(0, 100) < 10 and len(gas) == 0 and not pause):
                # gas.append(Gas(randint(0, WIDTH - 16), -40, sound))
                gas.append(Gas(ship.x, -40, sound))

    # Количество кадров
    frame += 1
    if frame > 10000:
        frame = 0

    # Задержка для синхронизации FPS
    # Время, прошедшее между кадрами
    deltatime = clock.tick(FPS) / 1000

# Конец истории

pygame.quit()
