import os

import pygame

from Blackjack import blackjack
from Quiz import quiz


def casino(player_coins):
    pygame.init()
    i = 0
    while i < 10:
        player_coins, run = runa(player_coins)
        i = i + 1
    return player_coins


def runa(player_coins):
    green = (0, 128, 0)
    black = (0, 0, 0)
    fps = 60
    list_ = []
    WIDTH, HEIGHT = 900, 500
    background_image = pygame.image.load(os.path.join("", "casino.png"))
    background_image = pygame.transform.scale(background_image, (900, 500))

    again_image = pygame.image.load(os.path.join("", "again.png"))
    again_image = pygame.transform.scale(again_image, (900, 500))
    fonta = pygame.font.SysFont("comicsans", 50)

    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    w = 0
    betting_coins = "0"
    again = True
    while again:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            WIN.fill(green)
            WIN.blit(again_image, (0, 0))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 142 <= mouse[0] <= 240 and 219 <= mouse[1] <= 278:
                    again = False
                if 633 <= mouse[0] <= 750 and 219 <= mouse[1] <= 280:
                    return player_coins, False
            if event.type == pygame.QUIT:
                return player_coins, False

    while run:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if (
                    586 <= mouse[0] <= 740
                    and 365 <= mouse[1] <= 373
                    and int(betting_coins) <= int(player_coins)
                ):
                    game = "blackjack"
                    run = False
                if (
                    145 <= mouse[0] <= 235
                    and 344 <= mouse[1] <= 390
                    and int(betting_coins) <= int(player_coins)
                ):
                    game = "quiz"
                    run = False

            if event.type == pygame.QUIT:
                run = False
            text1 = fonta.render(betting_coins, True, (0, 200, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    betting_coins = betting_coins[:-1]
                else:
                    betting_coins += event.unicode
            WIN.fill(green)
            WIN.blit(background_image, (0, 0))
            WIN.blit(text1, (420, 140))
            pygame.display.update()
    if game == "blackjack":
        w = blackjack()
        print(w)
    if game == "quiz":
        w, lista = quiz(list_)
        print(w)
    if w == 1:
        return int(betting_coins) + int(player_coins), True
    if w == -1:
        return int(player_coins) - int(betting_coins), True
    if w == 2:
        return int(player_coins), True
