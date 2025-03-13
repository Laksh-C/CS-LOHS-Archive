# box.py
"""
title: class for Bricks
author: Laksh Chopra
date-created: 07/02/24
"""

from my_sprite import MySprite
import pygame

class Box(MySprite):
    def __init__(self, WIDTH = 1, HEIGHT = 1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    def setColor(self, TUPLE):
        MySprite.setColor(self, TUPLE)
        self._SURFACE.fill(self._COLOR)


