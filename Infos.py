import pygame
import pygame.freetype  # Import the freetype module.

acceuil = [
    "Use the arrow up and arrow down ",
    "Welcome, your goal here is to buy THE GENIE LAMP",
    "so you can make 3 wishes.",
    " You are starting with 20 coins You will start with 100 HP and battlestaff as a weapon.",
    "your goal is to reach 200 coins",
    "make a step",
    "Places are : ",
    "Market, there you can buy weapons and potions ",
    "Hospital, there you can heal",
    "Casino, there you can gamble",
    "First mountain : contains easy monsters",
    "Second mountain : contains medium monsters",
    "Third mountains : contains hard monsters",
]
WIDTH, HEIGHT = 900, 500
blue = (0, 0, 255)
fps = 60
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 255)
orange = (255, 100, 0)


def draw_window(i, WIN):
    WIN.fill(white)
    fonta = pygame.font.SysFont("comicsans", 20)
    texta = fonta.render(acceuil[i], True, orange)
    WIN.blit(texta, (40, 200))
    pygame.display.update()


def run(i):
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    i = i + 1
                elif i >= 1 and event.key == pygame.K_DOWN:
                    i = i - 1
            if i == (len(acceuil) - 1):
                run = False
        draw_window(i, WIN)
        if i == len(acceuil):
            run = False
    pygame.quit()
    return


def info():
    i = 0
    run(i)
    return


# info()
