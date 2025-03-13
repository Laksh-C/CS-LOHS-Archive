# text.py in e_inheritance
"""
title: Text child class
author: Laksh Chopra
date-created: 2023-12-22
"""

from my_sprite import MySprite
import pygame

class Text(MySprite):
    """
    Subclass of MySprite
    """
    def __init__(self, TEXT, F_FAMILY="Arial", F_SIZE=36):
        MySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_FAMILY = F_FAMILY
        self.__FONT_SIZE = F_SIZE
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setColor(self, TUPLE):
        MySprite.setColor(self, TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Text Subclass")
    TEXT = Text("Hello World")
    TEXT.setColor((255, 255, 0))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), (0, 0))
        WINDOW.updateFrame()
