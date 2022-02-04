import os

import pygame


def mountain_choise():
    pygame.init()
    green = (0, 128, 0)
    black = (0, 0, 0)
    fps = 60
    WIDTH, HEIGHT = 900, 500
    background_image = pygame.image.load(os.path.join("combat photos", "chose.png"))
    background_image = pygame.transform.scale(background_image, (900, 500))
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            WIN.fill(green)
            WIN.blit(background_image, (0, 0))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 29 <= mouse[0] <= 234 and 229 <= mouse[1] <= 354:
                    return "snake"
                if 342 <= mouse[0] <= 546 and 229 <= mouse[1] <= 354:
                    return "fox"
                if 655 <= mouse[0] <= 852 and 229 <= mouse[1] <= 354:
                    return "crocodile"


# mountain_choise()
