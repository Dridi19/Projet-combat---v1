import os
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from typing import List


def hospital(p1):
    pygame.init()
    green = (0, 128, 0)
    black = (0, 0, 0)
    fps = 60
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    background_image = pygame.image.load(os.path.join("hospital.png"))
    background_image = pygame.transform.scale(background_image, (900, 500))
    fonta = pygame.font.SysFont("comicsans", 50)

    def run(p1):
        clock = pygame.time.Clock()
        is_running = True
        while is_running:
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and int(p1.hp) < 100:
                    if 24 <= mouse[0] <= 90 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 1:
                            p1.hp = int(p1.hp) + 10
                            p1.coins = int(p1.coins) - 1
                    if 123 <= mouse[0] <= 191 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 2:
                            p1.hp = int(p1.hp) + 20
                            p1.coins = int(p1.coins) - 2
                    if 224 <= mouse[0] <= 290 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 3:
                            p1.hp = int(p1.hp) + 30
                            p1.coins = int(p1.coins) - 3
                    if 323 <= mouse[0] <= 439 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 4:
                            p1.hp = int(p1.hp) + 40
                            p1.coins = int(p1.coins) - 4
                    if 418 <= mouse[0] <= 481 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 5:
                            p1.hp = int(p1.hp) + 50
                            p1.coins = int(p1.coins) - 5
                    if 515 <= mouse[0] <= 582 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 6:
                            p1.hp = int(p1.hp) + 60
                            p1.coins = int(p1.coins) - 6
                    if 616 <= mouse[0] <= 685 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 7:
                            p1.hp = int(p1.hp) + 70
                            p1.coins = int(p1.coins) - 7
                    if 711 <= mouse[0] <= 785 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 8:
                            p1.hp = int(p1.hp) + 80
                            p1.coins = int(p1.coins) - 8
                    if 814 <= mouse[0] <= 880 and 415 <= mouse[1] <= 461:
                        if int(p1.coins) >= 9:
                            p1.hp = int(p1.hp) + 90
                            p1.coins = int(p1.coins) - 9
                    if int(p1.hp) > 100:
                        p1.hp = 100
                WIN.fill(green)
                WIN.blit(background_image, (0, 0))
                text1 = fonta.render(str(p1.hp), True, black)
                text2 = fonta.render(str(p1.coins), True, black)
                WIN.blit(text1, (230, 1))
                WIN.blit(text2, (650, 1))
                pygame.display.update()

        return p1

    p1 = run(p1)
    return p1
