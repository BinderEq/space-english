# Подключаем pygame
import pygame
from setup import *



pygame.init()
size = [WIDTH, HEIGHT]
pygame.display.set_caption("Space English")
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# ГЛАВНЫЙ ЦИКЛ
while (playGame):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            playGame = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                playGame = False
            elif (event.key == pygame.K_LEFT):
                print("ВЛЕВО")
            elif (event.key == pygame.K_RIGHT):
                print("ВПРАВО")
            elif (event.key == pygame.K_UP):
                print("ВВЕРХ")
            elif (event.key == pygame.K_DOWN):
                print("ВНИЗ")

    # Очищаем сцену
    scene.fill(BLACK)

    # Отрисовываем изображения
    pygame.display.flip()

    # Расчёты:
    # ...

    # Задержка для синхронизации FPS
    clock.tick(FPS)

# Конец истории
pygame.quit()