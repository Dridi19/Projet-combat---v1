import os
import time
from random import randint

import pygame
from pygame import event, font
from pygame.constants import GL_GREEN_SIZE

import bj
import photo


def blackjack():
    run()


pygame.init()
green = (0, 128, 0)
black = (0, 0, 0)
fps = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
b2_image = pygame.image.load(os.path.join("bj", "2.png"))
b2_image = pygame.transform.scale(b2_image, (90, 80))

b3_image = pygame.image.load(os.path.join("bj", "3.png"))
b3_image = pygame.transform.scale(b3_image, (90, 80))

b4_image = pygame.image.load(os.path.join("bj", "4.png"))
b4_image = pygame.transform.scale(b4_image, (90, 80))

b5_image = pygame.image.load(os.path.join("bj", "5.png"))
b5_image = pygame.transform.scale(b5_image, (90, 80))

b7_image = pygame.image.load(os.path.join("bj", "7.png"))
b7_image = pygame.transform.scale(b7_image, (90, 80))

b6_image = pygame.image.load(os.path.join("bj", "6.png"))
b6_image = pygame.transform.scale(b6_image, (90, 80))

b8_image = pygame.image.load(os.path.join("bj", "8.png"))
b8_image = pygame.transform.scale(b8_image, (90, 80))

b9_image = pygame.image.load(os.path.join("bj", "9.png"))
b9_image = pygame.transform.scale(b9_image, (90, 80))

b10_image = pygame.image.load(os.path.join("bj", "10.png"))
b10_image = pygame.transform.scale(b10_image, (90, 80))

bj_image = pygame.image.load(os.path.join("bj", "j.png"))
bj_image = pygame.transform.scale(bj_image, (90, 80))

ba_image = pygame.image.load(os.path.join("bj", "a.png"))
ba_image = pygame.transform.scale(ba_image, (90, 80))

bk_image = pygame.image.load(os.path.join("bj", "k.png"))
bk_image = pygame.transform.scale(bk_image, (90, 80))

bq_image = pygame.image.load(os.path.join("bj", "q.png"))
bq_image = pygame.transform.scale(bq_image, (90, 80))

lost_image = pygame.image.load(os.path.join("bj", "lose.jpg"))
lost_image = pygame.transform.scale(lost_image, (140, 90))

win_image = pygame.image.load(os.path.join("bj", "win.jpg"))
win_image = pygame.transform.scale(win_image, (140, 90))


def draw_window(c, p_cards, bot_cards):
    ##mos pos
    WIN.fill(green)
    fonta = pygame.font.SysFont("comicsans", 20)
    text1 = fonta.render("Hit", 1, black)
    text2 = fonta.render("Stand", 1, black)
    psum = fonta.render(str(c), 1, black)
    WIN.blit(text1, (280, 400))
    WIN.blit(text2, (550, 400))
    WIN.blit(psum, (430, 400))
    p_h = 300
    p_w = 300
    b_h = 300
    b_w = 100
    for b in p_cards:
        WIN.blit(b, (p_h, p_w))
        p_h = p_h + 50
    for b in bot_cards:
        WIN.blit(b, (b_h, b_w))
        b_h = b_h + 50

    pygame.display.update()


p_cards = []
bot_cards = []
p_cards.append(randint(2, 14))
p_cards.append(randint(2, 14))
bot_cards.append(randint(2, 14))


def run():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouse = pygame.mouse.get_pos()
            c = sum(p_cards)
            bot_sum = sum(bot_cards)
            pa_cards = cardtoimage(p_cards)
            bota_cards = cardtoimage(bot_cards)
            draw_window(c, pa_cards, bota_cards)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p_cards.append(randint(2, 14))
                if event.key == pygame.K_DOWN:
                    while bot_sum < c and bot_sum <= 17:
                        bot_cards.append(randint(2, 14))
                        bot_sum = sum(bot_cards)
            if (bot_sum > c or bot_sum > 17) and bot_sum <= 21 and c <= 21:
                if bot_sum > c:
                    WIN.blit(lost_image, (400, 200))
                    pygame.display.update()

                if bot_sum < c:
                    WIN.blit(win_image, (400, 200))
                    pygame.display.update()
                if bot_sum == c:
                    WIN.blit(lost_image, (400, 200))
                    pygame.display.update()

            if c > 21:
                WIN.blit(lost_image, (400, 200))
                pygame.display.update()
            if bot_sum > 21:
                WIN.blit(win_image, (400, 200))
                pygame.display.update()

    pygame.quit()


def cardtoimage(p_cards):
    output = []
    for i in p_cards:
        if i == 2:
            output.append(b2_image)
        if i == 3:
            output.append(b3_image)
        if i == 4:
            output.append(b4_image)
        if i == 5:
            output.append(b5_image)
        if i == 6:
            output.append(b6_image)
        if i == 7:
            output.append(b7_image)
        if i == 8:
            output.append(b8_image)
        if i == 9:
            output.append(b9_image)
        if i == 10:
            output.append(b10_image)
        if i == 11:
            output.append(bj_image)
        if i == 12:
            output.append(bk_image)
        if i == 13:
            output.append(bq_image)
        if i == 14:
            output.append(ba_image)
    return output


def sum(player_cards):
    sum = 0
    A_counter = 0
    card_10 = [10, 11, 12, 13]
    for i in player_cards:
        if i in card_10:
            sum = sum + 10
        elif i == 14:
            A_counter = A_counter + 1
        else:
            sum = sum + i
    if (sum + A_counter * 11) < 22:
        sum = sum + A_counter * 11
    else:
        sum = sum + 1 * A_counter
    return sum


blackjack()
