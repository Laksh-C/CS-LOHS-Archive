# playing_field.py
"""
title: Generates Window, Title Text, and Title Bar for the entire game
author: Laksh Chopra
date-created: 09/02/24
"""

import pygame

class Window:
    """
    creates the window that will load the game
    """

    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30):
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIMENSIONS)
        self.__SURFACE.fill((40, 40, 40))
        pygame.display.set_caption(self.__TITLE)

    ### --- MODIFIER METHODS --- ###
    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.__SURFACE.fill((40, 40, 40))

    ### --- ACCESSOR METHODS --- ###
    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT

class Text:
    """
    Creates a text object to put on the screen
    """
    def __init__(self, TEXT):
        self.__TEXT_CONTENT = TEXT
        self.__FONT = "arial"
        self.__TEXT = pygame.font.SysFont(self.__FONT, 20)
        self.__COLOR_TUPLE = (255, 255, 255)
        self.__SURFACE = self.__TEXT.render(self.__TEXT_CONTENT, 1, self.__COLOR_TUPLE)
        self.__SIZE = 20
        self.__POS = (0, 0)


    ### --- MODIFIER METHODS --- ###
    def setTextSize(self, SIZE):
        self.__TEXT = pygame.font.SysFont(self.__FONT, SIZE)
        self.__SURFACE = self.__TEXT.render(self.__TEXT_CONTENT, 1, self.__COLOR_TUPLE)
        self.__SIZE = SIZE

    def setTextFont(self, FONT):
        self.__TEXT = pygame.font.Font(FONT, self.__SIZE)
        self.__SURFACE = self.__TEXT.render(self.__TEXT_CONTENT, 1, self.__COLOR_TUPLE)
        self.__FONT = FONT

    def setTextColor(self, TUPLE):
        self.__SURFACE = self.__TEXT.render(self.__TEXT_CONTENT, 1, TUPLE)
        self.__COLOR_TUPLE = TUPLE

    def pulseTextColor(self, COLOR, DIRECTION):
        for i in range(3):
            COLOR[i] += 5*DIRECTION[i]
            if COLOR[i] >= 255:
                COLOR[i] = 0
            elif COLOR[i] <= 0:
                COLOR[i] = 255
        self.__SURFACE = self.__TEXT.render(self.__TEXT_CONTENT, 1, COLOR)


    def setPOS(self, X, Y):
        self.__POS = (X, Y)

    ### --- ACCESSOR METHODS --- ###
    def getSurface(self):
        return self.__SURFACE

    def getFont(self):
        return self.__FONT

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()

    def getPOS(self):
        return self.__POS


if __name__ == "__main__":
    pygame.init()
    from box import Box
    from random import randrange

    WINDOW = Window("Brick Breaker", 800, 600, 30)
    SCORE = 0
    SCORE_TEXT = Text(f"SCORE: {SCORE}")
    BRICK_BREAKER_TEXT = Text("BRICK BREAKER!!!")
    BRICK_BREAKER_TEXT.setTextSize(40)
    BRICK_BREAKER_TEXT.setTextFont("varsity_regular.ttf")
    SCORE_TEXT.setTextSize(30)
    SCORE_TEXT.setTextColor((0, 255, 255))

    TITLE_BOX = Box(WINDOW.getWidth(), 40)
    TITLE_BOX.setColor((110, 110, 110))

    BRICK_BREAKER_TEXT.setPOS(WINDOW.getWidth() // 2 - BRICK_BREAKER_TEXT.getWidth() // 2,-4)

    FLASHING_COLOR = [140, 3, 252]



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        BRICK_BREAKER_TEXT.pulseTextColor(FLASHING_COLOR, [randrange(10)/10, randrange(10)/10, randrange(10)/10])
        WINDOW.getSurface().blit(TITLE_BOX.getSurface(), (0, 0))
        WINDOW.getSurface().blit(SCORE_TEXT.getSurface(), (10, 2.5))
        WINDOW.getSurface().blit(BRICK_BREAKER_TEXT.getSurface(), BRICK_BREAKER_TEXT.getPOS())
        WINDOW.updateFrame()