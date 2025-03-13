# d_stars.py
"""
title: create a starfield
author: Laksh Chopra
date-created: 2023-12-20
"""

if __name__ == "__main__":
    import pygame
    from a_template import Window
    from c_boxes import Box
    from random import randint
    pygame.init()

    WINDOW = Window("Starfield")
    STARS = []
    for i in range(200):
        WIDTH = randint(2, 5)
        STARS.append(Box(WIDTH, WIDTH))
        STARS[-1].setPOS(
            randint(0, WINDOW.getWidth() - WIDTH),
            randint(0, WINDOW.getHeight() - WIDTH)
        )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()
        for star in STARS:
            star.WASDmove(PRESSED_KEYS)
            #star.setColor((randint(0, 255),randint(0, 255), randint(0, 255)))
            star.wrapEdges(WINDOW.getWidth(), WINDOW.getHeight())

        WINDOW.clearScreen()
        for star in STARS:
            WINDOW.getSurface().blit(star.getSurface(), star.getPOS())
        WINDOW.updateFrame()

