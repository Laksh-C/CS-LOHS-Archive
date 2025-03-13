# my_sprite.py in e_inheritance
"""
title: the parent class
author: Laksh Chopra
date-created: 2023-12-22
"""

import pygame

class MySprite:
    """
    Abstract Sprite Class for pygame sprites
    """

    def __init__(self, WIDTH = 1, HEIGHT = 1, X=0, Y=0, SPEED=5, COLOR=(255, 255, 255)):
        self.__WIDTH = WIDTH # private attributes
        self.__HEIGHT = HEIGHT
        self.__X = X
        self.__Y = Y
        self._COLOR = COLOR # partially protected attributes
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self._COLOR = COLOR
        self._SURFACE = pygame.Surface
        self.__DIR_X = 1
        self.__DIR_Y = 1

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




    # --- ACCESSOR METHODS --- #
    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.__POS
