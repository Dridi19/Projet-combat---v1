import os

import pygame


def market(p1):
    pygame.init()
    green = (0, 128, 0)
    black = (0, 0, 0)
    fps = 60
    list = []
    WIDTH, HEIGHT = 900, 500
    ##image
    background_image = pygame.image.load(os.path.join("markett", "market.png"))
    background_image = pygame.transform.scale(background_image, (900, 500))

    fox_image = pygame.image.load(os.path.join("markett", "fox.png"))
    fox_image = pygame.transform.scale(fox_image, (374, 60))

    snake_image = pygame.image.load(os.path.join("markett", "snake.png"))
    snake_image = pygame.transform.scale(snake_image, (374, 60))

    crocodile_image = pygame.image.load(os.path.join("markett", "crocodile.png"))
    crocodile_image = pygame.transform.scale(crocodile_image, (374, 60))

    pistol_image = pygame.image.load(os.path.join("markett", "pistol.png"))
    pistol_image = pygame.transform.scale(pistol_image, (374, 60))

    axe_image = pygame.image.load(os.path.join("markett", "axe.png"))
    axe_image = pygame.transform.scale(axe_image, (374, 60))

    speed_image = pygame.image.load(os.path.join("markett", "speed.png"))
    speed_image = pygame.transform.scale(speed_image, (374, 60))

    defence_image = pygame.image.load(os.path.join("markett", "defence.png"))
    defence_image = pygame.transform.scale(defence_image, (374, 60))

    quit_image = pygame.image.load(os.path.join("markett", "quit.png"))
    quit_image = pygame.transform.scale(quit_image, (100, 60))

    ##
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    fonta = pygame.font.SysFont("comicsans", 50)

    def runa(p1):
        clock = pygame.time.Clock()
        run = True
        w = 0
        again = True
        text = fonta
        while again:
            clock.tick(fps)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return p1
                WIN.fill(green)
                WIN.blit(background_image, (0, 0))
                if "crocodile" in p1.items:
                    WIN.blit(crocodile_image, (7, 116))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 7 <= mouse[0] <= 380 and 118 <= mouse[1] <= 175:
                            p1.coins = p1.coins + 90
                            (p1.items).remove("crocodile")

                if "fox" in p1.items:
                    WIN.blit(fox_image, (7, 230))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 8 <= mouse[0] <= 380 and 230 <= mouse[1] <= 287:
                            p1.coins = p1.coins + 50
                            (p1.items).remove("fox")
                if "snake" in p1.items:
                    WIN.blit(snake_image, (7, 350))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 8 <= mouse[0] <= 380 and 351 <= mouse[1] <= 406:
                            p1.coins = p1.coins + 25
                            p1.items.remove("snake")
                if "pistol" not in p1.weapons:
                    WIN.blit(pistol_image, (511, 290))
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and int(p1.coins) >= 80
                    ):
                        if 511 <= mouse[0] <= 882 and 289 <= mouse[1] <= 349:
                            p1.coins = p1.coins - 80
                            p1.weapons.append("pistol")
                if "defence" not in p1.potions:
                    WIN.blit(defence_image, (511, 120))
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and int(p1.coins) >= 10
                    ):
                        if 511 <= mouse[0] <= 882 and 120 <= mouse[1] <= 176:
                            p1.coins = p1.coins - 10
                            (p1.potions).append("defence")
                if "speed" not in (p1.potions):
                    WIN.blit(speed_image, (511, 195))
                    if event.type == pygame.MOUSEBUTTONDOWN and p1.coins >= 10:
                        if 511 <= mouse[0] <= 882 and 194 <= mouse[1] <= 252:
                            p1.coins = p1.coins - 10
                            (p1.potions).append("speed")

                if "axe" not in p1.weapons:
                    WIN.blit(axe_image, (511, 370))
                    if event.type == pygame.MOUSEBUTTONDOWN and p1.coins >= 40:
                        if 511 <= mouse[0] <= 882 and 370 <= mouse[1] <= 428:
                            p1.coins = p1.coins - 40
                            (p1.weapons).append("axe")
                text2 = fonta.render("coins = " + str(p1.coins), True, black)
                WIN.blit(text2, (300, 30))
                WIN.blit(quit_image, (380, 420))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 380 <= mouse[0] <= 480 and 420 <= mouse[1] <= 480:
                        return p1

    p1 = runa(p1)
    print(p1)
    return p1

# market(50, ["axe", "pistol", "batllesraff"], [], ["snake", "fox", "crocodile"])
