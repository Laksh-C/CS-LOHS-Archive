# collision_test.py in f_santa

"""
title: collision test
author: Laksh Chopra
date-created: 15/1/24
"""

import pygame
from box import Box
from random import randrange

if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Collision Test")
    BOX_1 = Box(50, 50)
    BOX_2 = Box(150, 150)
    BOX_2.setPOS(
        randrange(0, WINDOW.getWidth() - BOX_2.getSurface().get_width()),
        randrange(0, WINDOW.getHeight() - BOX_2.getSurface().get_height())
    )

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        KEYS_PRESSED = pygame.key.get_pressed()

        # PROCESSING
        BOX_1.WASDmove(KEYS_PRESSED)
        if BOX_1.isCollision(BOX_2.getSurface(), BOX_2.getPOS()):
            print("HIT")

        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BOX_1.getSurface(), BOX_1.getPOS())
        WINDOW.getSurface().blit(BOX_2.getSurface(), BOX_2.getPOS())
        WINDOW.updateFrame()