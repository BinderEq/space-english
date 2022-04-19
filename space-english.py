# Подключаем pygame
from setup import *
from model.ship import Ship
from model.rocket import Rocket

pygame.init()
size = [WIDTH, HEIGHT]
pygame.display.set_caption("Space English")
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ship = Ship()
rocket = []



# ГЛАВНЫЙ ЦИКЛ
while (playGame):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            playGame = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                playGame = False
            elif (event.key == pygame.K_LEFT):
                ship.move_left(deltatime)
            elif (event.key == pygame.K_RIGHT):
                ship.move_right(deltatime)
            elif (event.key == pygame.K_UP):
                print("ВВЕРХ")
            elif (event.key == pygame.K_DOWN):
                print("ВНИЗ")
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):
                rocket.append(Rocket(ship.x, ship.y))

    if (pygame.mouse.get_pos()[0] < ship.x):
        ship.move_left(deltatime)
    elif (pygame.mouse.get_pos()[0] > ship.x + 64):
        ship.move_right(deltatime)
    # Очищаем сцену
    scene.fill(BLACK)
    ship.draw(scene)
    for i in range(len(rocket)):
        rocket[i].draw(scene)
    # Отрисовываем изображения
    pygame.display.flip()

    # Расчёты:
    # ...
    for i in range(len(rocket)):
        rocket[i].move(deltatime)

    # Задержка для синхронизации FPS
    deltatime = clock.tick(FPS) / 1000

# Конец истории
pygame.quit()