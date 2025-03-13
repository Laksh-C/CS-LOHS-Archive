# c_boxes.py
"""
title: box sprites in pygame
author: Laksh Chopra
date-createdd: 2023-12-20
"""

import pygame
from random import randrange


class Box:
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, COLOR=(255, 255, 255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__COLOR = COLOR
        self.__SPEED = 5
        self.__SURFACE = pygame.Surface(self.__DIMENSIONS, pygame.SRCALPHA, 32)
        self.__SURFACE.fill(self.__COLOR)
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # --- MODIFIER METHODS --- #
    ### INPUTS
    def WASDmove(self, KEY_PRESSES):
        """
        move the box based on WASD
        :param KEY_PRESSES: list[int]
        :return:
        """
        if KEY_PRESSES[pygame.K_d] == 1:
            self.__X = self.__X + self.__SPEED
            #if self.__X > MAX_X - self.getWidth():
             #   self.__X = MAX_X - self.getWidth()
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X = self.__X - self.__SPEED
            #if self.__X < MIN_X:
             #   self.__X = MIN_X
        if KEY_PRESSES[pygame.K_w] == 1:
            self.__Y = self.__Y - self.__SPEED
            #if self.__Y < MIN_Y:
             #   self.__Y = MIN_Y
        if KEY_PRESSES[pygame.K_s] == 1:
            self.__Y = self.__Y + self.__SPEED
            #if self.__Y > MAX_Y - self.getHeight():
             #   self.__Y = MAX_Y - self.getHeight()
        self.__POS = (self.__X, self.__Y)


    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X = 0, MIN_Y = 0):
        """

        :param MAX_X:
        :param MAX_Y:
        :param MIN_X:
        :param MIN_Y:
        :return:
        """
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y
        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()

    def wrapEdges(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        """
        if a box goes off screen, send it to the other side
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_X: int
        :param MIN_Y: int
        :return:
        """
        if self.__X > MAX_X:
            self.__X = MIN_X - self.getWidth()
        if self.__X < MIN_X - self.getWidth():
            self.__X  = MAX_X
        if self.__Y > MAX_Y:
            self.__Y = MIN_Y - self.getHeight()
        if self.__Y < MIN_Y - self.getHeight():
            self.__Y = MAX_Y
        self.__POS = (self.__X, self.__Y)


    def setPOS(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setColor(self, TUPLE):
        self.__COLOR = TUPLE  # just cuz we change attribute doesn't mean we update the surface with the color
        self.__SURFACE.fill(self.__COLOR)

    ### PROCESSING
    def bounceX(self, MAX_X, MIN_X = 0):
        self.__X = self.__X + self.__SPEED * self.__DIR_X

        if self.__X > MAX_X - self.getWidth():
            self.__SURFACE.fill((randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            self.__DIR_X = -1
        if self.__X < MIN_X:
            self.__SURFACE.fill((randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            self.__DIR_X = 1

        self.__POS = (self.__X, self.__Y)

    def bounceY(self, MAX_Y, MIN_Y = 0):
        self.__Y = self.__Y + self.__SPEED * self.__DIR_Y

        if self.__Y > MAX_Y - self.getHeight():
            self.__SURFACE.fill((randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            self.__DIR_Y = -1
        if self.__Y < MIN_Y:
            self.__SURFACE.fill((randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            self.__DIR_Y = 1


    # --- ACCESSOR METHODS --- #
    ### OUTPUTS
    def getPOS(self):
        return self.__POS

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()


if __name__ == "__main__":
    from a_template import Window

    pygame.init()

    ### INPUTS
    WINDOW = Window("Boxes")
    RED_BOX = Box(100, 100)
    RED_BOX.setColor((255, 0, 0))
    BLUE_BOX = Box(100, 100)
    BLUE_BOX.setPOS(WINDOW.getWidth() // 2 - BLUE_BOX.getWidth() // 2, WINDOW.getHeight() // 2 - BLUE_BOX.getHeight() // 2)
    BLUE_BOX.setColor((0, 0, 255))


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        BLUE_BOX.WASDmove(PRESSED_KEYS)

        ### PROCESSING
        #BLUE_BOX.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())
        BLUE_BOX.wrapEdges(WINDOW.getWidth(), WINDOW.getHeight())

        RED_BOX.bounceX(WINDOW.getWidth())
        RED_BOX.bounceY(WINDOW.getHeight())

        ### OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(RED_BOX.getSurface(), RED_BOX.getPOS())
        WINDOW.getSurface().blit(BLUE_BOX.getSurface(), BLUE_BOX.getPOS())
        WINDOW.updateFrame()