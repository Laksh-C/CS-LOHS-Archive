# my_sprite.py
"""
title: Parent class for boxes
author: Laksh Chopra
date-created: 07/02/24
"""

import pygame

class MySprite:
    """
    Abstract Sprite Class for pygame sprites
    """

    def __init__(self, WIDTH = 1, HEIGHT = 1, X=0, Y=0, SPEED=12.5, COLOR=(255, 255, 255)):
        self.__WIDTH = WIDTH # private attributes
        self.__HEIGHT = HEIGHT
        self.__X = X
        self.__Y = Y
        self._COLOR = COLOR # partially protected attributes
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self.__COLOR = COLOR
        self._SURFACE = pygame.Surface
        self.__DIR_X = 1
        self.__DIR_Y = 1
        self.__LIVES_REMAINING = 3

    # --- MODIFIER METHODS --- #
    def setX(self, X): # public methods
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def setColor(self, TUPLE):
        self._COLOR = TUPLE

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

    def ADmove(self, KEY_PRESSES, MIN_X = 0, MAX_X = 800):
        """
        move the box based on AD
        """
        if KEY_PRESSES[pygame.K_d] == 1:
            self.__X = self.__X + self.__SPEED
            if self.__X > MAX_X - self.getWidth():
               self.__X = MAX_X - self.getWidth()
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X = self.__X - self.__SPEED
            if self.__X < MIN_X:
                self.__X = MIN_X
        self.__POS = (self.__X, self.__Y)

    def loseLife(self):
        self.__LIVES_REMAINING -= 1

    def setSpeed(self, SPEED):
        self.__SPEED = SPEED

    def setXDIR(self, X_DIRECTION):
        self.__DIR_X = X_DIRECTION

    def setYDIR(self, Y_DIRECTION):
        self.__DIR_Y = Y_DIRECTION

    def bounceWindow(self):
        self.__X = self.__X + self.__SPEED*self.__DIR_X
        if self.__X >= 800 - self.__WIDTH:
            self.__DIR_X = -1
        if self.__X < 0:
            self.__DIR_X = 1
        self.__POS = (self.__X, self.__Y)
        self.__Y = self.__Y + self.__SPEED*self.__DIR_Y
        if self.__Y <= 40:
            self.__DIR_Y = 1
        if self.__Y + self.__HEIGHT>= 600:
            self.__DIR_Y = -1

    # --- ACCESSOR METHODS --- #
    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.__POS

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getSpeed(self):
        return self.__SPEED

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getXDIR(self):
        return self.__DIR_X

    def getYDIR(self):
        return self.__DIR_Y

    def isCollision(self, SURFACE, POS):
        """
        Testing whether the current sprite position is overlapping the given sprite's position
        :param SURFACE: Surface Object
        :param POS: Tuple (int)
        :return: bool
        """
        WIDTH = SURFACE.get_width()
        HEIGHT = SURFACE.get_height()
        X = POS[0]
        Y = POS[1]

        if X >= self.__X - WIDTH and X <= self.__X + self._SURFACE.get_width():
            if Y >= self.__Y - HEIGHT and Y <= self.__Y + self._SURFACE.get_height():
                return True
        return False

    def getLivesRemaining(self):
        return self.__LIVES_REMAINING


