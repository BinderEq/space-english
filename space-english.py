# Подключаем pygame
from setup import *
from model.ship import Ship


pygame.init()
size = [WIDTH, HEIGHT]
pygame.display.set_caption("Space English")
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ship = Ship()

# ГЛАВНЫЙ ЦИКЛ
while (playGame):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            playGame = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                playGame = False
            elif (event.key == pygame.K_LEFT):
                ship.move_left()
            elif (event.key == pygame.K_RIGHT):
                ship.move_right()
            elif (event.key == pygame.K_UP):
                print("ВВЕРХ")
            elif (event.key == pygame.K_DOWN):
                print("ВНИЗ")

    if (pygame.mouse.get_pos()[0] < ship.x):
        ship.move_left()
    elif (pygame.mouse.get_pos()[0] > ship.x + 64):
        ship.move_right()
    # Очищаем сцену
    scene.fill(BLACK)
    ship.draw(scene)
    # Отрисовываем изображения
    pygame.display.flip()

    # Расчёты:
    # ...

    # Задержка для синхронизации FPS
    clock.tick(FPS)

# Конец истории
pygame.quit()