import os

import pygame


def current_position(last_position):
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    blue = (0, 0, 255)
    fps = 60
    h_w = 530
    h_h = 200
    if last_position == "hospital":
        h_w = 650
        h_h = 280
    if last_position == "market":
        h_w = 390
        h_h = 360
    if last_position == "combat":
        h_w = 250
        h_h = 260
    if last_position == "casino":
        h_w = 480
        h_h = 27

    def draw_window():
        ##mos pos
        WIN.fill(blue)
        WIN.blit(background_image, (0, 0))
        WIN.blit(casino_image, (420, 10))
        WIN.blit(market_image, (310, 310))
        WIN.blit(hospital_image, (550, 200))
        WIN.blit(mountain_image, (130, 120))
        WIN.blit(spawn_image, (430, 130))
        WIN.blit(here_image, (h_w, h_h))
        pygame.display.update()
        ###

    ##photos
    background_image = pygame.image.load(os.path.join("photo", "map.png"))
    background_image = pygame.transform.scale(background_image, (900, 500))

    casino_image = pygame.image.load(os.path.join("photo", "casino.png"))
    casino_image = pygame.transform.scale(casino_image, (170, 130))

    market_image = pygame.image.load(os.path.join("photo", "market.png"))
    market_image = pygame.transform.scale(market_image, (220, 210))

    mountain_image = pygame.image.load(os.path.join("photo", "mountain.png"))
    mountain_image = pygame.transform.scale(mountain_image, (300, 354))

    hospital_image = pygame.image.load(os.path.join("photo", "hospital.png"))
    hospital_image = pygame.transform.scale(hospital_image, (255, 244))

    spawn_image = pygame.image.load(os.path.join("photo", "spawn.png"))
    spawn_image = pygame.transform.scale(spawn_image, (255, 244))

    here_image = pygame.image.load(os.path.join("photo", "here.png"))
    here_image = pygame.transform.scale(here_image, (50, 44))
    # photosss

    def runa():
        exit = 0
        clock = pygame.time.Clock()
        run = True
        new_position = ""
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = 1
                    run = False


            draw_window()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 466 <= mouse[0] <= 543 and 47 <= mouse[1] <= 90:
                    if last_position != "casino":
                        new_position = "casino"

                if 380 <= mouse[0] <= 455 and 387 <= mouse[1] <= 430:
                    if last_position != "market":
                        new_position = "market"

                if 640 <= mouse[0] <= 716 and 307 <= mouse[1] <= 340:
                    if last_position != "hospital":
                        new_position = "hospital"

                if 235 <= mouse[0] <= 326 and 277 <= mouse[1] <= 314:
                    if last_position != "mountain combat":
                        new_position = "combat"
            if len(new_position) > 1:
                run = False
        if not (run):
            pygame.quit()
        pygame.quit()
        return new_position,exit

    a,exit = runa()
    return a,exit


# position = current_position("spawn")
# print(position)
