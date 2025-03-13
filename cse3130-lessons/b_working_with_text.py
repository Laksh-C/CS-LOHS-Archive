# b_working_with_text.py
"""
title: text sprites
author: Laksh Chopra
date-created: 18/12/23
"""

import pygame
from a_template import Window

class Text:
    """
    Creates a text object to put on the screen
    """

    def __init__(self, TEXT, X=0, Y=0, SIZE = 48, FAMILY="Arial"):
        self.__TEXT = TEXT
        self.__FONT_FAMILY = FAMILY
        self.__FONT_SIZE = SIZE
        self.__FONT_COLOR = (0, 255, 0)
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self.__SURFACE = self.__FONT.render(self.__TEXT, 1, self.__FONT_COLOR)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    # --- MODIFIERS --- # SETTER METHODS
    def setPOS(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setColor(self, TUPLE):
        self.__FONT_COLOR = TUPLE
        self.__SURFACE = self.__FONT.render(self.__TEXT, 1, self.__FONT_COLOR)


    def marqueeX(self, MAX_X, MIN_X=0):
        self.__X = self.__X + 5
        if self.__X > MAX_X:
            self.__X = MIN_X - self.getWidth()

        self.__POS = (self.__X, self.__Y)



    # --- ACCESSORS --- # GETTER METHODS
    def getSurface(self):
        return self.__SURFACE

    def getPOS(self):
        return self.__POS

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()







if __name__ == "__main__":

    pygame.init()
    WINDOW = Window("Working with Texts")
    TEXT = Text("Hello World", 250, 250)
    TEXT.setPOS(
        WINDOW.getWidth()//2 - TEXT.getWidth()//2,
        WINDOW.getHeight()//2 - TEXT.getHeight()//2
    )
    TEXT.setColor((97, 237, 255))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        TEXT.marqueeX(WINDOW.getWidth(), WINDOW.getHeight())
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        WINDOW.updateFrame()

