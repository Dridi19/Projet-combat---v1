import os
import time
from random import randint

import pygame

green = (0, 128, 0)
black = (0, 0, 0)
fps = 60
WIDTH, HEIGHT = 900, 500
quiz1 = pygame.image.load(os.path.join("quiz", "1.png"))
quiz1 = pygame.transform.scale(quiz1, (900, 500))

quiz2 = pygame.image.load(os.path.join("quiz", "2.png"))
quiz2 = pygame.transform.scale(quiz2, (900, 500))

quiz3 = pygame.image.load(os.path.join("quiz", "3.png"))
quiz3 = pygame.transform.scale(quiz3, (900, 500))

quiz4 = pygame.image.load(os.path.join("quiz", "4.png"))
quiz4 = pygame.transform.scale(quiz4, (900, 500))

quiz5 = pygame.image.load(os.path.join("quiz", "5.png"))
quiz5 = pygame.transform.scale(quiz5, (900, 500))

quiz6 = pygame.image.load(os.path.join("quiz", "6.png"))
quiz6 = pygame.transform.scale(quiz6, (900, 500))

quiz7 = pygame.image.load(os.path.join("quiz", "7.png"))
quiz7 = pygame.transform.scale(quiz7, (900, 500))

quiz8 = pygame.image.load(os.path.join("quiz", "8.png"))
quiz8 = pygame.transform.scale(quiz8, (900, 500))

quiz9 = pygame.image.load(os.path.join("quiz", "9.png"))
quiz9 = pygame.transform.scale(quiz9, (900, 500))

quiz10 = pygame.image.load(os.path.join("quiz", "10.png"))
quiz10 = pygame.transform.scale(quiz10, (900, 500))

quiz11 = pygame.image.load(os.path.join("quiz", "11.png"))
quiz11 = pygame.transform.scale(quiz11, (900, 500))

quiz12 = pygame.image.load(os.path.join("quiz", "12.png"))
quiz12 = pygame.transform.scale(quiz12, (900, 500))

vrai_image = pygame.image.load(os.path.join("quiz", "vrai.png"))
vrai_image = pygame.transform.scale(vrai_image, (42, 20))

faux_image = pygame.image.load(os.path.join("quiz", "faux.png"))
faux_image = pygame.transform.scale(faux_image, (42, 20))


def run(card, vrai):
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    fonta = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()
    w = 0
    again = True
    while again:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            WIN.fill(green)
            WIN.blit(card, (0, 0))
            pygame.display.update()
            choice = ""
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 66 <= mouse[0] <= 385 and 356 <= mouse[1] <= 408:
                    choice = "a"

                if 516 <= mouse[0] <= 835 and 356 <= mouse[1] <= 408:
                    choice = "c"

                if 54 <= mouse[0] <= 385 and 421 <= mouse[1] <= 477:
                    choice = "b"

                if 516 <= mouse[0] <= 835 and 421 <= mouse[1] <= 477:
                    choice = "d"

            if choice in ["a", "b", "c", "d"]:
                if vrai == "a":
                    WIN.blit(vrai_image, (112, 370))
                    WIN.blit(faux_image, (560, 370))
                    WIN.blit(faux_image, (560, 440))
                    WIN.blit(faux_image, (105, 440))

                if vrai == "c":
                    WIN.blit(faux_image, (112, 370))
                    WIN.blit(vrai_image, (560, 370))
                    WIN.blit(faux_image, (560, 440))
                    WIN.blit(faux_image, (105, 440))

                if vrai == "d":
                    WIN.blit(faux_image, (112, 370))
                    WIN.blit(faux_image, (560, 370))
                    WIN.blit(vrai_image, (560, 440))
                    WIN.blit(faux_image, (105, 440))

                if vrai == "b":
                    WIN.blit(faux_image, (112, 370))
                    WIN.blit(faux_image, (560, 370))
                    WIN.blit(faux_image, (560, 440))
                    WIN.blit(vrai_image, (105, 440))

                pygame.display.update()
                time.sleep(2)
                if choice == vrai:
                    return "won"
                else:
                    return "lost"

            if event.type == pygame.QUIT:
                again = False
    return 0


def to_image(card_number):
    if card_number == 1:
        return quiz1, "a"

    if card_number == 2:
        return quiz2, "c"

    if card_number == 3:
        return quiz3, "d"

    if card_number == 4:
        return quiz4, "b"
    if card_number == 5:
        return quiz5, "a"

    if card_number == 6:
        return quiz6, "d"

    if card_number == 7:
        return quiz7, "c"

    if card_number == 8:
        return quiz8, "a"

    if card_number == 9:
        return quiz9, "b"

    if card_number == 10:
        return quiz10, "b"

    if card_number == 11:
        return quiz11, "c"

    if card_number == 12:
        return quiz12, "a"


def quiz(list):
    if len(list) == 12:
        return "2"
    score = 0
    for i in range(4):
        c = randint(1, 12)
        while c in list:
            c = randint(1, 12)
        list.append(c)
        card, vrai = to_image(c)
        b = run(card, vrai)
        if b == "won":
            score = score + 1
    if score > 2:
        return 1, list
    else:
        return -1,list
