import os
import time

import pygame
from pygame import event
from sqlalchemy import true

import photo

green = (0, 128, 0)
black = (0, 0, 0)
fps = 60
WIDTH, HEIGHT = 900, 500
# image
snake_hand = pygame.image.load(os.path.join("combat photos", "snake_hand.png"))
snake_hand = pygame.transform.scale(snake_hand, (900, 500))

snake_axe = pygame.image.load(os.path.join("combat photos", "snake_axe.png"))
snake_axe = pygame.transform.scale(snake_axe, (900, 500))

snake_battlestaff = pygame.image.load(
    os.path.join("combat photos", "snake_battlestaff.png")
)
snake_battlestaff = pygame.transform.scale(snake_battlestaff, (900, 500))

snake_pistol = pygame.image.load(os.path.join("combat photos", "snake_pistol.png"))
snake_pistol = pygame.transform.scale(snake_pistol, (900, 500))

crocodile_hand = pygame.image.load(os.path.join("combat photos", "crocodile_hand.png"))
crocodile_hand = pygame.transform.scale(crocodile_hand, (900, 500))

crocodile_pistol = pygame.image.load(
    os.path.join("combat photos", "crocodile_pistol.png")
)
crocodile_pistol = pygame.transform.scale(crocodile_pistol, (900, 500))

crocodile_battlestaff = pygame.image.load(
    os.path.join("combat photos", "crocodile_battlestaff.png")
)
crocodile_battlestaff = pygame.transform.scale(crocodile_battlestaff, (900, 500))

crocodile_axe = pygame.image.load(os.path.join("combat photos", "crocodile_axe.png"))
crocodile_axe = pygame.transform.scale(crocodile_axe, (900, 500))

fox_hand = pygame.image.load(os.path.join("combat photos", "fox_hand.png"))
fox_hand = pygame.transform.scale(fox_hand, (900, 500))

fox_pistol = pygame.image.load(os.path.join("combat photos", "fox_pistol.png"))
fox_pistol = pygame.transform.scale(fox_pistol, (900, 500))

fox_axe = pygame.image.load(os.path.join("combat photos", "fox_axe.png"))
fox_axe = pygame.transform.scale(fox_axe, (900, 500))

fox_battlestaff = pygame.image.load(
    os.path.join("combat photos", "fox_battlestaff.png")
)
fox_battlestaff = pygame.transform.scale(fox_battlestaff, (900, 500))


def combat(p1):
    pygame.init()
    fonta = pygame.font.SysFont("comicsans", 25)
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    if p1.monster == "snake":
        monster_hp = "100"
        monster_dmg = 10
    if p1.monster == "fox":
        monster_hp = "150"
        monster_dmg = 25
    if p1.monster == "crocodile":
        monster_hp = "200"
        monster_dmg = 35

    used_weapon, image = weapon_choice(p1.weapons, p1.monster, WIN, fonta)
    used_potion = potion_choice(p1.monster, p1.potions, image, WIN, fonta)

    if used_weapon == "battlestaff":
        player_dmg = 15
    if used_weapon == "axe":
        player_dmg = 25
    if used_weapon == "pistol":
        player_dmg = 45
    w,p1.hp = run(p1, monster_dmg, image, WIN, fonta,used_potion,player_dmg,monster_hp)
    if w == "win":
        if p1.monster == "snake":
            (p1.items).append("snake")
        if p1.monster == "fox":
            (p1.items).append("fox")
        if (p1.monster) == "crocodile":
            (p1.items).append("crocodile")
    return p1


def run(
    p1, monster_dmg, image, WIN, fonta,potions,player_dmg,monster_hp):
    s = 0
    d = 0
    clock = pygame.time.Clock()
    if potions == "speed":
        s = 3
    if potions == "defence":
        d = 3
    run = True
    while run:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            text1 = fonta.render("Choose your next step", True, black)
            text2 = fonta.render("Attack", True, black)
            text3 = fonta.render("Run", True, black)
            text4 = fonta.render(str(p1.hp), True, black)
            text5 = fonta.render(str(monster_hp), True, black)
            WIN.fill(green)
            WIN.blit(image, (0, 0))
            WIN.blit(text1, (320, 190))
            WIN.blit(text2, (298, 300))
            WIN.blit(text3, (470, 300))
            WIN.blit(text4, (215, 80))
            WIN.blit(text5, (716, 72))
            pygame.display.update()
            if int(p1.hp) == 0:
                time.sleep(2)
                return "lose",p1.hp
            if int(monster_hp) == 0:
                time.sleep(2)
                return "win",p1.hp
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 297 <= mouse[0] <= 384 and 300 <= mouse[1] <= 340:
                    if d == s == 0:
                        monster_hp = str(int(monster_hp) - int(player_dmg))
                        p1.hp = str(int(p1.hp) - int(monster_dmg))
                    if s > 0:
                        monster_hp = str(int(monster_hp) - int(player_dmg * 2))
                        s = s - 1
                        p1.hp = str(int(p1.hp) - int(monster_dmg))
                    if d > 0:
                        monster_hp = str(int(monster_hp) - int(player_dmg))
                        d = d - 1
                        p1.hp = str(int(p1.hp) - int((monster_dmg * 70) / 100))
                    if int(p1.hp) < 0:
                        p1.hp = "0"
                    if int(monster_hp) < 0:
                        monster_hp = "0"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 460 <= mouse[0] <= 520 and 300 <= mouse[1] <= 340:
                    return "draw",p1.hp


def weapon_choice(weapons, monster, WIN, fonta):
    clock = pygame.time.Clock()
    if monster == "snake":
        image = snake_hand
    if monster == "fox":
        image = fox_hand
    if monster == "crocodile":
        image = crocodile_hand
    run = True
    while run:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            text2 = fonta.render("choose your weapon", 1, black)
            text1 = fonta.render("Batllestaff", 1, black)
            WIN.fill(green)
            WIN.blit(image, (0, 0))
            WIN.blit(text2, (320, 190))
            WIN.blit(text1, (228, 300))
            if "axe" in weapons:
                axe = fonta.render("axe", 1, black)
                WIN.blit(axe, (410, 300))
            if "pistol" in weapons:
                pistol = fonta.render("pistol", 1, black)
                WIN.blit(pistol, (560, 300))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (
                    228 <= mouse[0] <= 316
                    and 308 <= mouse[1] <= 327
                    and "battlestaff" in weapons
                ):
                    if monster == "snake":
                        image = snake_battlestaff
                    if monster == "fox":
                        image = fox_battlestaff
                    if monster == "crocodile":
                        image = crocodile_battlestaff
                    return "battlestaff", image
                if (
                    409 <= mouse[0] <= 455
                    and 308 <= mouse[1] <= 327
                    and "axe" in weapons
                ):
                    if monster == "snake":
                        image = snake_axe
                    if monster == "fox":
                        image = fox_axe
                    if monster == "crocodile":
                        image = crocodile_axe
                    return "axe", image
                if (
                    560 <= mouse[0] <= 625
                    and 308 <= mouse[1] <= 327
                    and "pistol" in weapons
                ):
                    if monster == "snake":
                        image = snake_pistol
                    if monster == "fox":
                        image = fox_pistol
                    if monster == "crocodile":
                        image = crocodile_pistol
                    return "pistol", image


def potion_choice(monster, potions, image, WIN, fonta):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            text2 = fonta.render("choose your potion", 1, black)
            text1 = fonta.render("none", 1, black)
            WIN.fill(green)
            WIN.blit(image, (0, 0))
            WIN.blit(text2, (320, 190))
            WIN.blit(text1, (228, 300))
            if "speed" in potions:
                speed = fonta.render("speed", 1, black)
                WIN.blit(speed, (410, 300))
            if "defence" in potions:
                defence = fonta.render("defence", 1, black)
                WIN.blit(defence, (560, 300))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 217 <= mouse[0] <= 291 and 297 <= mouse[1] <= 341:
                    return "none"
                if (
                    551 <= mouse[0] <= 662
                    and 297 <= mouse[1] <= 341
                    and "defence" in potions
                ):
                    potions.remove("defence")
                    return "defence"
                if (
                    401 <= mouse[0] <= 487
                    and 297 <= mouse[1] <= 341
                    and "speed" in potions
                ):
                    potions.remove("speed")
                    return "speed"


# combat("snake", ["axe", "pistol", "battlestaff"], ["defence", "speed"], "100", [])
